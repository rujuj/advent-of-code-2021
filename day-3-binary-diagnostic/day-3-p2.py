import copy 

def bin_to_dec(enumerated_num, length):
    decimal = 0
    for i, num in enumerated_num:
        power = pow(2, length - i - 1)
        if int(num) > 0:
            decimal += power
    return decimal 

# open file and read input
input = open("input.txt")
lines = input.readlines()

# initialize variables
oxygentracker = ""
co2tracker = ""
round = 0
print(len(lines))

# loop through all lines and track which prefixes are valid
while len(oxygentracker) != len(lines[0].strip("\n")):
    oxygenones = 0
    oxygenzeroes = 0
    co2ones = 0
    co2zeroes = 0

    for line in lines:
        line = line.strip("\n")

        # either match the tracker to the line's prefix or make sure it's the first cycle 
        if oxygentracker == line[:len(oxygentracker)] or len(oxygentracker) == 0:

            # track the number of ones 
            if line[len(oxygentracker)] == "1":
                oxygenones += 1
            else:
                oxygenzeroes += 1

        if co2tracker == line[:len(co2tracker)] or len(co2tracker) == 0:
            if line[len(co2tracker)] == "1":
                co2ones += 1
            else:
                co2zeroes += 1

    # append the appropriate bit to keep track of the appropriate prefixes             
    if oxygenones >= oxygenzeroes:
        oxygentracker = oxygentracker + "1"
    else:
        oxygentracker = oxygentracker + "0"
    if co2zeroes <= co2ones and (co2zeroes + co2ones > 1):
        co2tracker = co2tracker + "0"
    elif co2zeroes > co2ones and (co2zeroes + co2ones > 1):
        co2tracker = co2tracker + "1"
    else:
        # i know this is terrible but i cannot just scrap all of this, i may rewrite later
        if co2zeroes > co2ones:
            co2tracker = co2tracker + "0"
        else:
            co2tracker = co2tracker + "1"
    
    # reset the ones to 0
    oxygenones = 0
    oxygenzeroes = 0
    co2ones = 0
    co2zeroes = 0
    round += 1

print(oxygentracker)
print(co2tracker)

oxygen = bin_to_dec(enumerate(oxygentracker), len(oxygentracker))
co2 = bin_to_dec(enumerate(co2tracker), len(co2tracker))

# print relevant data      
print(oxygen)
print(co2)
print(oxygen*co2)

# had to rethink this solution a few times and eventually re-wrote the whole thing
# forgot that i couldn't compare the ones in the column to how many total lines there were each time
    # since i wasn't actually updating the lines list
# the prefix check was actually written wrong :)

# first attempt: 5128 * 1695 = 8691960 (too high but at least the numbers looked somewhat reasonable?)
# second attempt: 2564 * 847 = 2171708 (too low)
    # am now realizing the sample input didn't work either and i should have tried that out first;
    # also realized there was 1 key statement that i ignored: after there is only 1 more line left
    # in the list, i need to terminate - and with my current system of just going through the whole 
    # list repeatedly, i actually cannot do that :( ;
    # figured out a hacky way to do it but it's upsetting so i think i will have to re-code this
    # some time to actually reflect the fact that i have to use some kind of list and remove elements
    # from it 
# third attempt: 3921 * 836 * 3277956 - correct