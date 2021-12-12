# open file :)
input = open("input.txt")
lines = input.readlines()

coordinates = []
max_x = 0
max_y = 0

# find out the dimensions to initialize the map 
for line in lines:
    coord1, coord2 = line.strip("\n").split(" -> ")
    x1, y1 = [int(x) for x in coord1.split(",")]
    x2, y2 = [int(x) for x in coord2.split(",")]
    coordinates.append([[x1, y1], [x2, y2]])
    # find the largest x and y coordinates 
    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    if y2 > max_y:
        max_y = y2

# initialize the map 
map = [[0] * (max_y + 1) for _ in range(max_x + 1)]
# print(map)
# print(len(map))
# print(len(map[0]))

# for each set of coordinates, mark the vents with numbers (increment by 1)

# REDO THIS SHIT LOL

for vent in coordinates:
    print(vent)
    # if the 2 y-coordinates match, it's a horizontal line
    if vent[0][0] == vent[1][0]:
        y = vent[0][0]
        if vent[0][0] > vent[1][0]:
            x1 = vent[0][0]
            x2 = vent[1][0]
        else:
            x1 = vent[1][0]
            x2 = vent[0][0]
        print(range(x1, x2+1))
        for x in range(x1, x2 + 1):
            if map[x][y] == None:
                map[x][y] = 1
            else:
                map[x][y] += 1
    # if the 2 x-coordinates match, it's a vertical line
    elif vent[0][1] == vent[1][1]:
        x = vent[0][1]
        if vent[1][0] > vent[1][1]:
            y1 = vent[1][0]
            y2 = vent[1][1]
        else:
            y1 = vent[1][1]
            y2 = vent[1][0]
        print(range(y1, y2+1))
        for y in range(y1, y2 + 1):
            if map[x][y] == None:
                map[x][y] = 1
            else:
                map[x][y] += 1

dangerous = 0
for row in map:
    for spot in row:
        if spot >= 2:
            dangerous += 1
    print(row)

print(dangerous)



# 