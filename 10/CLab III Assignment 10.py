import numpy as np

# Define the problem - set of cities and distances
cities = np.array([[0, 0], [1, 2], [3, 1], [5, 3], [2, 4]])
num_cities = len(cities)

# Define parameters
num_ants = 5
num_iterations = 100
alpha = 1  # Pheromone factor
beta = 2   # Distance factor
rho = 0.1  # Pheromone evaporation rate
Q = 1      # Pheromone deposit factor

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))

# Define distance function
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

# Initialize best tour
best_tour = None
best_distance = np.inf

# Perform iterations
for iteration in range(num_iterations):
    ant_tours = []
    tour_distances = []
    
    # Move ants
    for ant in range(num_ants):
        current_city = np.random.randint(num_cities)
        tour = [current_city]
        distance_traveled = 0
        
        while len(tour) < num_cities:
            probabilities = []
            for city in range(num_cities):
                if city not in tour:
                    pheromone_level = pheromone[current_city][city]
                    dist = distance(cities[current_city], cities[city])
                    prob = (pheromone_level ** alpha) * ((1 / dist) ** beta)
                    probabilities.append((city, prob))
            
            probabilities = np.array(probabilities)
            probabilities[:, 1] /= np.sum(probabilities[:, 1])
            
            next_city = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])
            tour.append(int(next_city))
            distance_traveled += distance(cities[current_city], cities[int(next_city)])
            current_city = int(next_city)
        
        ant_tours.append(tour)
        tour_distances.append(distance_traveled)
    
    # Update pheromone levels
    pheromone *= (1 - rho)
    for i in range(num_ants):
        tour = ant_tours[i]
        for j in range(num_cities - 1):
            pheromone[tour[j]][tour[j+1]] += (Q / tour_distances[i])
        pheromone[tour[-1]][tour[0]] += (Q / tour_distances[i])
    
    # Update best tour
    min_distance_idx = np.argmin(tour_distances)
    if tour_distances[min_distance_idx] < best_distance:
        best_tour = ant_tours[min_distance_idx]
        best_distance = tour_distances[min_distance_idx]

print("Best tour:", best_tour)
print("Best distance:", best_distance)


"""

What is the Traveling Salesman Problem (TSP)?
TSP is a classic optimization problem where a salesman must visit a set of cities exactly once and return to the starting city, minimizing the total travel distance or cost. It's NP-hard, meaning no known algorithm can solve it efficiently for large inputs.

How does Ant Colony Optimization (ACO) work, and what are its key components?

ACO is a bio-inspired algorithm that simulates how ants find the shortest path using pheromones. Key components include:
Ant agents: Construct paths probabilistically.
Pheromone trails: Indicate path desirability.
Heuristic information: Like inverse distance between cities.
Pheromone evaporation and update: Helps balance exploration and exploitation.

What role do pheromone trails play in ACO?
Pheromone trails guide ants in choosing paths; stronger pheromone levels increase the probability of a path being chosen. Over time, frequently used and shorter paths accumulate more pheromones, reinforcing optimal or near-optimal solutions.





This code is an implementation of the **Ant Colony Optimization (ACO)** algorithm to solve a simplified **Traveling Salesman Problem (TSP)**. Here's a **line-by-line explanation**:

---

### 🧩 Problem Setup

```python
import numpy as np
```

→ Imports NumPy for numerical operations (like arrays, math functions, etc.).

```python
# Define the problem - set of cities and distances
cities = np.array([[0, 0], [1, 2], [3, 1], [5, 3], [2, 4]])
```

→ Defines the coordinates of 5 cities as 2D points. Each row is a city, like `[x, y]`.

```python
num_cities = len(cities)
```

→ Calculates the number of cities (5 here).

---

### ⚙️ Parameters

```python
num_ants = 5
```

→ Number of ants used in each iteration.

```python
num_iterations = 100
```

→ Total iterations the algorithm will run.

```python
alpha = 1  # Pheromone factor
beta = 2   # Distance factor
rho = 0.1  # Pheromone evaporation rate
Q = 1      # Pheromone deposit factor
```

→ ACO parameters:

* `alpha`: importance of pheromone
* `beta`: importance of distance (shorter is better)
* `rho`: how fast pheromone evaporates
* `Q`: amount of pheromone deposited

---

### 🌐 Pheromone Initialization

```python
pheromone = np.ones((num_cities, num_cities))
```

→ Initializes a matrix where each entry `pheromone[i][j]` starts with `1`, representing the trail strength from city `i` to `j`.

---

### 📏 Distance Function

```python
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)
```

→ Calculates the **Euclidean distance** between two cities using the formula √((x2-x1)² + (y2-y1)²).

---

### 🥇 Best Tour Initialization

```python
best_tour = None
best_distance = np.inf
```

→ Keeps track of the shortest tour found so far and its distance. Starts with `infinity`.

---

### 🔁 Main ACO Loop

```python
for iteration in range(num_iterations):
```

→ Repeats the whole ant simulation and pheromone update `100` times.

---

### 🐜 Ants Move and Build Tours

```python
    ant_tours = []
    tour_distances = []
```

→ Lists to store each ant's tour and distance traveled.

```python
    for ant in range(num_ants):
```

→ Loop over each ant.

```python
        current_city = np.random.randint(num_cities)
        tour = [current_city]
        distance_traveled = 0
```

→ Each ant starts from a random city. It builds its `tour`, accumulating `distance_traveled`.

---

### 🗺️ Probabilistic Path Selection

```python
        while len(tour) < num_cities:
            probabilities = []
            for city in range(num_cities):
                if city not in tour:
```

→ While the ant hasn’t visited all cities, it evaluates unvisited ones.

```python
                    pheromone_level = pheromone[current_city][city]
                    dist = distance(cities[current_city], cities[city])
                    prob = (pheromone_level ** alpha) * ((1 / dist) ** beta)
                    probabilities.append((city, prob))
```

→ Calculates the **attractiveness** of going to each unvisited city, influenced by:

* high pheromone
* short distance

```python
            probabilities = np.array(probabilities)
            probabilities[:, 1] /= np.sum(probabilities[:, 1])
```

→ Converts raw probabilities into a **proper probability distribution** (they sum to 1).

```python
            next_city = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])
```

→ Chooses the next city **randomly based on the probabilities**.

```python
            tour.append(int(next_city))
            distance_traveled += distance(cities[current_city], cities[int(next_city)])
            current_city = int(next_city)
```

→ Moves to the selected city, adds its distance, and updates current city.

---

### 📥 Save Ant's Tour & Distance

```python
        ant_tours.append(tour)
        tour_distances.append(distance_traveled)
```

→ After visiting all cities, store the tour and its distance.

---

### 🔄 Pheromone Update

```python
    pheromone *= (1 - rho)
```

→ **Evaporate pheromones** on all paths.

```python
    for i in range(num_ants):
        tour = ant_tours[i]
        for j in range(num_cities - 1):
            pheromone[tour[j]][tour[j+1]] += (Q / tour_distances[i])
        pheromone[tour[-1]][tour[0]] += (Q / tour_distances[i])
```

→ For each ant's tour:

* Increase pheromone on all edges it used
* The amount is **inversely proportional to tour length** (shorter tour deposits more)
* Also deposits for the last city back to the first to complete the loop

---

### ✅ Update Global Best

```python
    min_distance_idx = np.argmin(tour_distances)
    if tour_distances[min_distance_idx] < best_distance:
        best_tour = ant_tours[min_distance_idx]
        best_distance = tour_distances[min_distance_idx]
```

→ If this iteration produced a better tour than ever before, save it as `best_tour`.

---

### 🖨️ Final Output

```python
print("Best tour:", best_tour)
print("Best distance:", best_distance)
```

→ Prints the best tour found and the total distance.

"""

