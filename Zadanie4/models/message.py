from pydantic import BaseModel

class Message(BaseModel):
    body : str
 
class SignedMessage(BaseModel):
    body : str
    signature : str

