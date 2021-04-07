from models.message import Message
from models.key import Key
from coders import SymmetricCoders
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def root(): 
    """Root function.

    Returns:
        JSON: Welcome message :)
    """
    return {"message": "Goooooooood morning Wietnam!"}

@app.get("/sym/key")
async def get_key():
    return SymmetricCoders.GenerateKey()

@app.post("/sym/")
async def post_key(key:Key):
    global coder
    coder = SymmetricCoders(key.value)
    return {"message:", "Key has been set."}

@app.post("/sym/message_encoded")
async def postSymmetricEncodedMessage(message:Message):
    encodedMessage = coder.Encoder(message.body)
    return encodedMessage

@app.post("/sym/message_decoded")
async def postSymmetricDecodedMessage(message:Message):
    decodedMessage=SymmetricCoders.Decoder(message.body)
    return decodedMessage

