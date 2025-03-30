from typing import Optional
from pydantic import BaseModel

class OperadoraDTO(BaseModel):
    registro_ans: int
    cnpj: str
    razao_social: str
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    uf: str
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    endereco_eletronico: Optional[str] = None
    representante: str

    class Config:
        from_attributes = True