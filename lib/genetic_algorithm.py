# lib/genetic_algorithm.py
from typing import Callable
from copy import deepcopy
import random

def get_best_ind(population: list, maximization: bool):
    fitness_list = [ind.fitness() for ind in population]
    if maximization:
        return population[fitness_list.index(max(fitness_list))]
    else:
        return population[fitness_list.index(min(fitness_list))]

def genetic_algorithm(
    initial_population: list,
    max_gen: int,
    selection_algorithm: Callable,
    maximization: bool = False,
    xo_prob: float = 0.9,
    mut_prob: float = 0.1,
    elitism: bool = True,
    verbose: bool = False,
    track_history: bool = False  
):
    population = initial_population
    best_fitness_over_time = []  # List to store the best fitness in each generation

    for gen in range(1, max_gen + 1):
        if verbose:
            print(f'-------------- Generation: {gen} --------------')

        new_population = []

        if elitism:
            new_population.append(deepcopy(get_best_ind(population, maximization)))

        while len(new_population) < len(population):
            first_ind = selection_algorithm(population, maximization)
            second_ind = selection_algorithm(population, maximization)

            if verbose:
                print(f'Selected individuals:\n{first_ind}\n{second_ind}')

            if random.random() < xo_prob:
                offspring1, offspring2 = first_ind.crossover(second_ind)
                if verbose:
                    print(f'Applied crossover')
            else:
                offspring1, offspring2 = deepcopy(first_ind), deepcopy(second_ind)
                if verbose:
                    print(f'Applied replication')

            if verbose:
                print(f'Offspring:\n{offspring1}\n{offspring2}')

            first_new_ind = offspring1.mutation(mut_prob)
            new_population.append(first_new_ind)

            if verbose:
                print(f'First mutated individual: {first_new_ind}')

            if len(new_population) < len(population):
                second_new_ind = offspring2.mutation(mut_prob)
                new_population.append(second_new_ind)
                if verbose:
                    print(f'Second mutated individual: {second_new_ind}')

        population = new_population

        # Track best fitness per generation
        if track_history:
            best_individual = get_best_ind(population, maximization)
            best_fitness_over_time.append(best_individual.fitness())

        if verbose:
            print(f'Final best individual in generation: {get_best_ind(population, maximization)}')

    # Return the best individual and the fitness history if requested
    if track_history:
        return get_best_ind(population, maximization), best_fitness_over_time
    else:
        return get_best_ind(population, maximization)


