import csv
import commodity


class location:
    #Constructor for the location object
    def __init__(self, name, description, imageFile, riskFactor, eventChance):
        self.name = name
        self.description = description
        self.imageFile = imageFile
        self.riskFactor = riskFactor
        self.eventChance = eventChance
        #Each location contains a commodityContainer
        self.commodititiesList = commodity.commodityContainer("commodityData.txt", self.name + "Contents")

    #Method which calls the dump method of a locations commoditiesList object. .
    def dumpContent(self):
        self.commodititiesList.dump()
    #Method which calls the RandomiseLocation method of a locations commoditiesList object. .
    def randomiseLocation(self):
        self.commodititiesList.randmomiseLocation()


class locationContainer:
    #Constructor for a container of locations
    #populated from a supplied text file
    #each location object contains a commoditiesList object which holds commoditi
    def __init__(self, sourceFile, name):
        self.name = name
        self.sourceFile = sourceFile
        self.masterList = []
        f = open(self.sourceFile)
        csv_f = csv.reader(f)
        for row in csv_f:
            #print (row)
            self.masterList.append(location(row[0], (row[1]), (row[2]), row[3], row[4]))
            #print(self.masterList)

    def rando(self):
        for x in range(0, len(self.masterList)):
            self.masterList[x].randomiseLocation()


    def dump(self):
        for x in range(0, len(self.masterList)):
            print(self.masterList[x].name + "  -   " + self.masterList[x].description)
            self.masterList[x].dumpContent()
        print()

