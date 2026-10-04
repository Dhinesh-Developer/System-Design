
servers = ["server-1","server-2","server-3"]

requests = 9

for i in range(requests):
    server = servers[i% len(servers)]

    print(f"Requests {i+1} -> {server}")

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/load-balancing$ python3 round-robin.py
# Requests 1 -> server-1
# Requests 2 -> server-2
# Requests 3 -> server-3
# Requests 4 -> server-1
# Requests 5 -> server-2
# Requests 6 -> server-3
# Requests 7 -> server-1
# Requests 8 -> server-2
# Requests 9 -> server-3
