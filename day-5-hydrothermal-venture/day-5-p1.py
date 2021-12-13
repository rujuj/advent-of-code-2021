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
# the row indicates the y value
# the column indicates the x value 
map = [[0] * (max_x + 1) for _ in range(max_y + 1)]

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

dangerous = 0
for row in map:
    for spot in row:
        if spot >= 2:
            dangerous += 1
    print(row)
print(dangerous)

# so I did this and then had to re-do the whole thing because I confused myself too much 
# realized during debugging that I was including input that contained diagonal vents oops

# first attempt: 5442 - correct