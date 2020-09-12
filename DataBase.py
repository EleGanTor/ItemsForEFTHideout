import sqlite3
import os
class DataBaseAccess:
    def __init__(self, DataBaseName):
        os.remove('ItemsDB.db')
        self.Connection = sqlite3.connect(DataBaseName)
        self.Cursor = self.Connection.cursor()
        self.CreateFromFile('createTables.txt')
        self.InsertFromFile('tableCSV.csv')

    def CreateFromFile(self, FileName):
        f = open(FileName, 'r')
        stringToExecute = ''
        for line in f:
            stringToExecute += line.replace('\n', '')
        self.Connection.execute(stringToExecute)
        self.Connection.commit()
        f.close()

    def InsertFromFile(self, FileName):
        f = open('tableCSV.csv', 'r')
        header = None
        for line in f:
            if not header:
                header = ''
                s = line.replace('\n', '').split(';')
                for i in range(0, len(s) - 1):
                    header += s[i] + ', '
                header += s[len(s) - 1]
                continue
            s = '\"'
            s += line.replace('\n', '').replace(';', '\", \"') + '\"'
            self.Connection.execute('Insert Into Hideout (' + header + ') Values(' + s + ');')
            self.Connection.commit()

if __name__ == '__main__':
    test = DataBaseAccess('ItemsDB.db')