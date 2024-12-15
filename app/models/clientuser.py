from pydantic import BaseModel

class Client(BaseModel):
    name: str
    location: str
    description: str | None = None
    usermail: str
    phone: str