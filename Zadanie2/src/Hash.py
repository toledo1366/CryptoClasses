import hashlib
import timeit
import random
import string
import plotly.express as px

class Hash(object):
    def __init__(self):
        pass

    def createHashTable(self):
        hashes = []
        for hash_algo in sorted(hashlib.algorithms_available):
            hashes.append(hashlib.new(hash_algo))
        return hashes


    def hashing(self, text)->None:
        hashesList = Hash.createHashTable(text)
        for cell in hashesList:
            cell.update(text.encode())
            print('{}: {}'.format(cell, timeit.default_timer()))

    def hashFile(self, filePath):
        f = open(filePath, "rb")
        hashedFile = hashlib.sha256(f.read()).hexdigest()
        print(hashlib.sha256(f.read()).hexdigest())
        print("Time: {}".format(timeit.default_timer()))
        return hashedFile

    def createPlot(self)->None:
        obj = {
            'word_length': [],
            'time': []
        }
        for i in range(5, 30):
            letters = string.ascii_lowercase
            obj['word_length'].append(len(random.choices(letters + string.digits, k=i)))
            obj['time'].append(timeit.timeit())
        plot = px.line(obj, 'word_length', 'time')
        plot.show()


