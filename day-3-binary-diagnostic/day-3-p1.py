# open file and read input
input = open("input.txt")
lines = input.readlines()

# initialize variables
tracker = [0] * (len(lines[0]) - 1)
gamma = 0
epsilon = 0

# track number of 0s and 1s in each column
for line in lines:
    line = line.strip("\n")
    for i, num in enumerate(line):
        if int(line[i]) == 1:
            tracker[i] += 1
        else:
            tracker[i] -= 1

print(tracker) 

# convert numbers to binary 
# negative numbers in the tracker indicate a 1 for epsilon in that spot 
# positive numbers indicate a 1 for gamma in that spot 
for i, num in enumerate(tracker):
    power = pow(2, len(tracker)-i-1)
    if num > 0:
        gamma += power
    elif num < 0:
        epsilon += power

# print relevant data      
print(gamma)
print(epsilon)
print(gamma*epsilon)

# first try: the test input didn't work because I tracked the numbers wrong
# second try: 6698 * 1492 = 9993416 (too high) - made array initialize to wrong size
# third try: 3349 * 746 = 2498354 - correct