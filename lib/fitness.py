
import numpy as np

NUM_STAGES = 5
NUM_SLOTS = 7

def get_artist_by_id(artist_id, artists):
    return next(a for a in artists if a.id == artist_id)

def compute_prime_slot_popularity(solution, artists):
    # Prime slots: last slot on each stage
    prime_indices = [stage * NUM_SLOTS + (NUM_SLOTS - 1) for stage in range(NUM_STAGES)]
    return sum(get_artist_by_id(solution[i], artists).popularity_norm for i in prime_indices)


def compute_genre_diversity(solution, artists):
    total_unique = 0
    for slot in range(NUM_SLOTS):
        genres = set()
        for stage in range(NUM_STAGES):
            idx = stage * NUM_SLOTS + slot
            genres.add(get_artist_by_id(solution[idx], artists).genre_code)
        total_unique += len(genres)
    return total_unique / NUM_SLOTS


def compute_conflict_penalty(solution, conflict_matrix):
    # For each slot, sum conflicts between all pairs of artists on different stages
    total_conflict = 0
    for slot in range(NUM_SLOTS):
        slot_artist_indices = [stage * NUM_SLOTS + slot for stage in range(NUM_STAGES)]
        slot_artist_ids = [solution[i] for i in slot_artist_indices]
        # Sum pairwise conflicts
        for i in range(NUM_STAGES):
            for j in range(i + 1, NUM_STAGES):
                total_conflict += conflict_matrix[slot_artist_ids[i], slot_artist_ids[j]]
    # Average per slot
    return total_conflict / NUM_SLOTS

def fitness(solution, artists, conflict_matrix):
    # 1. Calculate the maximum possible normalized prime slot popularity
    top5 = sorted(artists, key=lambda a: a.popularity_norm, reverse=True)[:NUM_STAGES]
    max_prime_popularity = sum(a.popularity_norm for a in top5)

    # 2. Calculate the maximum possible genre diversity
    all_genres = set(a.genre for a in artists)
    max_genre_diversity = min(len(all_genres), NUM_STAGES)

    # 3. Calculate the worst possible conflict (for normalization)
    max_conflict = (NUM_STAGES * (NUM_STAGES - 1) / 2) * NUM_SLOTS * 1.0

    # 4. Calculate actual values for the current solution
    norm_prime_pop = compute_prime_slot_popularity(solution, artists) / max_prime_popularity
    norm_genre_div = compute_genre_diversity(solution, artists) / max_genre_diversity
    norm_conflict = compute_conflict_penalty(solution, conflict_matrix) / max_conflict

    # 5. Combine into the final fitness score
    fitness_score = (norm_prime_pop + norm_genre_div + (1 - norm_conflict)) / 3
    return fitness_score

