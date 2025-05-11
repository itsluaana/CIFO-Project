from lib.genetic_algorithm import genetic_algorithm
from lib.crossover import pmx_crossover, order_crossover
from lib.mutation import swap_mutation, inversion_mutation, insertion_mutation, prime_slot_mutation, slot_shuffle_mutation
from lib.fitness import fitness



class Solution:
    def __init__(self, representation, artists=None, conflict_matrix=None, 
                 crossover_method='pmx', mutation_method='swap'):
        self.representation = representation
        self.artists = artists
        self.conflict_matrix = conflict_matrix
        self.crossover_method = crossover_method
        self.mutation_method = mutation_method
        self._fitness = None

    def fitness(self):
        if self._fitness is None:
            self._fitness = fitness(self.representation, self.artists, self.conflict_matrix)
        return self._fitness

    def crossover(self, other, method=None):
        method = method or self.crossover_method
        if method == 'pmx':
            child1_repr, child2_repr = pmx_crossover(self.representation, other.representation)
        elif method == 'ox':
            child1_repr, child2_repr = order_crossover(self.representation, other.representation)
        else:
            raise ValueError("Unknown crossover method")
        return (
            Solution(child1_repr, self.artists, self.conflict_matrix, method, self.mutation_method),
            Solution(child2_repr, self.artists, self.conflict_matrix, method, self.mutation_method)
        )

    def mutation(self, mut_prob=0.1, method=None):
        import random
        method = method or self.mutation_method
        if random.random() > mut_prob:
            return Solution(self.representation.copy(), self.artists, self.conflict_matrix,
                            self.crossover_method, self.mutation_method)
        if method == 'swap':
            mutant = swap_mutation(self.representation)
        elif method == 'inversion':
            mutant = inversion_mutation(self.representation)
        elif method == 'insertion':
            mutant = insertion_mutation(self.representation)
        elif method == 'prime':
            mutant = prime_slot_mutation(self.representation.copy(), 5, 7)
        elif method == 'shuffle':
            mutant = slot_shuffle_mutation(self.representation.copy(), 5, 7)
        else:
            raise ValueError("Unknown mutation method")
        return Solution(mutant, self.artists, self.conflict_matrix,
                        self.crossover_method, self.mutation_method)

    def __repr__(self):
        return str(self.representation)


