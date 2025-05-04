import random
from copy import deepcopy



def tournament_selection(population, maximization, k=3):
    # Randomly select k individuals
    tournament = random.sample(population, k)
    # Choose the best (max or min) in the tournament
    if maximization:
        return max(tournament, key=lambda ind: ind.fitness())
    else:
        return min(tournament, key=lambda ind: ind.fitness())
    

def ranking_selection(population, maximization):
    # Sort individuals by fitness
    sorted_pop = sorted(population, key=lambda ind: ind.fitness(), reverse=maximization)
    n = len(sorted_pop)
    # Assign probabilities: rank 1 gets highest probability
    probs = [2*(i+1)/(n*(n+1)) for i in range(n)]  # Linear ranking
    # Select one individual based on these probabilities
    selected = random.choices(sorted_pop, weights=probs, k=1)[0]
    return selected



