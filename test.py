roster = ["Buster", "Brandon", "Joe", "Christian", "Brandon", "Hunter"]

for batter in roster:
    if (batter == "Christian"):
        print("The rookie steps up to the plate")
        continue
    elif (batter == "Joe"):
        pass
        print("Number 12 digs in")
    else:
        print(batter + " steps into the box")
