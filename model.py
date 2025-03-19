from typing import Optional
from pydantic import BaseModel

class Personagem(BaseModel):
    id: Optional[int]= None
    nome : str
    luta : str
    personalidade : str
    historico : str
    foto : str
