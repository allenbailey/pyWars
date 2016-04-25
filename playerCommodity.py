import commodity

#clas which extends the commodity clas by adding a quantity attribute so it can be used in the player bag
#is this redundant - do we need a quanityt attribute anyway as a function of a commodities
#availability in a  given location!


class playerCommodity(commodity.commodity):

     def __init__(self, quantity, id,name, minPrice, maxPrice, currentPrice, crashChance, boomChance, description, imageFile,
                 availability):

        commodity.commodity.__init__(self, id,name, minPrice, maxPrice, currentPrice, crashChance, boomChance, description, imageFile,availability)

        self.quantity=quantity









