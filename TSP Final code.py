import numpy as np
import operator
import pandas as pd
import random

#from create_initial_population import createFirstPopulation
from fitness import Fitnes




def rankRoutes(population):
    # dictionary
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


# .items() returns an object's dictionary's (element/info); in this case, a whole dictionary object
# ORDERING THE LIST-LIKE OBJECT BY ROUTE LENGTH

def selection(populationRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(populationRanked), columns=["Index", "Fitness"])
    #followinggeneration.  # data frame => df.
    #providesalistofthematingPoolfunction's IDs.
    # declaring lists as new columns
    
    df['cumulative_sum'] = df.Fitness.cumsum()
    df['cumulative_percentage'] = 10 * df.cumulative_sum / df.Fitness.sum()

    # add elite to selectionResults
    for i in range(0, eliteSize):
        selectionResults.append(populationRanked[i][0])

    # add
    # DataFrame.iat -> Access a single value for a row/column pair by integer position.
    for i in range(0, len(populationRanked) - eliteSize):
        # 0 < number < 100
        pick = 100 * random.random()
        for i in range(0, len(populationRanked)):
            if pick < df.iat[i, 5]:
                selectionResults.append(populationRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    mating_pool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        mating_pool.append(population[index])
    return mating_pool

def breed(parent1, parent2):
    # "Ordered crossover" - successive alleles from parent 1 are dropped, and the remaining values are assigned to the child.
    childPart1 = [0]
    # position of city in list
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childPart1.append(parent1[i])

    childPart2 = [item for item in parent2 if item not in childPart1]

    child = childPart1 + childPart2
    return child

def breedPopulation(mating_pool, eliteSize):
    children = []
    leftLength = len(mating_pool) - eliteSize
    pool = random.sample(mating_pool, len(mating_pool))
    for i in range(0, eliteSize):
        children.append(mating_pool[i])

    # pool - reorganized matingpool

    for i in range(0, leftLength):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
        children.append(child)
    return children

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if random.random() < mutationRate:
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual

# mutates every individual in population and adds to list
def mutatePopulation(population, mutationRate):
    mutatedPopulation = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPopulation.append(mutatedInd)

    return mutatedPopulation


def nextGeneration(currentGene, eliteSize, mutationRate):
    pass

def geneticAlgorithm(population, populationSize, eliteSize, mutationRate, generations):
    pop = createFirstPopulation(populationSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][1]
    bestRoute = pop[bestRouteIndex]
    print("Route: " + str(bestRoute))
    return bestRoute