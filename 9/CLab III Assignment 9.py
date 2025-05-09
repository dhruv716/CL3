import csv
from functools import reduce
from collections import defaultdict

# Define mapper function to emit (year, temperature) pairs
def mapper(row):
    year = row["Date/Time"].split("-")[0]  # Extract year from "Date/Time" column
    temperature = float(row["Temp_C"])  # Convert temperature to float
    return (year, temperature)

# Define reducer function to calculate sum and count of temperatures for each year
def reducer(accumulated, current):
    accumulated[current[0]][0] += current[1]
    accumulated[current[0]][1] += 1
    return accumulated

# Read the weather dataset
weather_data = []
with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        weather_data.append(row)
        
        # Map phase
mapped_data = map(mapper, weather_data)

# Reduce phase
reduced_data = reduce(reducer, mapped_data, defaultdict(lambda: [0, 0]))

# Calculate average temperature for each year
avg_temp_per_year = {year: total_temp / count for year, (total_temp, count) in reduced_data.items()}

# Find coolest and hottest year
coolest_year = min(avg_temp_per_year.items(), key=lambda x: x[1])
hottest_year = max(avg_temp_per_year.items(), key=lambda x: x[1])

print("Coolest Year:", coolest_year[0], "Average Temperature:", coolest_year[1])
print("Hottest Year:", hottest_year[0], "Average Temperature:", hottest_year[1])


"""

Can you briefly explain what MapReduce is and how it works?
MapReduce is a programming model for processing large datasets in a distributed environment. It has two main phases:
Map: Processes input data and outputs key-value pairs.
Reduce: Aggregates the intermediate key-value pairs from the Map phase to produce final results.
It runs across many nodes, ensuring scalability and fault tolerance.

What are the advantages of using MapReduce for processing large-scale data?
MapReduce provides high scalability, fault tolerance, and parallel processing. It simplifies coding for big data tasks, automatically handles data distribution, and works well with large clusters, making it ideal for processing terabytes or petabytes of data efficiently.

How does data shuffling occur in MapReduce, and why is it important?
Shuffling is the process between Map and Reduce phases where the framework groups and transfers intermediate key-value pairs with the same key to the same reducer. It’s crucial because it ensures that each reducer gets all values associated with a particular key, enabling correct aggregation.





## ✅ Problem Statement Summary

> Design a **distributed application** to find the **coolest** and **hottest year** from weather data using **MapReduce**.

---

## 📘 What the Code Does (Line-by-Line Explanation)

### 1. **Imports**

```python
import csv
from functools import reduce
from collections import defaultdict
```

* `csv` is for reading the weather data file.
* `reduce` is a functional programming tool to aggregate a result.
* `defaultdict` lets us default to `[0, 0]` for sum and count pairs.

---

### 2. **Map Function**

```python
def mapper(row):
    year = row["Date/Time"].split("-")[0]  # Gets the year from the date string
    temperature = float(row["Temp_C"])     # Converts temperature to float
    return (year, temperature)
```

🧠 This represents the **map phase** of MapReduce: it transforms raw data into `(key, value)` pairs → in this case `(year, temperature)`.

---

### 3. **Reduce Function**

```python
def reducer(accumulated, current):
    accumulated[current[0]][0] += current[1]  # Add temperature to sum
    accumulated[current[0]][1] += 1           # Increment count
    return accumulated
```

🧠 The **reduce phase** accumulates the sum and count of temperatures per year.

---

### 4. **Read the CSV**

```python
weather_data = []
with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        weather_data.append(row)
```

📄 Reads the CSV file into a list of dictionaries (`weather_data`), each representing a row.

---

### 5. **Map Phase**

```python
mapped_data = map(mapper, weather_data)
```

Runs the `mapper()` function on each row → transforms raw data into `(year, temperature)` pairs.

---

### 6. **Reduce Phase**

```python
reduced_data = reduce(reducer, mapped_data, defaultdict(lambda: [0, 0]))
```

→ Aggregates the mapped data into:

```python
{
  '2015': [sum_of_temperatures, count],
  '2016': [sum_of_temperatures, count],
  ...
}
```

---

### 7. **Calculate Averages**

```python
avg_temp_per_year = {year: total_temp / count for year, (total_temp, count) in reduced_data.items()}
```

→ Creates a dictionary with average temperature per year.

---

### 8. **Find Extremes**

```python
coolest_year = min(avg_temp_per_year.items(), key=lambda x: x[1])
hottest_year = max(avg_temp_per_year.items(), key=lambda x: x[1])
```

→ Finds the year with the **lowest** and **highest** average temperature.

---

### 9. **Print Result**

```python
print("Coolest Year:", coolest_year[0], "Average Temperature:", coolest_year[1])
print("Hottest Year:", hottest_year[0], "Average Temperature:", hottest_year[1])
```

✔ Outputs the final result.

---

## 🧠 How This Implements MapReduce

| Phase              | Role                                         | Code                         |
| ------------------ | -------------------------------------------- | ---------------------------- |
| **Map**            | Emit `(year, temperature)` pairs             | `mapper()`                   |
| **Shuffle & Sort** | Group by year (implicit using `defaultdict`) | Done via `reduce()`          |
| **Reduce**         | Aggregate and compute averages               | `reducer()` + final division |

---

## ⚠️ Distributed Nature?

Right now this code is **not distributed** — it's just a **local simulation** of MapReduce.

To actually **run it in a distributed environment**, you could:

1. **Use Hadoop Streaming**: Convert your Python code to work with `stdin/stdout` for Hadoop jobs.
2. **Use PySpark**: Replace this with PySpark’s `map()`, `reduceByKey()`, etc. to run on clusters.

"""
