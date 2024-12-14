from pydantic import BaseModel

class clientuser(BaseModel):
    client_name : str
    location : str
    description : str
    status : bool

    

    