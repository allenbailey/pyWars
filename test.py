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


def main():
    world = location.locationContainer("locationData.txt", "The World")
    world.dump()
    world.rando()
    world.dump()


if __name__ == '__main__':
    main()
