from message import Message
from coders import SymmetricCoders
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): 
    return {"message": "Goooooooood morning Wietnam!"}

@app.get("/sym/key")
async def get_key():
    return SymmetricCoders.generateKey()

@app.post("/sym/")
async def post_key(key):
    symmetricKey = SymmetricCoders(key)
    global coder
    coder = FastAPI(key)
    return {"message:", "Key has been set"}

@app.post("/sym/message_encoded")
async def postSymmetricEncodedMessage(message:Message):
    encodedMessage = coder.Encoder(message.body)
    return encodedMessage

@app.post("/sym/message_decoded")
async def postSymmetricDecodedMessage(message:Message):
    decodedMessage=coder.Decoder(message.body)
    return decodedMessage