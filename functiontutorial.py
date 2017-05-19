import pdb
# required Arguments
def printme( str ):
    print str
    return;

# printme( "Buster Posey" )

def walkup( player, number = 28):
    print "Now batting, {}...{}!!".format(str(number), player)
    return;

# walkup("Buster Posey")

def roster( number, *additionalplayers ):
    i = 1
    print "{} {}".format(i, number)
    i += 1
    for player in additionalplayers:
        pdb.set_trace()
        print "{} {}".format(i, player)
        i += 1

    return

# roster(28)
roster(28, 12, 2, 8, 9, 35, 22)
