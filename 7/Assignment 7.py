import random
from deap import base, creator, tools, algorithms

# Define the evaluation function (minimize a simple mathematical function)
def eval_func(individual):
    # Example evaluation function (minimize a quadratic function)
    return sum(x ** 2 for x in individual),

# DEAP setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Define attributes and individuals
toolbox.register("attr_float", random.uniform, -5.0, 5.0)  # Example: Float values between -5 and 5
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)  # Example: 3-dimensional individual
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function and genetic operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create population
population = toolbox.population(n=50)

# Genetic Algorithm parameters
generations = 20

# Run the algorithm
for gen in range(generations):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit

    population = toolbox.select(offspring, k=len(population))

# Get the best individual after generations
best_ind = tools.selBest(population, k=1)[0]
best_fitness = best_ind.fitness.values[0]

print("Best individual:", best_ind)
print("Best fitness:", best_fitness)


"""

Explain the key components of DEAP:

Creator: Defines the structure of individuals (solutions) and fitness.
Toolbox: Registers evolutionary operators like selection, mutation, and crossover.
Population: A collection of individuals.
Algorithms: Contains ready-to-use evolutionary strategies (e.g., eaSimple, eaMuPlusLambda).
Fitness function: Evaluates the quality of each individual.

What are the steps involved in using DEAP to solve an optimization problem?

Define the problem and fitness function.
Create individuals and register them using creator.
Register genetic operators in toolbox (selection, mutation, crossover).
Initialize the population.
Run the evolutionary algorithm loop (evaluate, select, mate, mutate).
Retrieve and analyze the best solution from the final population.




This script implements a **Genetic Algorithm (GA)** using the [**DEAP** library](https://deap.readthedocs.io/en/master/) to **minimize a quadratic objective function** $ \(f(x) = x_1^2 + x_2^2 + x_3^2$ ). Here's a breakdown of how it works:

---

## 🧠 **Goal**

Minimize the function:

$$
f(x) = x_1^2 + x_2^2 + x_3^2
$$

This is a convex function with a **global minimum at** $x = [0, 0, 0]$ and $f(x) = 0$.

---

## ⚙️ **Key Components in DEAP**

### 1. **Fitness & Individual Definition**

```python
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
```

* The goal is minimization (`-1.0`).
* Each **individual** is a list (i.e., a vector) of 3 floats.

---

### 2. **Attribute & Population Initialization**

```python
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
```

* Each gene is a float in $[-5, 5]$.
* A population of 50 individuals is created.

---

### 3. **Genetic Operators**

```python
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
```

* **Crossover**: `cxBlend` mixes genes from parents.
* **Mutation**: `mutGaussian` adds Gaussian noise with 20% probability per gene.
* **Selection**: Tournament selection with size 3.

---

### 4. **GA Execution**

```python
for gen in range(generations):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
```

* For 20 generations, new offspring are produced and evaluated.
* Selection determines who survives into the next generation.

---

### 5. **Best Result**

```python
best_ind = tools.selBest(population, k=1)[0]
```

Prints the best solution and its fitness at the end.

---

## ✅ **Sample Output**

Typical output would look like:

```
Best individual: [0.001, -0.0005, 0.0007]
Best fitness: 1.2e-06
```

This shows the GA successfully minimized the objective function close to zero.

"""

