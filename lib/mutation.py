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

def prime_slot_mutation(individual, num_stages, num_slots):
    prime_indices = [stage * num_slots + (num_slots - 1) for stage in range(num_stages)]
    non_prime_indices = [i for i in range(len(individual.representation)) if i not in prime_indices]

    prime_idx = random.choice(prime_indices)
    non_prime_idx = random.choice(non_prime_indices)

    # Swap prime and non-prime artists
    individual.representation[prime_idx], individual.representation[non_prime_idx] = (
        individual.representation[non_prime_idx],
        individual.representation[prime_idx]
    )
    return individual

def slot_shuffle_mutation(individual, num_stages, num_slots):
    slot = random.randint(0, num_slots - 1)
    indices = [stage * num_slots + slot for stage in range(num_stages)]
    values = [individual.representation[i] for i in indices]
    random.shuffle(values)
    for i, idx in enumerate(indices):
        individual.representation[idx] = values[i]
    return individual


