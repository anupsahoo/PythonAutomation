import json
import os.path

class allFilesReaders():
    my_path = os.path.abspath(os.path.dirname(__file__))
    _jsonfilepath = os.path.join(my_path, "../DataFiles/data.json")
    _excelfilepath = os.path.join(my_path,"../DataFiles/TestData.xlsx")
    _txtfilepath = os.path.join(my_path,"../DataFiles/menu.txt")

    def readfromjson(self, key):
        """
        reads from json file
        :param key: to get the data of this kay
        :return: Value of that key
        """
        self.key=key
        with open(self._jsonfilepath) as data_file:
            product = json.load(data_file)
            return product[self.key]

    def readbytextfile(self):
        """
        opening the text file to read
        :return: file
        """
        file=open(self._txtfilepath,'r')
        return file

    def readlinebyline(self):
        """
        reading the data line by line from text file
        :return:
        """
        lines=[line.replace("\n","") for line in self.readbytextfile()]
        return lines