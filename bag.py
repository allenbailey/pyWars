import commodity
import playerCommodity

import csv

class bag:
    #constructor for the commority object
    def __init__(self, name,initialCapacity):
        self.name=name
        self.startCash=2000
        self.bagCapacity=initialCapacity
        self.contents={}
        f = open("commodityData.txt")
        csv_f = csv.reader(f)
        for row in csv_f:
            #print (row)
            self.contents[int (row[0])]=commodity.commodity(int(row[0]), (row[1]), int(row[2]), row[3], row[4], row[5], row[6], row[7], row[8],row[9])
            #print(self.masterList)


    def addContents(self,type,ammount):
        pass
    def removeContents(self, type, ammount):
        pass
    def increaseBagSize(self,sizeToIncrease):
        pass
    def displayBagContents(self):
        print ("Displaying Player bag contents")
        #print (self.contents)
        for a in self.contents.keys():
            print (a)
            print (self.contents[a].name)



    def calcFreeSpace(self):
        pass
        if (len(self.contents)>1):
            for  thing in self.contents:
                pass
            return self.bagCapacity-10000

        else:
            return self.bag



