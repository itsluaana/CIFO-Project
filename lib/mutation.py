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

def prime_slot_mutation(representation, num_stages, num_slots):
    prime_indices = [stage * num_slots + (num_slots - 1) for stage in range(num_stages)]
    non_prime_indices = [i for i in range(len(representation)) if i not in prime_indices]

    prime_idx = random.choice(prime_indices)
    non_prime_idx = random.choice(non_prime_indices)

    representation[prime_idx], representation[non_prime_idx] = (
        representation[non_prime_idx],
        representation[prime_idx]
    )
    return representation


def slot_shuffle_mutation(representation, num_stages, num_slots):
    slot = random.randint(0, num_slots - 1)
    indices = [stage * num_slots + slot for stage in range(num_stages)]
    values = [representation[i] for i in indices]

    random.shuffle(values)

    new_repr = representation.copy()
    for i, idx in enumerate(indices):
        new_repr[idx] = values[i]
    return new_repr



