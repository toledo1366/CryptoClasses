from models.message import Message
from coders import Symmetric, Asymmetric
from fastapi import FastAPI
from typing import Optional

app = FastAPI()
symmetric = Symmetric()
asymmetric = Asymmetric()

@app.get("/")
async def root(): 
    """Basic root route.

    Returns:
        JSON: Hello message.
    """
    return {"message": "Goooooooood morning Wietnam!"}

# Symmetric routes
@app.get("/sym/key")
def getKey():
    """Methods getting generated key.

    Returns:
        HEX:Symmetric key.
    """
    key = symmetric.generateKey()
    return key


@app.post("/sym/key")
def postKey(key):
    """Posts symmetric key.

    Args:
        key (HEX): Symmetric key.

    Returns:
        JSON: Information if symmetric key has been set.
    """
    symmetric.setKey(key)
    return {"message": "Key has been set."}


@app.post("/sym/encode")
async def postMessageEncodedSym(message: Message):
    """Posts encoded message.

    Args:
        message (Message): Message object.

    Returns:
        JSON: Encoded message.
    """
    messageEncoded = symmetric.encode(message.body)
    return {"Encoded Message": f"{messageEncoded}"}


@app.post("/sym/decode")
async def postMessageDecodedSym(message: Message):
    """Posts decoded message.

    Args:
        message (Message): Message object.

    Returns:
        JSON: Decoded message.
    """
    messageDecoded = symmetric.decode(message.body)
    return {"Decoded Message": f"{messageDecoded}"}

# Asymmetric routes
@app.get("/asym/keys")
async def getKeys():
    keys = asymmetric.generateKeys()
    return {"Private key:":f"{keys[0]}", "Public key:":f"{keys[1]}"}

@app.get("/asym/keys/ssh")
async def getSshKeys():
    ssh_keys = asymmetric.generateSshKeys()
    return {"Private SSH key":f"{ssh_keys[0]}", "Public SSH key":f"{ssh_keys[1]}"}