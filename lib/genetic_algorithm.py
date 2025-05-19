from typing import Callable
from copy import deepcopy
import random

# Function to retrieve the best individual from the population based on fitness
def get_best_ind(population: list, maximization: bool):
    # Compute the fitness for each individual in the population
    fitness_list = [ind.fitness() for ind in population]
    
    # If maximization is True, return the individual with the maximum fitness, else the minimum
    if maximization:
        return population[fitness_list.index(max(fitness_list))]
    else:
        return population[fitness_list.index(min(fitness_list))]

def genetic_algorithm(
    initial_population: list,  # Initial population of individuals
    max_gen: int,               # Maximum number of generations to run the algorithm
    selection_algorithm: Callable,  # Selection algorithm for choosing parents
    maximization: bool = True,  # Whether we are maximizing or minimizing the fitness function
    xo_prob: float = 0.9,       # Probability of applying crossover
    mut_prob: float = 0.1,      # Probability of applying mutation
    elitism: bool = True,       # Whether to use elitism (preserving the best individual)
    verbose: bool = False,      # Whether to print detailed logs of each generation
    track_history: bool = False, # Whether to track the best fitness in each generation
    **sel_params                # Unpack the selection method's parameters (like k or pressure)
):
    population = initial_population  # Initialize population
    best_fitness_over_time = []      # List to store the best fitness of each generation

    # Loop through the generations
    for gen in range(1, max_gen + 1):
        if verbose:
            print(f'-------------- Generation: {gen} --------------')

        new_population = []  # Create a new population for this generation

        # If elitism is enabled, carry over the best individual to the new population
        if elitism:
            new_population.append(deepcopy(get_best_ind(population, maximization)))

        # Fill the new population by selecting parents, performing crossover, and mutation
        while len(new_population) < len(population):
            # Select two individuals from the population using the selection algorithm
            first_ind = selection_algorithm(population, maximization, **sel_params)
            second_ind = selection_algorithm(population, maximization, **sel_params)

            if verbose:
                print(f'Selected individuals:\n{first_ind}\n{second_ind}')

            # Apply crossover with probability 'xo_prob'
            if random.random() < xo_prob:
                offspring1, offspring2 = first_ind.crossover(second_ind)
                if verbose:
                    print(f'Applied crossover')
            else:
                # If no crossover, replicate the individuals
                offspring1, offspring2 = deepcopy(first_ind), deepcopy(second_ind)
                if verbose:
                    print(f'Applied replication')

            if verbose:
                print(f'Offspring:\n{offspring1}\n{offspring2}')

            # Apply mutation to the first offspring
            first_new_ind = offspring1.mutation(mut_prob)
            new_population.append(first_new_ind)

            if verbose:
                print(f'First mutated individual: {first_new_ind}')

            # Apply mutation to the second offspring if needed
            if len(new_population) < len(population):
                second_new_ind = offspring2.mutation(mut_prob)
                new_population.append(second_new_ind)
                if verbose:
                    print(f'Second mutated individual: {second_new_ind}')

        # Update the population for the next generation
        population = new_population

        # Track the best fitness value if requested
        if track_history:
            best_individual = get_best_ind(population, maximization)
            best_fitness_over_time.append(best_individual.fitness())

        # Verbose output for the best individual in the current generation
        if verbose:
            print(f'Final best individual in generation: {get_best_ind(population, maximization)}')

    # Store best individual
    best_individual = get_best_ind(population, maximization)

    # Return both best solution and fitness history (or empty list if not tracked)
    return best_individual, (best_fitness_over_time if track_history else [])

    


