from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class OperadoraSchema(BaseModel):
    registro_ans: int
    cnpj: str = Field(..., min_length=14, max_length=14)
    razao_social: str
    nome_fantasia: Optional[str]
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str]
    bairro: str
    cidade: str
    uf: str = Field(..., min_length=2, max_length=2)
    cep: str = Field(..., min_length=8, max_length=8)
    ddd: Optional[str]
    telefone: Optional[str]
    fax: Optional[str]
    endereco_eletronico: Optional[str]
    representante: str
    cargo_representante: str
    regiao_de_comercializacao: Optional[int]
    data_registro_ans: date

    class Config:
        from_attributes = True
