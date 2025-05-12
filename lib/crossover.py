import random

# Order Crossover (OX) implementation
def order_crossover(parent1, parent2):
    size = len(parent1)
    # Randomly select two crossover points
    a, b = sorted(random.sample(range(size), 2))

    # Initialize children with None values
    child1 = [None] * size
    child2 = [None] * size

    # Copy a slice from each parent into the corresponding child
    child1[a:b] = parent1[a:b]
    child2[a:b] = parent2[a:b]

    # Helper function to fill the remaining genes preserving order and without duplicates
    def fill_child(child, parent):
        pos = b  # Start filling after the second cut point
        for i in range(size):
            idx = (b + i) % size  # Wrap around the list
            gene = parent[idx]
            if gene not in child:
                child[pos % size] = gene
                pos += 1

    fill_child(child1, parent2)
    fill_child(child2, parent1)

    return child1, child2

# Partially Matched Crossover (PMX) implementation
def pmx_crossover(parent1, parent2):
    size = len(parent1)
    # Randomly select two crossover points
    a, b = sorted(random.sample(range(size), 2))

    # Initialize children with None values
    child1 = [None] * size
    child2 = [None] * size

    # Copy a slice from each parent into the corresponding child
    child1[a:b] = parent1[a:b]
    child2[a:b] = parent2[a:b]

    # Helper function to fill the rest of the child based on PMX rules
    def pmx_fill(child, parent, a, b):
        for i in range(a, b):
            gene = parent[i]
            # If the gene is not already in the child, resolve conflict using mapping
            if gene not in child:
                pos = i
                while True:
                    gene_in_child = child[pos]
                    pos = parent.index(gene_in_child)
                    if child[pos] is None:
                        child[pos] = gene
                        break

        # Fill any remaining None positions directly from the parent
        for i in range(size):
            if child[i] is None:
                child[i] = parent[i]

    pmx_fill(child1, parent2, a, b)
    pmx_fill(child2, parent1, a, b)

    return child1, child2
