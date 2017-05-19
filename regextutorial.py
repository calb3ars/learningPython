#!/usr/bin/python
import re

play = "Steph Curry dribbles left, steps to the right, launches the shot...three is good!"

matchCall = re.match(r'launches', play, re.M|re.I)

if matchCall:
    print "match --> matchCall.group() : ", matchCall.group()
else:
    print "No match!"

searchCall = re.search( r'the', play, re.M|re.I)
if searchCall:
    print "search --> searchCall.group() : ", searchCall.group()
else:
    print "Nothing found"
