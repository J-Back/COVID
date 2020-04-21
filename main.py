import pandas as pd

import alabama, arizona, connecticut, delaware, florida, georgia, hawaii, new_hampshire, new_jersey, new_mexico, north_carolina

dataCoronavirus = []

def RunScraping():
    alabama.Main()
    # arizona.Main()
    connecticut.Main()
    florida.Main()
    georgia.Main()
    hawaii.Main()
    new_hampshire.Main()
    # new_jersey.Main()
    new_mexico.Main()
    north_carolina.Main()

def Main():
    RunScraping()

if __name__ == '__main__':
    Main()
