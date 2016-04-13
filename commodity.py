import csv
import random


class commodity:
    def __init__(self, name, minPrice, maxPrice, currentPrice, crashChance, boomChance, description, imageFile,
                 availability):
        self.name = name
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.currentPrice = currentPrice
        self.crashChance = crashChance
        self.boomChance = boomChance
        self.description = description
        self.imageFile = imageFile
        self.availability = availability

    def randomise(self):

        #code events
        diceRoll = int(random.randint(1, 100))
        #print ("Randomised commodity " + self.name + " and roll is " + str(diceRoll))
        if diceRoll <= int(self.crashChance):
            self.isCrash()
        elif diceRoll >= (100 - int(self.boomChance)):
            self.isBoom()
        else:

            #print ("dice Roll ",str(diceRoll))
            self.currentPrice = int(random.randint(int(self.minPrice), int(self.maxPrice)))
            #self.currentPrice=random.randint(1,100)

    def isAvailable(self):
        diceRoll = random.randint(1, 100)
        if diceRoll <= int(self.availability):
            return True
        else:
            return False

    def isCrash(self):
        #handle a crash or boom.. .
        print(self.name + " is crashing!")

    def isBoom(self):
        print(self.name + " is booming!")


class commodityReader:
    def __init__(self, sourceFile, name):
        self.name = name
        self.sourceFile = sourceFile
        self.masterList = []
        f = open(self.sourceFile)
        csv_f = csv.reader(f)
        for row in csv_f:
            #print (row)
            self.masterList.append(
                commodity(row[0], int(row[1]), int(row[2]), row[3], row[4], row[5], row[6], row[7], row[8]))
            #print(self.masterList)


    def dump(self):
        for x in range(0, len(self.masterList)):
            if self.masterList[x].isAvailable():

                print(self.masterList[x].name + " costs " + str(self.masterList[x].currentPrice))
            else:
                print(self.masterList[x].name + " ---------------------------")  #not available

    def randmomiseLocation(self):
        for x in self.masterList:
            x.randomise()





