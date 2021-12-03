# open file and read input
input = open("input.txt")
lines = input.readlines()

horizontal = 0
depth = 0

# parse inputs
for line in lines:
    direction, num = line.split(" ")
    num = int(num.strip("\n"))
    print(direction, num)

    # adjust as required 
    if direction == "forward":
        horizontal += num
    elif direction == "up":
        depth -= num
    elif direction == "down":
        depth += num 

# print results
print(horizontal, depth)
print(horizontal*depth)

# first try: 1911 * 779 = 1488669 - correct