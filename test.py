#-------------------------------------------------------------------------------
# Name:        module1oooooo
# Purpose:
#
# Author:      baileya
#
# Created:     12/04/2016
# Copyright:   (c) baileya 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#import commodity
import location
import player
import playerCommodity


def main():

    p1= player.player("Bailey")




    world = location.locationContainer("locationData.txt", "The World")
    world.dump()
    world.rando()
    world.dump()

    print ("--------------------------------------------------------")
    p1.playersBag.displayBagContents()

if __name__ == '__main__':
    main()
