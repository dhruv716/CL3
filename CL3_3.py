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
