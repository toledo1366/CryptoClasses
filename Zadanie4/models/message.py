from pydantic import BaseModel

class Message(BaseModel):
    body : str

