input = open("input.txt")
fish = [int(x) for x in input.read().split(",")]
fishPerDay = [0] * 9

# store each fish in the day that it belongs in
for fishy in fish:
    fishPerDay[fishy] += 1

def findFish(fish, days):
    for day in range(days):
        newFishPerDay = [0] * 9
        for i, fishy in enumerate(fish):
            if i == 0:
                newFishPerDay[6] += fishy
                newFishPerDay[8] += fishy
            elif i > 0:
                newFishPerDay[i - 1] += fishy
        fish = newFishPerDay
    return newFishPerDay

def totalFish(fish):
    totalFishy = 0
    for fishy in fish:
        totalFishy += fishy
    return totalFishy

print(totalFish(findFish(fishPerDay, 256)))

# okay using the previous method literally gives a memory error which is fair
# i need to just figure out how many fish to add each day and not store all the fish manually :)

# first attempt: 1650309278600 - correct