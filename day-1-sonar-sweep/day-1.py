# open file and read input
input = open("input.txt")
lines = input.readlines()

# create a way to track increases and decreases
increases = 0
same = 0
decreases = 0
previous = int(lines[0].strip("\n"))

# parse through each entry
for line in lines[1:]:
    # strip the line of the newline and convert to an int
    print(line)
    line = int(line.strip("\n"))

    # compare to previous 
    if line > previous:
        increases += 1
        print(previous, line, "increases")
    elif line < previous:
        decreases += 1
        print(previous, line, "decreases")
    else:
        same += 1

    # update previous
    previous = line   

print(increases)
assert(increases+decreases+same+1 == len(lines))

# first try: 1445 (too low) - issue was that I was not converting the inputs into integers
    # strings were being compared so 1 string (ex. 9 to 10) would be logged as a decrease instead of an increase
# second try: 1446 