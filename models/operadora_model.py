from sqlalchemy import Column, Integer, String, Date
from database.database import Base

class Operadora(Base):
    __tablename__ = "cadop"
    __table_args__ = {'extend_existing': True}  # Garantir que use a tabela existente

    registro_ans = Column(Integer, primary_key=True, unique=True, nullable=False)
    cnpj = Column(String(14), nullable=False)
    razao_social = Column(String(150), nullable=False)
    nome_fantasia = Column(String(150), nullable=True)
    modalidade = Column(String(50), nullable=False)
    logradouro = Column(String(50), nullable=False)
    numero = Column(String(15), nullable=False)
    complemento = Column(String(40), nullable=True)
    bairro = Column(String(30), nullable=False)
    cidade = Column(String(30), nullable=False)
    uf = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
    ddd = Column(String(3), nullable=True)
    telefone = Column(String(20), nullable=True)
    fax = Column(String(18), nullable=True)
    endereco_eletronico = Column(String(50), nullable=True)
    representante = Column(String(50), nullable=False)
    cargo_representante = Column(String(40), nullable=False)
    regiao_de_comercializacao = Column(Integer, nullable=True)
    data_registro_ans = Column(Date, nullable=False)
