from src.Hash import Hash

if __name__ == '__main__':
    h = Hash()
    text = input("Enter some text: ")
    result1 = h.hashing(text)
    result2= h.hashFile("file.txt")
    result3=h.createPlot()