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

map = [["."] * max_x] * max_y
print(map)
print(len(map))
print(len(map[0]))

# 