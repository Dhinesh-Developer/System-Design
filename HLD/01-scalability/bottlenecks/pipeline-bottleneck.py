# pipeline bottleneck

stages = [
    ("API", 5000),
    ("Business Logic", 3000),
    ("Database", 800),
    ("Response", 4000)
]

system_capacity = min(
    capacity for name, capacity in stages
)

print("System maximum capacity:", system_capacity, "requests/sec")

for name, capacity in stages:
    if capacity == system_capacity:
        print("Bottleneck:",name)


# The entire pipeline is limited by:
# Database = 800 RPS

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/bottlenecks$ python3 pipeline-bottleneck.py
# System maximum capacity: 800 requests/sec
# Bottleneck: Database