from models.message import *
from coders import *
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
    """Gets private and public hex keys.

    Returns:
        JSON: HEX keys.
    """
    asymmetric.generateKeys()
    keys = asymmetric.getHex()
    return {"Private key:":f"{keys[0]}", "Public key:":f"{keys[1]}"}

@app.get("/asym/keys/ssh")
async def getSshKeys():
    """Gets private and public SSH keys.

    Returns:
        JSON: SSH keys.
    """
    ssh_keys = asymmetric.getSsh()
    return {"Private SSH key":f"{ssh_keys[0]}", "Public SSH key":f"{ssh_keys[1]}"}

@app.post("/asym/keys")
async def postKeys(privateKey, publicKey):
    """Posts private and public HEX keys.

    Args:
        privateKey (HEX): Private hex key.
        publicKey (HEX): Public hex key.
    """
    asymmetric.setKeys(privateKey, publicKey)
    return{"message": "Keys have been set."}

@app.post("/asym/sign")
def postAsymmetricSingResponse(message: Message):
    """Posts signed message.

    Args:
        message (Message): Message content.

    Returns:
        JSON: Signed message content. 
    """
    signedMessage = asymmetric.signMessage(message.body)
    return {"Signed Message": f"{signedMessage}"}

@app.post("/asym/verify")
def postAsymmetricVerifyResponse(message:SignedMessage):
    """Posts response if message was verified.

    Args:
        message (SignedMessage): Message raw and message signed.

    Returns:
        JSON: Information if message was verified.
    """
    result = asymmetric.verifyMessage(message.body, message.signature)
    return {"Verification result":f"{result}"}

@app.post("/asym/encode")
def postEncodedMessage(message:Message):
    """Posts encoded message.

    Args:
        message (Message): Raw message content.

    Returns:
        JSON: Response with encoded message.
    """
    encodedMessage = asymmetric.encode(message.body)
    return {"Message":f"{encodedMessage}"}

@app.post("/asym/decode")
def postDecodedMessage(message:Message):
    """Posts decoded message.

    Args:
        message (Message): Encoded message content.

    Returns:
        JSON: Response with decoded message.
    """
    decodedMessage=asymmetric.decode(message.body)
    return {"Message":f"{decodedMessage}"}
