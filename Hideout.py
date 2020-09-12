from DataBase import DataBaseAccess
class Hideout:
    def __init__(self):
        self.DataBase = DataBaseAccess('ItemsDB.db')
        self.itemsYouNeed = {}
        self.askUserForLevels()


    def ifExistAddElseCreate(self, itemName, Ammount):
        try:
            self.itemsYouNeed[itemName] += Ammount
        except:
            self.itemsYouNeed[itemName] = Ammount

    def fromDBToItems(self, Select):
        for i in range(0, len(Select)):
            self.ifExistAddElseCreate(Select[i][2], Select[i][3])

    def askUserForLevels(self):
        self.DataBase.Cursor.execute('SELECT DISTINCT ModuleName From Hideout')
        modules = self.DataBase.Cursor.fetchall()
        for i in range(0, len(modules)):
            level = input(modules[i][0] + ': ')
            self.itemsForModule(modules[i][0], level)

    def itemsForModule(self, ModuleName, level):
        self.DataBase.Cursor.execute('SELECT ModuleName, level, itemName, ammount FROM Hideout WHERE lower(ModuleName) == lower(\"' + ModuleName + '\") AND level > ' + str(level))
        self.fromDBToItems(self.DataBase.Cursor.fetchall())

    def printAllItems(self):
        for item in self.itemsYouNeed:
            print(item, ': ', self.itemsYouNeed[item])



if __name__ == '__main__':
    test = Hideout()
    test.printAllItems()