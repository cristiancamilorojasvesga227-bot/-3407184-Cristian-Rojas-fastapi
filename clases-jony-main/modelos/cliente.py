from pydantic import BaseModel

class client(BaseModel):
    id: int
    name: str
    age: int
    description: str   |None=None

    class ClienteCrear(ClienteBase):
        pass

    class Cliente(ClienteBase):
        id: int |None = None