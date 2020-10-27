import copy
import random


def isFeasible(solution):
    itemWeight = {
        1: 30,
        2: 25,
        3: 10,
        4: 20,
        5: 5
    }
    isFeasibleSolution = 0

    if len(solution) != 5:
        isFeasibleSolution = 1
    else:
        bins = [0, 0, 0, 0, 0]
        for i in range(0, 5):
            bins[solution[i] - 1] = bins[solution[i] - 1] + itemWeight[i + 1]

        for binWeight in bins:
            if binWeight > 50:
                isFeasibleSolution = 1
                break
    return isFeasibleSolution


def mutate(populationItems):
    randIndex = random.randint(0, (len(populationItems) - 1))
    print("Item mutated: " + str(randIndex+1))

    res = changeRandomGene(populationItems, randIndex)
    while isFeasible(res[randIndex]) == 1:
        res = changeRandomGene(populationItems, randIndex)

    return res


def changeRandomGene(allItems, randIndex):
    items = copy.deepcopy(allItems)
    randItem = items[randIndex]
    randGene = random.randint(0, (len(items) - 1))
    oldGeneValue = randItem[randGene]
    newGeneValue = random.randint(1, 5)
    while newGeneValue == oldGeneValue:
        newGeneValue = random.randint(1, 5)
    randItem[randGene] = newGeneValue
    return items


def crossover():
    pass


if __name__ == "__main__":
    population = [
        [1, 2, 3, 1, 2],
        [2, 1, 3, 2, 3],
        [2, 1, 2, 1, 1],
        [3, 1, 1, 4, 2]
    ]
    print(population)
    print("\nPopulation after mutation:")
    result = mutate(population)
    print(result)
