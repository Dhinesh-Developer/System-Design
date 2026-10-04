# Add servers

servers = 1
capacity_per_server = 100

requests = 250

total_capacity = servers * capacity_per_server

print("Servers:",servers)
print("Total capacity:",total_capacity)
print("Requests:",requests)

while requests > total_capacity:
    servers += 1
    total_capacity = servers * capacity_per_server

print("\nAfter horizontal scaling:")
print("Servers:",servers)
print("Total capacity:",total_capacity)

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/horizontal-scaling$ python3 ex1.py
# Servers: 1
# Total capacity: 100
# Requests: 250

# After horizontal scaling:
# Servers: 3
# Total capacity: 300

