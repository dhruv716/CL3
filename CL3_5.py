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
