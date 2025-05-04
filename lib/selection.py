import random
from copy import deepcopy

def tournament_selection(population: list, tournament_size: int, maximization: bool = True):
    """
    Selects a single individual from the population using tournament selection.
    
    Args:
        population (list): List of Solution objects.
        tournament_size (int): Number of individuals in the tournament.
        maximization (bool): True if higher fitness is better, False for minimization.
        
    Returns:
        Solution: A deepcopy of the selected individual.
    """
    # Randomly sample tournament_size individuals
    tournament = random.sample(population, tournament_size)
    
    # Select winner based on maximization or minimization
    if maximization:
        winner = max(tournament, key=lambda ind: ind.fitness())
    else:
        winner = min(tournament, key=lambda ind: ind.fitness())
        
    return deepcopy(winner)
