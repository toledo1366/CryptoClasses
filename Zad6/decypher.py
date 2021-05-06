import string

class Cypher:
    @staticmethod
    def __generate_square__(key):
        big_letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        square = []
        for char in key.upper():
            if char not in square and char in big_letters:
                square.append(char)

        for char in big_letters:
            if char not in square:
                square.append(char)

        return square

    @staticmethod
    def decode(encoded_text, key):
        square = Cypher.__generate_square__(key)
        decoded = ""

        for i in range(0, len(encoded_text), 2):
            char1 = encoded_text[i]
            char2 = encoded_text[i + 1]
            row1, col1 = divmod(square.index(char1), 5)
            row2, col2 = divmod(square.index(char2), 5)

            if col1 == col2:
                decoded += square[((row1 - 1) % 5) * 5 + col1]
                decoded += square[((row2 - 1) % 5) * 5 + col2]
            elif row1 == row2:
                decoded += square[row1 * 5 + (col1 - 1) % 5]
                decoded += square[row2 * 5 + (col2 - 1) % 5]
            else:
                decoded += square[row1 * 5 + col2]
                decoded += square[row2 * 5 + col1]

        return decoded