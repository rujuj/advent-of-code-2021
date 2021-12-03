# open file and read input
input = open("input.txt")
lines = input.readlines()

horizontal = 0
depth = 0
aim = 0

# parse inputs
for line in lines:
    direction, num = line.split(" ")
    num = int(num.strip("\n"))

    # adjust as required 
    if direction == "forward":
        horizontal += num
        depth += aim * num
    elif direction == "up":
        aim -= num
    elif direction == "down":
        aim += num 

# print results
print(horizontal, depth)
print(horizontal*depth)

# first try: 1911 * 615654 = 1176514794