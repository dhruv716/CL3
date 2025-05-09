import random

class LoadBalancer:
	def __init__(self, servers):
		self.servers = servers
		self.server_index_rr = 0

	def round_robin(self):
		server = self.servers[self.server_index_rr]
		self.server_index_rr = (self.server_index_rr + 1) % len(self.servers)
		return server

	def random_selection(self):
		return random.choice(self.servers)

def simulate_client_requests(load_balancer, num_requests):
	for i in range(num_requests):
		# Simulating client request
		print(f"Request {i+1}: ", end="")
		# Using Round Robin algorithm for load balancing
		server_rr = load_balancer.round_robin()
		print(f"Round Robin - Server {server_rr}")
		# Using Random algorithm for load balancing
		server_random = load_balancer.random_selection()
		print(f"Random - Server {server_random}")
		print()

if __name__ == "__main__":
	# List of servers
	servers = ["Server A", "Server B", "Server C"]
	# Create a LoadBalancer instance
	load_balancer = LoadBalancer(servers)
	# Simulate 10 client requests
	simulate_client_requests(load_balancer, 10)


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


This Python program simulates **load balancing** across multiple servers using two algorithms: **Round Robin** and **Random Selection**.

---

## 💡 What's the Goal?

To **distribute client requests** among a list of servers using:

1. **Round Robin**: Each server takes turns in a fixed order.
2. **Random Selection**: A server is picked at random for each request.

---

## 📦 Class: `LoadBalancer`

```python
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_index_rr = 0
```

* **`servers`**: A list of server names, like `["Server A", "Server B", "Server C"]`.
* **`server_index_rr`**: Keeps track of the next server for Round Robin.

---

### 🔁 Method: `round_robin()`

```python
def round_robin(self):
    server = self.servers[self.server_index_rr]
    self.server_index_rr = (self.server_index_rr + 1) % len(self.servers)
    return server
```

* Selects the next server in the list.
* Wraps around using modulo `%` after reaching the end of the list.

---

### 🎲 Method: `random_selection()`

```python
def random_selection(self):
    return random.choice(self.servers)
```

* Picks any server at random for each request.

---

## 🧪 Function: `simulate_client_requests(load_balancer, num_requests)`

```python
for i in range(num_requests):
    print(f"Request {i+1}: ", end="")
    server_rr = load_balancer.round_robin()
    print(f"Round Robin - Server {server_rr}")
    server_random = load_balancer.random_selection()
    print(f"Random - Server {server_random}")
    print()
```

* Simulates `num_requests` client requests.
* For each request, it prints:

  * Server chosen by Round Robin.
  * Server chosen by Random Selection.

---

## ▶️ Example Output (approximate)

```plaintext
Request 1: Round Robin - Server A
          Random - Server C

Request 2: Round Robin - Server B
          Random - Server A

Request 3: Round Robin - Server C
          Random - Server B
```

---

## ✅ Summary

| Method           | How It Works                        | Use Case                              |
| ---------------- | ----------------------------------- | ------------------------------------- |
| Round Robin      | Sequentially cycles through servers | Predictable, fair distribution        |
| Random Selection | Picks a server randomly             | Fast and simple, but may overload one |

"""

