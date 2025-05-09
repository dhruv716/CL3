class FuzzySet:
    def __init__(self, elements):
        self.elements = elements  
    
    def union(self, other):
        return FuzzySet({x: max(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) | set(other.elements)})
    
    def intersection(self, other):
        return FuzzySet({x: min(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) & set(other.elements)})
    
    def complement(self):
        return FuzzySet({x: 1 - self.elements[x] for x in self.elements})
    
    def difference(self, other):
        return FuzzySet({x: min(self.elements.get(x, 0), 1 - other.elements.get(x, 0)) for x in self.elements})
    
    def __repr__(self):
        return str(self.elements)

class FuzzyRelation:
    def __init__(self, set1, set2):
        self.relation = {(x, y): min(set1.elements[x], set2.elements[y]) for x in set1.elements for y in set2.elements}
    
    def max_min_composition(self, other):
        result = {}
        for (a, b) in self.relation:
            for (c, d) in other.relation:
                if b == c:
                    result[(a, d)] = max(result.get((a, d), 0), min(self.relation[(a, b)], other.relation[(c, d)]))
        return result
    
    def __repr__(self):
        return str(self.relation)

# Example Usage
A = FuzzySet({'x1': 0.2, 'x2': 0.7, 'x3': 1.0})
B = FuzzySet({'x1': 0.5, 'x2': 0.4, 'x3': 0.8})
C = FuzzySet({'y1': 0.6, 'y2': 0.9})

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Complement of A:", A.complement())
print("Difference A - B:", A.difference(B))

R1 = FuzzyRelation(A, C)
R2 = FuzzyRelation(C, B)

print("Fuzzy Relation R1:", R1)
print("Fuzzy Relation R2:", R2)
print("Max-Min Composition of R1 and R2:", R1.max_min_composition(R2))


"""

Absolutely! Here are concise 4–6 line answers for each question on fuzzy logic:

---

**1. Explain the concept of a fuzzy set and its representation:**
A fuzzy set is a class of objects with a continuum of membership grades between 0 and 1. Unlike classical sets (where elements either belong or don’t), fuzzy sets allow partial membership. It's represented as a set of ordered pairs: $A = \{(x, \mu_A(x))\}$, where $\mu_A(x)$ is the membership function.

---

**2. Define a fuzzy relation and its purpose in fuzzy logic:**
A fuzzy relation is an extension of a classical relation where the degree of relationship between elements is expressed with values from 0 to 1. It models uncertainty and vague associations between elements of two or more fuzzy sets, commonly used in fuzzy inference systems.

---

**3. How is the Cartesian product of two fuzzy sets computed?**
The Cartesian product of fuzzy sets $A$ and $B$ forms a fuzzy relation $R$, where each pair $(x, y)$ has a membership value $\mu_R(x, y) = \min[\mu_A(x), \mu_B(y)]$. It combines elements of both sets with the minimum of their membership values.

---

**4. Discuss the steps involved in performing max-min composition on fuzzy relations:**

* Take two fuzzy relations $R$ (from X to Y) and $S$ (from Y to Z).
* For each pair $(x, z)$, compute the minimum of $\mu_R(x, y)$ and $\mu_S(y, z)$ for all $y$.
* Then take the maximum of these minimum values.
* The result is a new fuzzy relation $T$ from X to Z, representing composed inference.



Here's a full breakdown of your **FuzzySet and FuzzyRelation** Python implementation, how each part works, and how the operations are computed.

---

## 🔢 What is a Fuzzy Set?

A **fuzzy set** allows elements to have partial membership, meaning each element has a **degree of membership** ranging from `0` (not a member) to `1` (full member). You're implementing standard fuzzy set operations: union, intersection, complement, difference, and fuzzy relations.

---

## 📄 Code Explanation

### ✅ Class: `FuzzySet`

```python
class FuzzySet:
    def __init__(self, elements):
        self.elements = elements
```

* Initializes the fuzzy set with elements and their membership values.
* Example: `{'x1': 0.2, 'x2': 0.7, 'x3': 1.0}`

---

#### 🔹 `union(self, other)`

```python
return FuzzySet({x: max(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) | set(other.elements)})
```

* Union takes the **maximum** membership of each element from both sets.
* The `|` operator finds the union of keys.

---

#### 🔹 `intersection(self, other)`

```python
return FuzzySet({x: min(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) & set(other.elements)})
```

* Intersection takes the **minimum** membership of each element from both sets.
* `&` gets common keys.

---

#### 🔹 `complement(self)`

```python
return FuzzySet({x: 1 - self.elements[x] for x in self.elements})
```

* Complement in fuzzy logic is `1 - membership value`.

---

#### 🔹 `difference(self, other)`

```python
return FuzzySet({x: min(self.elements.get(x, 0), 1 - other.elements.get(x, 0)) for x in self.elements})
```

* Fuzzy difference `A - B` is computed as:
  `min(A(x), 1 - B(x))` for each element in A.

---

#### 🔹 `__repr__(self)`

```python
return str(self.elements)
```

* Returns string representation for printing.

---

### ✅ Class: `FuzzyRelation`

#### 🔹 Constructor

```python
self.relation = {(x, y): min(set1.elements[x], set2.elements[y]) for x in set1.elements for y in set2.elements}
```

* Forms a **Cartesian product** of two sets (set1 × set2).
* Membership for each `(x, y)` pair is the **minimum** of the individual values.
* Example: If A(x1)=0.2, C(y1)=0.6 → R1(x1, y1)=min(0.2, 0.6)=0.2

---

#### 🔹 `max_min_composition(self, other)`

```python
result[(a, d)] = max(result.get((a, d), 0), min(self.relation[(a, b)], other.relation[(c, d)]))
```

* Computes **Max-Min Composition** of two fuzzy relations `R1` and `R2`.
* For all pairs where the second element of a pair in R1 matches the first in R2 (`b == c`), it finds:

  ```
  result[(a, d)] = max over all b of (min(R1(a, b), R2(b, d)))
  ```

---

#### 🔹 `__repr__(self)`

```python
return str(self.relation)
```

* String form of relation for printing.

---

## 📌 Example Execution

### ✅ Sets:

```python
A = {'x1': 0.2, 'x2': 0.7, 'x3': 1.0}
B = {'x1': 0.5, 'x2': 0.4, 'x3': 0.8}
C = {'y1': 0.6, 'y2': 0.9}
```

### ✅ Set Operations:

* **Union**: max of A and B:

  ```
  {'x1': 0.5, 'x2': 0.7, 'x3': 1.0}
  ```
* **Intersection**: min of A and B:

  ```
  {'x1': 0.2, 'x2': 0.4, 'x3': 0.8}
  ```
* **Complement of A**:

  ```
  {'x1': 0.8, 'x2': 0.3, 'x3': 0.0}
  ```
* **Difference A - B**:

  ```
  {'x1': 0.5, 'x2': 0.6, 'x3': 0.2}
  ```

---

### ✅ Fuzzy Relations

#### R1 = A × C (min of each pair):

```
{
 ('x1', 'y1'): 0.2, ('x1', 'y2'): 0.2,
 ('x2', 'y1'): 0.6, ('x2', 'y2'): 0.7,
 ('x3', 'y1'): 0.6, ('x3', 'y2'): 0.9
}
```

#### R2 = C × B:

```
{
 ('y1', 'x1'): 0.5, ('y1', 'x2'): 0.4, ('y1', 'x3'): 0.6,
 ('y2', 'x1'): 0.5, ('y2', 'x2'): 0.4, ('y2', 'x3'): 0.8
}
```

---

### ✅ Max-Min Composition (R1 ∘ R2)

For example:

* To compute result\[('x1', 'x1')]:

  * From `R1('x1', 'y1') = 0.2`, `R2('y1', 'x1') = 0.5` → min(0.2, 0.5) = 0.2
  * From `R1('x1', 'y2') = 0.2`, `R2('y2', 'x1') = 0.5` → min(0.2, 0.5) = 0.2
  * max(0.2, 0.2) = **0.2**

This process repeats for all (a, d) where intermediate `b == c`.

"""


