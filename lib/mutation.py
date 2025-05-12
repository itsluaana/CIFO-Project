import random

# Swap Mutation: This mutation swaps two randomly selected genes in the individual.
# It creates a new individual where two genes are exchanged.
def swap_mutation(individual):
    mutant = individual.copy()  # Create a copy of the individual to avoid modifying the original.
    i, j = random.sample(range(len(mutant)), 2)  # Randomly select two distinct indices.
    mutant[i], mutant[j] = mutant[j], mutant[i]  # Swap the genes at these indices.
    return mutant  # Return the mutated individual.


# Inversion Mutation: This mutation selects a subsequence of genes and reverses it.
# It creates a new individual with the selected segment inverted.
def inversion_mutation(individual):
    mutant = individual.copy()  # Create a copy of the individual to avoid modifying the original.
    i, j = sorted(random.sample(range(len(mutant)), 2))  # Randomly select two distinct indices and sort them to get the slice boundaries.
    mutant[i:j+1] = reversed(mutant[i:j+1])  # Reverse the subsequence from index i to j.
    return mutant  # Return the mutated individual.


# Insertion Mutation: This mutation removes one gene from a randomly chosen position and inserts it at another randomly chosen position.
# It creates a new individual where one gene is relocated within the individual.
def insertion_mutation(individual):
    mutant = individual.copy()  # Create a copy of the individual to avoid modifying the original.
    i, j = random.sample(range(len(mutant)), 2)  # Randomly select two distinct indices.
    gene = mutant.pop(i)  # Remove the gene at index i.
    mutant.insert(j, gene)  # Insert the gene at index j.
    return mutant  # Return the mutated individual.


# Prime Slot Mutation: This mutation swaps an artist between a prime slot (last slot of each stage)
# and a non-prime slot (any slot that is not the last one) in the given individual representation.
def prime_slot_mutation(representation, num_stages, num_slots):
    prime_indices = [stage * num_slots + (num_slots - 1) for stage in range(num_stages)]  # Get indices of all prime slots (last slot of each stage).
    non_prime_indices = [i for i in range(len(representation)) if i not in prime_indices]  # Get all non-prime slot indices.

    prime_idx = random.choice(prime_indices)  # Randomly select a prime slot index.
    non_prime_idx = random.choice(non_prime_indices)  # Randomly select a non-prime slot index.

    # Swap the artists assigned to the selected prime slot and non-prime slot.
    representation[prime_idx], representation[non_prime_idx] = (
        representation[non_prime_idx],
        representation[prime_idx]
    )
    return representation  # Return the mutated representation.


# Slot Shuffle Mutation: This mutation randomly selects a slot (across all stages),
# and shuffles the artists assigned to that slot (randomly permutes the list of artists).
def slot_shuffle_mutation(representation, num_stages, num_slots):
    slot = random.randint(0, num_slots - 1)  # Randomly choose a slot.
    indices = [stage * num_slots + slot for stage in range(num_stages)]  # Get the indices for the chosen slot across all stages.
    values = [representation[i] for i in indices]  # Extract the artists assigned to the selected slot across stages.

    random.shuffle(values)  # Shuffle the list of artists in the selected slot.

    new_repr = representation.copy()  # Create a copy of the individual representation to avoid modifying the original.
    for i, idx in enumerate(indices):  # Assign the shuffled artists back to their respective slots.
        new_repr[idx] = values[i]

    return new_repr  # Return the mutated representation.




