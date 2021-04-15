class FileService:
    text = ""
    def readFile(self, path):
        """Read from file

        Args:
            path (string): Path to file.

        Returns:
            [string]: File content.
        """
        file = open(path, "r")
        for line in file:
            self.text += line
        file.close()
        return self.text

    def writeFile(self, text):
        """Write to file.

        Args:
            text (string): Encoded text.
        """
        file = open("decryptedText.txt", "a")
        file.write(text)
        file.close()

    