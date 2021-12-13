input = open("input.txt")
fish = [int(x) for x in input.read().split(",")]

def findFish(fish, days):
    for day in range(days):
        nextFish = []
        newFishToAdd = []
        for fishy in fish:
            if fishy == 0:
                nextFish.append(6)
                newFishToAdd.append(8)
            elif fishy > 0:
                nextFish.append(fishy - 1)
        fish = nextFish + newFishToAdd
    return len(fish)

print(findFish(fish, 80))

# first attempt: 365131 - correct
# this was surprisingly easy for how many words were in the question description and how intimidated i was at first