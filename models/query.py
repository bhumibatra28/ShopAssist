from pydantic import BaseModel

class MessageQuery(BaseModel):
    query: str
    no_of_recomendations: int = 5