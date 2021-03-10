import hashlib
import timeit
from base64 import encode
import plotly.express as px

class Hash(object):
    def __init__(self):
        pass

    def createHashTable(self):
        hashes = []
        for hash_algo in sorted(hashlib.algorithms_available):
            hashes.append(hashlib.new(hash_algo))
        return hashes


    def hashing(text):
        hashesList = Hash.createHashTable(text)
        for cell in hashesList:
            cell.update(text.encode())
            print('{}: {}'.format(cell, timeit.default_timer()))

    def hashFile(filePath):
        f = open(filePath, "rb")
        print(hashlib.sha256(f.read()).hexdigest())
        print("Time: {}".format(timeit.default_timer()))

    def plot(filePath):
        tab = Hash.createHashTable(filePath)
        f = open(filePath, "r")
        z = f.read().encode()
        data = []
        for a in tab:
            data.append(a.update(z))
        fig = px.bar(data)
        fig.show()


#Zad1
#Hash.hashing(input("Enter some text: "))

#Zad2 and Zad3
#Hash.hashFile("ubuntu.iso")

#Zad4
Hash.plot("file.txt")
