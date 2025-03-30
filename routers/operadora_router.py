from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from math import ceil

from database.database import get_db
from services.operadora_service import buscar_operadoras
from models.operadora_dto import OperadoraDTO
from models.operadora_pagination import PaginationResponse

router = APIRouter()

@router.get("/api/operadoras/", response_model=PaginationResponse[OperadoraDTO])
def buscar(
    termo: str = Query(..., description="Termo de busca"), 
    pagina: int = Query(1, ge=1, description="Página atual"),
    quantidade: int = Query(10, ge=1, le=100, description="Número de itens por página"),
    db: Session = Depends(get_db)
):
    # Convertendo página para skip
    pular = (pagina - 1) * quantidade
    
    # Buscando operadoras com paginação
    items, total = buscar_operadoras(db, termo, pular, quantidade)
    
    # Calculando o total de páginas
    total_paginas = ceil(total / quantidade) if total > 0 else 0
    
    return PaginationResponse(
        items=items,
        total=total,
        pagina=pagina,
        quantidade=quantidade,
        paginas=total_paginas,
        tem_proximo=pagina < total_paginas,
        tem_anterior=pagina > 1
    )