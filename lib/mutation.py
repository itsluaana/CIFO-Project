import random

def swap_mutation(individual):
    mutant = individual.copy()
    i, j = random.sample(range(len(mutant)), 2)
    mutant[i], mutant[j] = mutant[j], mutant[i]
    return mutant

def inversion_mutation(individual):
    mutant = individual.copy()
    i, j = sorted(random.sample(range(len(mutant)), 2))
    mutant[i:j+1] = reversed(mutant[i:j+1])
    return mutant

def insertion_mutation(individual):
    mutant = individual.copy()
    i, j = random.sample(range(len(mutant)), 2)
    gene = mutant.pop(i)
    mutant.insert(j, gene)
    return mutant
