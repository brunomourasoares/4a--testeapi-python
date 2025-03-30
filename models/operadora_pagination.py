from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel

T = TypeVar('T')

class PaginationResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    pagina: int
    quantidade: int
    paginas: int
    tem_proximo: bool
    tem_anterior: bool