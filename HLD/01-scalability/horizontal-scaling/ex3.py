# Add server when traffic increases

servers = 2
capacity_per_server = 100

traffic = [100,150,180,250,400,550]

for request in traffic:
    total_capacity = servers * capacity_per_server

    print("\nTraffic:",request)
    print("Servers:",servers)
    print("Capacity:",total_capacity)

    if request > total_capacity:
        servers += 1
        print("Adding a server...")
    else:
        print("Capacity is sufficient")    

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/horizontal-scaling$ python3 ex3.py

# Traffic: 100
# Servers: 2
# Capacity: 200
# Capacity is sufficient

# Traffic: 150
# Servers: 2
# Capacity: 200
# Capacity is sufficient

# Traffic: 180
# Servers: 2
# Capacity: 200
# Capacity is sufficient

# Traffic: 250
# Servers: 2
# Capacity: 200
# Adding a server...

# Traffic: 400
# Servers: 3
# Capacity: 300
# Adding a server...

# Traffic: 550
# Servers: 4
# Capacity: 400
# Adding a server...

