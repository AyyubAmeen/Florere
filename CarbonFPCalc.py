#All emissions will be calculated in pounds(lbs).
totalEm = 0
points = 0
x = 0

emissions = {
    "car": 0.78,
    "bike": 0,
    "walk": 0,
    "bus": 0.4,
    "plane": 53,
    "public transport": 0.14
}

def transportEm(points, emissions):
    y = 0
    totalTransportEm = 0
    transportMethod = input("What did you use to travel today?\n(car, bike, walk, bus, plane, public transport or type END to stop adding): ")
    while y == 0:
        if transportMethod == "car" or "plane":
            totalTransportEm += emissions[transportMethod]
            points -= 10
        elif transportMethod == "bus" or "public transport":
            totalTransportEm += emissions[transportMethod]
            points += 5
        elif transportMethod == "walk" or "bike":
            points += 10
        elif transportMethod == "END":
            y += 1
            break
        else:
            transportMethod = input("What did you use to travel today\n(car, bike, walk, bus, plane, public transport or type END to stop adding): ")
            pass
        transportMethod = input("What did you use to travel today\n(car, bike, walk, bus, plane, public transport or type END to stop adding): ")
    return totalTransportEm, points

def houseEm(points):
    energy = input("Do you use sustainable energy or not? (Yes or No)")
    if energy == "yes":
        energyEm = 0
        points += 10
    else:
        energyEm = (0.889 * 10,649)
        points -= 10
        refrig = input("Do you use a refrigerator or not? (Yes or No)")
        if refrig == "yes":
            refrigEm = 672
            points -= 3
        else:
            refrigEm = 0
            points += 3
    totalHouseEm = energyEm + refrigEm
    return totalHouseEm, points

def foodEm(points):
    meatPrcnt = int(input("How much meat did you eat on average today compared to other foods?\n(Enter an integer percentage, e.g. 50):"))
    dairyPrcnt = int(input("How much dairy did you eat/drink on average today compared to other foods?\n(Enter an integer percentage, e.g. 50):"))
    otherPrcnt = 100 - meatPrcnt - dairyPrcnt
    meatEm = ((9.59*3)*(meatPrcnt/100))
    points -= 10 * (meatPrcnt/100)
    dairyEm = ((4.06*3)*(dairyPrcnt/100))
    points -= 5 * (dairyPrcnt/100)
    otherEm =  ((0.37*3)*(otherPrcnt/100))
    points += 10 * (otherPrcnt/100)
    totalFoodEm = meatEm + dairyEm + otherEm
    return totalFoodEm, points

addActivity = input("Would you like to add an activity? Type in either: transport, food or household to update your daily emissions,\nor type in END to finish adding activities!: ")

while x == 0:
    if addActivity == "transport":
        totalEm += int((transportEm(points,emissions))[0])
        points += int((transportEm(points,emissions))[1])
    elif addActivity == "household":
        totalEm += int((houseEm(points))[0])
        points += int((houseEm(points))[1])
    elif addActivity == "food":
        totalEm += int((foodEm(points))[0])
        points += int((foodEm(points))[1])
    elif addActivity == "END":
        x += 1
        break
    else:
        pass
    addActivity = input("Would you like to add an activity? Type in either: transport, food or household to update your daily emissions,\nor type in END to finish adding activities!: ")

print("You've emitted " + str(totalEm) + " lbs today.\nYou have also gained " + str(points) + " points.")