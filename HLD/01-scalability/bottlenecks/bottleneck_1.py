# Find the slowest component


components = {
    "Load Balancer": 10000,
    "Application Server": 5000,
    "Database": 1000,
    "Cache": 15000
}

bottleneck = min(
    components,
    key=components.get
)

print("Component capacities:")

for component, capacity in components.items():
    print(component, ":", capacity, "requests/sec")

print("\nBottleneck:", bottleneck)
print("Capacity:", components[bottleneck])

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/bottlenecks$ python3 bottleneck_1.py
# Component capacities:
# Load Balancer : 10000 requests/sec
# Application Server : 5000 requests/sec
# Database : 1000 requests/sec
# Cache : 15000 requests/sec

# Bottleneck: Database
# Capacity: 1000