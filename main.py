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


def mutate(populationItems):
    randIndex = random.randint(0, (len(populationItems) - 1))
    print("Parent " + str(randIndex + 1) + " was chosen for mutation")
    res = changeRandomGene(populationItems, randIndex)
    while isFeasible(res[randIndex]) == 1:
        res = changeRandomGene(populationItems, randIndex)
    return res


def pickTwoParents(parents):
    differentParents = []
    noOfParents = len(parents)
    p1 = p2 = 0
    while p1 == p2:
        p1 = random.randint(0, (noOfParents - 1))
        p2 = random.randint(0, (noOfParents - 1))
    differentParents.append(p1)
    differentParents.append(p2)
    return differentParents


def crossover(parents):
    point = random.randint(1, (len(parents[0]) - 1))
    parentLength = len(parents[0])
    p1 = p2 = 0
    child = []

    while isFeasible(child) == 1:
        child = []
        parentsToCrossover = pickTwoParents(parents)
        p1 = parents[parentsToCrossover[0]]
        p2 = parents[parentsToCrossover[1]]

        for i in range(0, parentLength):
            if i < point:
                child.append(p1[i])
            else:
                child.append(p2[i])

    print("Parent " + str(p1) + " and parent " + str(p2) + " were chosen for crossover at point " + str(point))
    parents.append(child)


if __name__ == "__main__":
    population = [
        [1, 2, 3, 1, 2],
        [2, 4, 3, 2, 3],
        [5, 1, 2, 1, 1],
        [3, 1, 1, 4, 2]
    ]
    print("Initial population:")
    print(population)
    print("\nPopulation after mutation:")
    population = mutate(population)
    print(population)
    print("\nPopulation after crossover:")
    crossover(population)
    print(population)
