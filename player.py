import bag


class player:
    #constructor for the commority object
    def __init__(self, name):
        self.name=name
        self.startCash=2000
        self.startBagCapacity=80
        self.startDebt=0
        self.playersBag=bag.bag(self.name + "'s Bag ", self.startBagCapacity)
