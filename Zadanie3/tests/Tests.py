import unittest
from src.AccountModel import AccountModel
import src.Saver as saver


class TestEx3(unittest.TestCase):

    def test_creating_user(self):
        account = saver.createAccount()
        self.assertIsInstance(account, AccountModel)

    def test_repeating_password(self):
        password = "abcd"
        isSame = saver.checkPassword(password)
        self.assertEqual(isSame, True)

