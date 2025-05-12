from lib.genetic_algorithm import genetic_algorithm
from lib.crossover import pmx_crossover, order_crossover
from lib.mutation import swap_mutation, inversion_mutation, insertion_mutation, prime_slot_mutation, slot_shuffle_mutation
from lib.fitness import fitness

class Solution:
    def __init__(self, representation, artists=None, conflict_matrix=None, 
                 crossover_method='pmx', mutation_method='swap'):
        # - `representation`: the specific arrangement of artists in stages and slots.
        # - `artists`: a list of artist objects.
        # - `conflict_matrix`: a matrix containing conflict scores between pairs of artists.
        # - `crossover_method`: the method used for crossover in genetic algorithm.
        # - `mutation_method`: the mutation technique to apply.
        # - `_fitness`: a cache to store the fitness value of the solution.
        self.representation = representation
        self.artists = artists
        self.conflict_matrix = conflict_matrix
        self.crossover_method = crossover_method
        self.mutation_method = mutation_method
        self._fitness = None

    def fitness(self):
        # This method computes and returns the fitness value of the solution.
        # It caches the value the first time it is computed to avoid recalculating it repeatedly.
        if self._fitness is None:
            self._fitness = fitness(self.representation, self.artists, self.conflict_matrix)
        return self._fitness

    def crossover(self, other, method=None):
        # This method handles crossover between the current solution and another solution.
        # - `method`: The crossover method to use.
        # Returns two child solutions that result from the crossover operation.
        method = method or self.crossover_method  # If no method is passed, use the one set in the constructor.
        if method == 'pmx':
            child1_repr, child2_repr = pmx_crossover(self.representation, other.representation)
        elif method == 'ox':
            child1_repr, child2_repr = order_crossover(self.representation, other.representation)
        else:
            raise ValueError("Unknown crossover method")  # Raise an error if an invalid method is provided.
        return (
            Solution(child1_repr, self.artists, self.conflict_matrix, method, self.mutation_method),
            Solution(child2_repr, self.artists, self.conflict_matrix, method, self.mutation_method)
        )

    def mutation(self, mut_prob=0.1, method=None):
        # This method applies mutation to the solution.
        # - `mut_prob`: Probability of mutation happening.
        # - `method`: The mutation method to apply.
        # If a random number exceeds `mut_prob`, no mutation occurs, and a copy of the current solution is returned.
        import random
        method = method or self.mutation_method  # If no method is passed, use the one set in the constructor.
        if random.random() > mut_prob:  # If mutation is not applied (based on mut_prob), return a copy of the current solution.
            return Solution(self.representation.copy(), self.artists, self.conflict_matrix,
                            self.crossover_method, self.mutation_method)
        
        # Depending on the mutation method chosen, apply the corresponding mutation technique.
        if method == 'swap':
            mutant = swap_mutation(self.representation)
        elif method == 'inversion':
            mutant = inversion_mutation(self.representation)
        elif method == 'insertion':
            mutant = insertion_mutation(self.representation)
        elif method == 'prime':
            mutant = prime_slot_mutation(self.representation.copy(), 5, 7)  # 5 stages and 7 slots
        elif method == 'shuffle':
            mutant = slot_shuffle_mutation(self.representation.copy(), 5, 7)  # 5 stages and 7 slots
        else:
            raise ValueError("Unknown mutation method")  # Raise an error if an invalid method is provided.
        
        # Return the mutated solution.
        return Solution(mutant, self.artists, self.conflict_matrix,
                        self.crossover_method, self.mutation_method)

    def __repr__(self):
        # Return a string representation of the solution.
        return str(self.representation)


