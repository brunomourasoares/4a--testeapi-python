from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from typing import List, Optional, Tuple
from models.operadora_model import Operadora
from models.operadora_dto import OperadoraDTO
from exceptions.database_exceptions import DatabaseConnectionError

def buscar_operadoras(db: Session, termo: str, pular: int = 0, quantidade: int = 10) -> Tuple[List[OperadoraDTO], int]:
    try:
        if not termo or not termo.strip():
            return [], 0
            
        termo = termo.strip()
        query = db.query(Operadora).filter(
            (Operadora.cnpj.ilike(f"%{termo}%")) | 
            (Operadora.razao_social.ilike(f"%{termo}%")) | 
            (Operadora.nome_fantasia.ilike(f"%{termo}%")) | 
            (Operadora.modalidade.ilike(f"%{termo}%")) | 
            (Operadora.uf.ilike(f"%{termo}%")) | 
            (Operadora.cidade.ilike(f"%{termo}%")) | 
            (Operadora.bairro.ilike(f"%{termo}%")) | 
            (Operadora.cep.ilike(f"%{termo}%")) | 
            (Operadora.representante.ilike(f"%{termo}%"))
        )
        
        # Contar o total de itens antes de aplicar a paginação
        total = query.count()
        
        # Aplicar a paginação
        operadoras = query.offset(pular).limit(quantidade).all()
        
        return [OperadoraDTO.model_validate(operadora) for operadora in operadoras], total
    
    except OperationalError as e:
        print(f"Erro de conexão com o banco de dados: {str(e)}")
        raise DatabaseConnectionError(f"Falha na conexão com o banco de dados: {str(e)}")
    
    except SQLAlchemyError as e:
        print(f"Erro SQL ao buscar operadoras: {str(e)}")
        # Se não for um erro de conexão, apenas propaga o erro
        raise
    
    except Exception as e:
        print(f"Erro inesperado ao buscar operadoras: {str(e)}")
        raise