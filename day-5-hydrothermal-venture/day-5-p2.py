# open file :)
input = open("input.txt")
lines = input.readlines()

coordinates = []
maxX = 0
maxY = 0

# find out the dimensions to initialize the map 
for line in lines:
    coord1, coord2 = line.strip("\n").split(" -> ")
    x1, y1 = [int(x) for x in coord1.split(",")]
    x2, y2 = [int(x) for x in coord2.split(",")]
    coordinates.append([[x1, y1], [x2, y2]])
    # find the largest x and y coordinates 
    if x1 > maxX:
        maxX = x1
    if x2 > maxX:
        maxX = x2
    if y1 > maxY:
        maxY = y1
    if y2 > maxY:
        maxY = y2

# initialize the map 
# the row indicates the y value
# the column indicates the x value 
map = [[0] * (maxX + 1) for _ in range(maxY + 1)]
dangerous = 0

# for each set of coordinates, mark the vents with numbers (increment by 1)
for vent in coordinates:
    # split into x1, x2, y1, y2
    coord1 = vent[0]
    coord2 = vent[1]
    # x values match
    if coord1[0] == coord2[0]:
        # defaults
        # print("x not running")
        x = coord1[0]
        y1 = coord1[1]
        y2 = coord2[1]
        # mark along the range of y values in that column
        if coord1[1] > coord2[1]:
             # they need to go backwards
            y1 = coord2[1]
            y2 = coord1[1]
           
        for y in range(y1, y2 + 1):
            map[y][x] += 1
            if map[y][x] == 2:
                dangerous += 1

    elif coord1[1] == coord2[1]:
        # defaults
        y = coord1[1]
        x1 = coord1[0]
        x2 = coord2[0]
        if coord1[0] > coord2[0]:
            # they need to go backwards
            x1 = coord2[0]
            x2 = coord1[0]
        
        for x in range(x1, x2 + 1):
            map[y][x] += 1
            if map[y][x] == 2:
                dangerous += 1
    
    # diagonal lines:
    else: 
        x1, y1 = coord1
        x2, y2 = coord2
        
        increaseXBy = 1
        increaseYBy = 1

        # 4 scenarios

        # bottom right to top left
        if x1 > x2 and y1 > y2:
            print("backwards")
            # just swap these 2 coordinates and continue as usual 
            temp1, temp2 = [x1, y1]
            x1, y1 = [x2, y2]
            x2, y2 = [temp1, temp2]
        # top right to bottom left 
        elif x1 > x2 and y2 > y1:
            print("top right to bottom left")
            print(x1, y1, x2, y2)
            increaseXBy = -1
        # bottom left to top right
        elif x2 > x1 and y1 > y2:
            print("bottom left to top right")
            print(x1, y1, x2, y2)
            increaseYBy = -1
        # top left to bottom right
        # no changes to anything
        else:
            print("normal")

        populating = True
        currX = x1
        currY = y1
        while(populating):
            print(currX, currY)
            map[currY][currX] += 1
            if map[currY][currX] == 2:
                dangerous += 1
            if currX == x2:
                populating = False
                print(currY, y2)
                assert(currY == y2)
            currX += increaseXBy
            currY += increaseYBy

for row in map:
    print(row)
print(dangerous)

# messed up sooooo many times doing the diagonals 
# first attempt: 19571 - correct
# seems like i'm getting better at testing