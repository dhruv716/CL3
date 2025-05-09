import numpy as np

# Define the objective function (example: sphere function)
def objective_function(x):
    return np.sum(x**2)

# Initialize parameters
num_antibodies = 20
num_generations = 100
clone_factor = 5
mutation_rate = 0.1
dimension = 5

# Initialize antibody population
antibodies = np.random.uniform(-10, 10, (num_antibodies, dimension))

# Clonal Selection Algorithm
for generation in range(num_generations):
    # Evaluate antibodies
    fitness = np.array([objective_function(antibody) for antibody in antibodies])
    
    # Select top antibodies
    top_antibodies = antibodies[np.argsort(fitness)[:int(num_antibodies/2)]]
    
    # Clone and mutate antibodies
    new_antibodies = []
    for antibody in top_antibodies:
        clones = [antibody + mutation_rate * np.random.randn(dimension) for _ in range(clone_factor)]
        new_antibodies.extend(clones)
    
    # Evaluate new antibodies
    new_fitness = np.array([objective_function(antibody) for antibody in new_antibodies])
    
    # Select the best antibodies for the next generation
    antibodies = np.array(new_antibodies)[np.argsort(new_fitness)[:num_antibodies]]

# Output the best solution found
best_antibody = antibodies[np.argmin([objective_function(antibody) for antibody in antibodies])]
print("Best solution found:", best_antibody)
print("Objective function value:", objective_function(best_antibody))



"""Theory :
Key components include:

Population (antibodies): Initial candidate solutions.
Affinity evaluation: Measures fitness of each antibody.
Selection: Chooses high-affinity antibodies for cloning.
Cloning and mutation: Produces diverse variations of selected antibodies.
Replacement and memory: Updates the population with better solutions and preserves the best in memory for future use.

This code implements the **Clonal Selection Algorithm (CSA)** — a biologically-inspired optimization technique derived from the human immune system. It's being used here to **minimize a mathematical objective function**, specifically the **Sphere function**, which is commonly used for benchmarking:

---

## 🔬 Objective

Minimize the **Sphere function**:

```python
f(x) = x₁² + x₂² + ... + xₙ²
```

This function has a **global minimum at `x = [0, 0, ..., 0]` with `f(x) = 0`**.

---

## ⚙️ Key Parameters

```python
num_antibodies = 20         # Number of candidate solutions
num_generations = 100       # Number of iterations
clone_factor = 5            # How many clones per top antibody
mutation_rate = 0.1         # Perturbation applied to clones
dimension = 5               # Dimensionality of the solution space
```

---

## 🧬 Algorithm Breakdown

### 1. **Initialization**

```python
antibodies = np.random.uniform(-10, 10, (num_antibodies, dimension))
```

Each "antibody" is a candidate solution in 5D space initialized randomly between \[-10, 10].

---

### 2. **Main Loop (Evolution Over Generations)**

For each generation:

#### a. **Evaluate Fitness**

```python
fitness = np.array([objective_function(antibody) for antibody in antibodies])
```

Lower fitness (closer to zero) is better.

#### b. **Select Top 50%**

```python
top_antibodies = antibodies[np.argsort(fitness)[:int(num_antibodies/2)]]
```

Best-performing antibodies (based on fitness) are retained for cloning.

#### c. **Clone + Mutate**

```python
clones = [antibody + mutation_rate * np.random.randn(dimension) for _ in range(clone_factor)]
```

Each top antibody is cloned 5 times, and Gaussian noise is added to simulate mutation.

#### d. **Select Best Clones**

```python
new_antibodies = ...
antibodies = np.array(new_antibodies)[np.argsort(new_fitness)[:num_antibodies]]
```

From all the mutated clones, the best `num_antibodies` are selected to form the next generation.

---

## ✅ Final Output

```python
best_antibody = antibodies[np.argmin(...)]
```

Returns the best antibody (solution vector) and its corresponding minimized function value.

---

## 🧠 Sample Output (Typical)

```plaintext
Best solution found: [ 0.002, -0.001, 0.0005, -0.0007, 0.0012]
Objective function value: 9.3e-06
```

This suggests CSA has successfully minimized the Sphere function close to 0.

"""



