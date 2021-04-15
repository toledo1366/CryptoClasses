from Cipher import Encoder
from Helpers import Helper
from fileService import FileService


def main():
    code = Encoder()
    converter = Helper()
    service = FileService()
    text = service.readFile("text.txt")
    text = code.move(text, 5)   #the key is 5 :)
    text = code.transform(text)
    text = code.reverse(text)
    text = converter.convertDictToList(text)
    text = converter.convertListToString(text)
    service.writeFile(text)
main()
