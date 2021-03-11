import unittest
from src.Hash import Hash

class TestHash(unittest.TestCase):
    def test_ubuntu_hash(self):
        path = "../ubuntu-20.04.2.0-desktop-amd64.iso"
        h =Hash()
        result = h.hashFile(path)
        self.assertEqual(result, "93bdab204067321ff131f560879db46bee3b994bf24836bb78538640f689e58f")

    def test_create_table(self):
        tab = []
        h = Hash()
        result = h.createHashTable()
        self.assertEqual(type(tab), type(result))


