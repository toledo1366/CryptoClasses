def decypher(text, jump):
    newText = []
    for i in range(len(text)):
            asciiCode = ord(text[i])
            if(asciiCode != 32):
                newAscii = asciiCode + jump
                if(newAscii > 122):
                    newAscii = (newAscii-122) + 96
                elif(newAscii > 90 and newAscii < 97):
                    newAscii = (newAscii-90) + 65
                newText.append(chr(newAscii))
            else:
                newText.append(chr(asciiCode))
    return newText        
        