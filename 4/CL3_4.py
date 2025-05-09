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

What are the common load balancing algorithms?
Common load balancing algorithms include:

Round-Robin: Evenly distributes requests in a rotating order.
Least Connections: Chooses the server with the fewest active connections.
IP Hashing: Uses client IP to consistently assign a server.
Weighted Round-Robin: Distributes based on server capacities.
Random: Assigns requests to a randomly selected server.

2. How does the round-robin algorithm distribute requests among servers?
Round-robin cycles through servers sequentially, assigning each incoming request to the next server in line. 
After reaching the last server, it loops back to the first, ensuring an even distribution of traffic 
regardless of server load or response time.

3. How does load balancing contribute to the scalability and efficiency of a distributed system?
Load balancing prevents overload on any single server, allowing requests to be handled smoothly across multiple servers. 
This improves system responsiveness, ensures high availability, allows for horizontal scaling, 
and optimizes resource utilization—key factors for efficient, scalable distributed systems.



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

