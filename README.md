<div style="text-align: center; font-family: 'Segoe UI', sans-serif; color: #333; padding: 20px; border-radius: 12px; border: 1px solid #97b83a; background-color: #f9fdf4;">

  <h1 style="color: #97b83a; margin-bottom: 10px;">Computational Intelligence for Optimization <span style="font-weight: 300;">2024–25 | NOVA IMS</span></h1>

  <h3 style="margin-top: 5px; margin-bottom: 20px; font-weight: 500;">Professors: Leonardo Vanneschi | Inês Magessi</h3>

  <h4 style="margin-top: 20px; margin-bottom: 10px; color: #444;">Music Festival Lineup Optimization</h4>

  <h5 style="margin-top: 20px; margin-bottom: 5px; color: #666;">Group O Members:</h5>
  <ul style="list-style: none; padding-left: 0; line-height: 1.6;">
    <li>Ana Margarida Valente | <a href="mailto:20240936@novaims.unl.pt" style="color: #97b83a;">20240936@novaims.unl.pt</a></li>
    <li>Luana Rocha | <a href="mailto:20240111@novaims.unl.pt" style="color: #97b83a;">20240111@novaims.unl.pt</a></li>
    <li>Pedro Costa | <a href="mailto:20222121@novaims.unl.pt" style="color: #97b83a;">20222121@novaims.unl.pt</a></li>
    <li>Susana Reis | <a href="mailto:20240567@novaims.unl.pt" style="color: #97b83a;">20240567@novaims.unl.pt</a></li>
  </ul>

</div>

---

# Genetic Algorithm for Festival Scheduling

### Project Overview: Music Festival Lineup Optimization

The goal of this project is to design an optimal music festival lineup by scheduling artists across 5 stages and 7 time slots. Each artist is characterized by a popularity score, genre, and pairwise fanbase conflict scores with other artists.

To evaluate a lineup, we optimize three equally important and normalized objectives:
- **Prime Slot Popularity**: Maximizing the popularity of artists in final time slots.
- **Genre Diversity**: Ensuring a wide range of musical genres per time slot.
- **Conflict Penalty**: Minimizing scheduling of artists with overlapping fan bases at the same time.

Each solution must comply with strict constraints: all artists must be assigned exactly once, and no lineup should include duplicates or omissions.

The dataset includes artist information and a conflict matrix, and solutions are evolved under these conditions to find high quality festival arrangements.

### 📁 Project Structure Overview

The components of the Music Festival Lineup Optimization project:

- **`data/`**  
  Contains the input datasets:
  - `artists(in).csv` – Artist details including name, genre, and popularity.  
  - `conflicts(in).csv` – Matrix capturing fanbase conflict scores between artists.

- **`documents/`**  
  Reference materials for the project:
  - `CIFO_2024_2025_Project.pdf` – Official project description.

- **`lib/`**  
  Modular Python implementations of the core algorithms and utilities:
  - `Projectsolution.py`: Defines the `Solution` class representing a festival lineup.
  - `fitness.py`: Calculates the multi-objective fitness score (popularity, diversity, conflicts).
  - `crossover.py`, `mutation.py`, `selection.py`: Genetic Algorithm operators.
  - `genetic_algorithm.py`: Main loop for GA execution.
  - `hill_climbing.py`, `simulated_annealing.py`: Local search optimizers for comparison.
  - `__init__.py`: Makes `lib` a Python package.

- **`src/`**  
  - `PROJECT.ipynb`: Main Jupyter Notebook with experimentation, analysis, and results.  
  - `ga_fitness_results.csv`: Stores GA performance results.

- **`requirements.txt`**  
  List of Python packages required to run the project environment.


---

### Grid Search Experiment

We conducted an extensive grid search to evaluate different combinations of GA operators and configurations:

- **Crossover Methods:**  
  - Partially Matched Crossover (PMX)  
  - Order Crossover (OX)  

- **Mutation Methods:**  
  - Insertion Mutation  
  - Slot Shuffle Mutation  
  - Prime Slot Mutation  

- **Selection Methods:**  
  - Tournament Selection 
  - Ranking Selection 

- **Elitism:**  
  - Enabled  
  - Disabled

### Results and Analysis

The grid search helps us understand how different GA components impact solution quality and convergence speed.

### Comparative Evaluation

To further validate the effectiveness of our bestcperforming Genetic Algorithm configuration, we benchmark it against two classic local search algorithms: **Hill Climbing** and **Simulated Annealing**. 
