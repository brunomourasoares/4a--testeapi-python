from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, SQLAlchemyError

from exceptions.database_exceptions import DatabaseConnectionError

# Configuração da conexão com o PostgreSQL
DATABASE_URL = "postgresql://python:python123456@localhost:5432/ans_database"

# Criando o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando a base do modelo (não cria nada automaticamente no banco)
Base = declarative_base()

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        # Verifica se a conexão está funcionando
        # Usando text() para especificar explicitamente a consulta SQL
        db.execute(text("SELECT 1"))
        yield db
    except (OperationalError, SQLAlchemyError) as e:
        db.close()
        raise DatabaseConnectionError(f"Falha na conexão com o banco de dados: {str(e)}")
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful")
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
