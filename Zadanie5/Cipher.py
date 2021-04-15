import hashlib
from collections import OrderedDict

class Encoder:
    """Class responsible for encoding message
    """
    def move(self, text:str, jump:int)->list:
        """Something like Ceasar-cypher. Replacing letters by given jump.

        Args:
            text (str): Text to encode.
            jump (int): Jump length

        Returns:
            list: Encoded text.
        """
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

    def transform(self, text:list)->dict:
        """Transforms list to dictionary to make cypher a bit complicated.

        Args:
            text (list): Encoded text.

        Returns:
            dict: Encoded text harder.
        """
        modules = {}
        index = 0
        times = 0

        if(len(text)%20 == 0):
            length = len(text)/20
        else:
            length = (len(text)/20)+1

        for i in range(int(length)):
            modules[i] = []
        for j in text:
            if(times != 20):
                modules[index].append(j)
                times+=1
            else:
                modules[index].append(j)
                times = 0
                index +=1
        return modules

    def reverse(self, text:dict)->list:
        """Reversing dictionary from the end to the start of text.

        Args:
            text (dict): Encoded text harder.

        Returns:
            list: The hardest encoded text.
        """
        return dict(reversed(list(text.items())))


            