import random
from copy import deepcopy

# Tournament Selection: A selection operator where a small subset of individuals
# is randomly chosen, and the best individual from that subset is selected.
def tournament_selection(population, maximization, k=3):
    # Randomly select k individuals from the population
    tournament = random.sample(population, k)
    
    # If maximization is True, return the individual with the highest fitness in the tournament
    if maximization:
        return max(tournament, key=lambda ind: ind.fitness())
    # If maximization is False, return the individual with the lowest fitness in the tournament
    else:
        return min(tournament, key=lambda ind: ind.fitness())
    


# Ranking Selection: This selection method assigns higher selection probabilities
# to individuals with better fitness, but in a ranked manner (using a "pressure" parameter).
def ranking_selection(population, maximization, pressure=1.7):  # `pressure` is a tunable parameter
    # Sort the population by fitness in descending order if maximization is True,
    # otherwise in ascending order (for minimization).
    sorted_pop = sorted(population, key=lambda ind: ind.fitness(), reverse=maximization)
    n = len(sorted_pop)  # Number of individuals in the population

    # Ensure pressure is within the acceptable range
    if pressure < 1.0 or pressure > 2.0:
        raise ValueError("pressure must be between 1.0 and 2.0")

    # Linear ranking probabilities calculation:
    # The probability of selection increases with rank. The pressure controls the extent of this effect.
    probs = [(2 - pressure) / n + (2 * i * (pressure - 1)) / (n * (n - 1)) for i in range(n)]

    # Randomly select an individual based on the calculated probabilities
    selected = random.choices(sorted_pop, weights=probs, k=1)[0]
    
    return selected


#def ranking_selection(population, maximization):
    # Sort individuals by fitness
#    sorted_pop = sorted(population, key=lambda ind: ind.fitness(), reverse=maximization)
#    n = len(sorted_pop)
    # Assign probabilities: rank 1 gets highest probability
#    probs = [2*(i+1)/(n*(n+1)) for i in range(n)]  # Linear ranking
#    # Select one individual based on these probabilities
#    selected = random.choices(sorted_pop, weights=probs, k=1)[0]
#    return selected





