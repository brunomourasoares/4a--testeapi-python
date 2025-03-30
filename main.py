from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import operadora_router
from exceptions.database_exceptions import DatabaseConnectionError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(DatabaseConnectionError)
async def database_exception_handler(request: Request, exc: DatabaseConnectionError):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"detail": "O serviço está temporariamente indisponível. O banco de dados está offline."}
    )

app.include_router(operadora_router.router)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health_check():
    from database.database import test_connection
    from sqlalchemy import text
    from sqlalchemy.exc import SQLAlchemyError
    
    try:
        # Teste mais robusto usando uma conexão direta
        from database.database import engine
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).fetchone()
            if result and result[0] == 1:
                return {"status": "ok", "database": "connected"}
            else:
                return JSONResponse(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    content={"status": "error", "database": "response invalid"}
                )
    except SQLAlchemyError as e:
        print(f"Health check error: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "error", "database": "disconnected", "detail": str(e)}
        )
    except Exception as e:
        print(f"Unexpected health check error: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"status": "error", "detail": str(e)}
        )
