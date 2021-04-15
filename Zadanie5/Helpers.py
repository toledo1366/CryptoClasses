class Helper:
    """Class responsible for distrubute helping functions like converters.
    """
    def convertListToString(self, list:list)->str:
        """Converting list to string.

        Args:
            list (list): List to convert.

        Returns:
            str: Converted list to string.
        """
        text = ''.join([str(letter) for letter in list])
        return text

    def convertDictToList(self, dict:dict)->list:
        """Converting dictionary for list

        Args:
            dict (dict): Dictionary to convert.

        Returns:
            list: Converted dictionary to list.
        """
        newlist=[]
        for i in range(len(dict)):
            newlist+=dict[i]
        return newlist