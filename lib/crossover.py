import random

def order_crossover(parent1, parent2):
    size = len(parent1)
    # Choose two random cut points
    a, b = sorted(random.sample(range(size), 2))
    # Initialize children with None
    child1 = [None] * size
    child2 = [None] * size

    # Copy the slice from parents to children
    child1[a:b] = parent1[a:b]
    child2[a:b] = parent2[a:b]

    def fill_child(child, parent):
        pos = b
        for i in range(size):
            idx = (b + i) % size
            gene = parent[idx]
            if gene not in child:
                child[pos % size] = gene
                pos += 1

    fill_child(child1, parent2)
    fill_child(child2, parent1)

    return child1, child2

def pmx_crossover(parent1, parent2):
    size = len(parent1)
    # Choose two random cut points
    a, b = sorted(random.sample(range(size), 2))
    # Initialize children
    child1 = [None] * size
    child2 = [None] * size

    # Copy the slice from parents to children
    child1[a:b] = parent1[a:b]
    child2[a:b] = parent2[a:b]

    def pmx_fill(child, parent, a, b):
        for i in range(a, b):
            gene = parent[i]
            if gene not in child:
                pos = i
                while True:
                    gene_in_child = child[pos]
                    pos = parent.index(gene_in_child)
                    if child[pos] is None:
                        child[pos] = gene
                        break

        # Fill in remaining positions
        for i in range(size):
            if child[i] is None:
                child[i] = parent[i]

    pmx_fill(child1, parent2, a, b)
    pmx_fill(child2, parent1, a, b)

    return child1, child2
