def isFeasible(solution):
    itemWeight = {
        1: 30,
        2: 25,
        3: 10,
        4: 20,
        5: 5
    }
    if len(solution) != 5:
        return 1
    else:
        b1 = b2 = b3 = b4 = b5 = 0
        for i in range(0, 5):
            if solution[i] == 1:
                b1 = b1 + itemWeight[i + 1]
            if solution[i] == 2:
                b2 = b2 + itemWeight[i + 1]
            if solution[i] == 3:
                b3 = b3 + itemWeight[i + 1]
            if solution[i] == 4:
                b4 = b4 + itemWeight[i + 1]
            if solution[i] == 5:
                b5 = b5 + itemWeight[i + 1]
        if b1 <= 50 and b2 <= 50 and b3 <= 50 and b4 <= 50 and b5 <= 50:
            return 0
        else:
            return 1


def generatePopulation(items, bins, pop_size):
    popList = []
    for i in range(0, pop_size):
        popList.append()


def mutate():
    pass


def crossover():
    pass


if __name__ == "__main__":
    s = [1, 2, 3, 1, 2]
    print(isFeasible(s))
