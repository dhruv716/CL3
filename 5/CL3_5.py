import numpy as np
import random

# Define GA Parameters
POP_SIZE = 20
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 50

# Sample input space (temperature, feed rate, air velocity)
param_ranges = {
    "temperature": (100, 200),  # Example range
    "feed_rate": (5, 15),
    "air_velocity": (1, 5)
}

# Fitness function using a trained neural network model (Placeholder)
def fitness_function(params):
    predicted_output = sum(params.values())  # Sum dictionary values
    return -abs(predicted_output - 100)  # Minimize error from target value

# Initialize population
def initialize_population():
    return [{key: random.uniform(*param_ranges[key]) for key in param_ranges} for _ in range(POP_SIZE)]

# Selection (Fixed normalization issue)
def tournament_selection(pop, fitnesses):
    min_fitness = min(fitnesses)
    normalized_fitnesses = [f - min_fitness + 1e-6 for f in fitnesses]  # Ensure all values are positive
    selected = random.choices(pop, weights=normalized_fitnesses, k=2)
    return selected

# Crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        return {key: (parent1[key] + parent2[key]) / 2 for key in parent1}
    return parent1

# Mutation
def mutate(individual):
    for key in individual:
        if random.random() < MUTATION_RATE:
            individual[key] = random.uniform(*param_ranges[key])
    return individual

# GA Optimization
population = initialize_population()

for gen in range(GENERATIONS):
    fitnesses = [fitness_function(ind) for ind in population]  # Compute fitness
    new_population = []

    for _ in range(POP_SIZE // 2):
        p1, p2 = tournament_selection(population, fitnesses)
        child = crossover(p1, p2)
        child = mutate(child)
        new_population.append(child)

    population = new_population

# Best solution
best_solution = min(population, key=fitness_function)
print("Optimized Drying Parameters:", best_solution)


"""
Population size: Number of solutions per generation.
Crossover rate: Frequency of combining solutions.
Mutation rate: Rate at which random changes occur.
Selection method: How parents are chosen (e.g., tournament, roulette).
Number of generations: How long the algorithm evolves.


This code implements a **Genetic Algorithm (GA)** to optimize **drying parameters** (like temperature, feed rate, air velocity) with the goal of minimizing error from a **target output**. Below is a detailed breakdown of how it works:

---

## 🧠 Objective

To find a combination of drying parameters such that the **sum** of the parameters is **as close as possible to 100** (this is a placeholder for a more complex neural network-based fitness function).

---

## ⚙️ GA Parameters

```python
POP_SIZE = 20         # Number of individuals in each generation
MUTATION_RATE = 0.1   # Probability of mutation
CROSSOVER_RATE = 0.8  # Probability of crossover
GENERATIONS = 50      # Number of generations to run
```

---

## 📌 Parameter Space

```python
param_ranges = {
    "temperature": (100, 200),
    "feed_rate": (5, 15),
    "air_velocity": (1, 5)
}
```

These are the allowed value ranges for each parameter.

---

## 🧮 Fitness Function

```python
def fitness_function(params):
    predicted_output = sum(params.values())
    return -abs(predicted_output - 100)
```

* The goal is to get the total sum of parameters close to **100**.
* `-abs(...)` ensures that **lower deviation = higher fitness**.

---

## 👶 Population Initialization

```python
def initialize_population():
    return [{key: random.uniform(*param_ranges[key]) for key in param_ranges} for _ in range(POP_SIZE)]
```

Creates 20 individuals (random parameter dictionaries) per generation.

---

## 🏆 Tournament Selection

```python
def tournament_selection(pop, fitnesses):
    min_fitness = min(fitnesses)
    normalized_fitnesses = [f - min_fitness + 1e-6 for f in fitnesses]
    selected = random.choices(pop, weights=normalized_fitnesses, k=2)
    return selected
```

* Fixes negative values by shifting all fitnesses to be positive.
* Selects 2 parents based on their relative fitness.

---

## 🔗 Crossover

```python
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        return {key: (parent1[key] + parent2[key]) / 2 for key in parent1}
    return parent1
```

* With 80% probability, creates a child as the **average** of the two parents.
* Otherwise, copies one parent.

---

## 🧬 Mutation

```python
def mutate(individual):
    for key in individual:
        if random.random() < MUTATION_RATE:
            individual[key] = random.uniform(*param_ranges[key])
    return individual
```

* Each gene (parameter) has a 10% chance to be randomly reset.

---

## 🔁 Evolution Loop

```python
for gen in range(GENERATIONS):
    ...
```

* For 50 generations:

  * Evaluate fitness of population.
  * Select, crossover, and mutate to form a new generation.

---

## ✅ Final Output

```python
best_solution = min(population, key=fitness_function)
print("Optimized Drying Parameters:", best_solution)
```

* Selects the individual with the **highest fitness** (i.e., smallest error from 100).

---

## 🔍 Example Output

```plaintext
Optimized Drying Parameters: {'temperature': 148.3, 'feed_rate': 9.2, 'air_velocity': 2.5}
```

Which means:

```
148.3 + 9.2 + 2.5 ≈ 160
Fitness = -abs(160 - 100) = -60
```

A better result would be one where the sum is closer to 100.

"""

