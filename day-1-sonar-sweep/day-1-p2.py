# open file and read input
input = open("input.txt")
lines = input.readlines()
lines = [int(x.strip("\n")) for x in lines]

# create a way to track increases and decreases
increases = 0
same = 0
decreases = 0
previous = lines[0] + lines[1] + lines[2]

# parse through the input but take the current line + the next 2 lines
for i in range(1, len(lines) - 2):
    # strip the line of the newline and convert to an int
    current = lines[i] + lines[i + 1] + lines[i + 2]

    # compare to previous 
    if current > previous:
        increases += 1
        print(previous, current, "increases")
    elif current < previous:
        decreases += 1
        print(previous, current, "decreases")
    else:
        same += 1

    # update previous
    previous = current

print(increases)
assert(increases+decreases+same+1 == len(lines)-2)

# first answer: 1486 - correct