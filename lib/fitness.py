import numpy as np

# Constants representing the layout
NUM_STAGES = 5        # Number of stages at the festival
NUM_SLOTS = 7         # Number of time slots per stage

# Helper function to get an Artist object by ID from the list of Artist objects
def get_artist_by_id(artist_id, artists):
    return next(a for a in artists if a.id == artist_id)

# Calculate the total normalized popularity of artists in the prime slots
def compute_prime_slot_popularity(solution, artists):
    # Prime slots are the last slot on each stage
    prime_indices = [stage * NUM_SLOTS + (NUM_SLOTS - 1) for stage in range(NUM_STAGES)]
    # Sum the normalized popularity of the artists in those slots
    return sum(get_artist_by_id(solution[i], artists).popularity_norm for i in prime_indices)

# Measure genre diversity across slots
def compute_genre_diversity(solution, artists):
    total_normalized_diversity = 0
    # For each time slot (across all stages)
    for slot in range(NUM_SLOTS):
        genres = set()
        for stage in range(NUM_STAGES):
            idx = stage * NUM_SLOTS + slot
            # Add the genre code of the artist at that stage/slot
            genres.add(get_artist_by_id(solution[idx], artists).genre_code)
        # Normalize by the possible max of unique genres by slot
        max_possible = min(len(set(a.genre_code for a in artists)), NUM_STAGES)
        total_normalized_diversity += len(genres) / max_possible
    # Average normalized diversity by slot
    return total_normalized_diversity / NUM_SLOTS

# Compute the conflict penalty using the conflict matrix
def compute_conflict_penalty(solution, conflict_matrix):
    total_conflict = 0
    # For each time slot, collect all artists across all stages
    for slot in range(NUM_SLOTS):
        slot_artist_indices = [stage * NUM_SLOTS + slot for stage in range(NUM_STAGES)]
        slot_artist_ids = [solution[i] for i in slot_artist_indices]
        # For each unique pair of artists in the same slot but different stages
        for i in range(NUM_STAGES):
            for j in range(i + 1, NUM_STAGES):
                total_conflict += conflict_matrix[slot_artist_ids[i], slot_artist_ids[j]]
    # Average the conflict over all slots
    return total_conflict / NUM_SLOTS

# Fitness function that combines popularity, genre diversity, and conflict
def fitness(solution, artists, conflict_matrix):
    # Step 1: Max possible popularity in prime slots (top artist per stage)
    top5 = sorted(artists, key=lambda a: a.popularity_norm, reverse=True)[:NUM_STAGES]
    max_prime_popularity = sum(a.popularity_norm for a in top5)

    # Step 2: Max possible genre diversity (up to one unique genre per stage)
    all_genres = set(a.genre for a in artists)
    max_genre_diversity = min(len(all_genres), NUM_STAGES)

    # Step 3: Worst-case conflict (all pairs conflicting, max penalty = 1)
    max_conflict = (NUM_STAGES * (NUM_STAGES - 1) / 2) * NUM_SLOTS * 1.0

    # Step 4: Compute normalized values for the current solution
    norm_prime_pop = compute_prime_slot_popularity(solution, artists) / max_prime_popularity
    norm_genre_div = compute_genre_diversity(solution, artists) / max_genre_diversity
    norm_conflict = compute_conflict_penalty(solution, conflict_matrix) / max_conflict

    # Step 5: Combine the three components into a final fitness score
    # We want to maximize popularity and genre diversity, and minimize conflict
    fitness_score = (norm_prime_pop + norm_genre_div + (1 - norm_conflict)) / 3
    return fitness_score


