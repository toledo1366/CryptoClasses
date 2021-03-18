from src.AccountModel import AccountModel


def createAccount():
    """Function creating instance of account"""

    name = input("Enter your name: ")
    password = input("Enter your password: ")
    passwordsMatch = checkPassword(password)
    if passwordsMatch:
        newUser = AccountModel(name, password)
    return newUser


def checkPassword(password):
    """Function checking if given passwords are the same"""

    repeatedPassword = input("Repeat you password: ")
    while password != repeatedPassword:
        print("Passwords are different!")
        repeatedPassword = input("Enter the corrected password: ")
    return True
