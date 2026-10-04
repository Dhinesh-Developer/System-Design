# weighted load balancing

# suppose:
# Server 1 = powerful
# Server 2 = medium
# Server 3 = weak

servers = {
    "server-1": 3,
    "server-2": 1,
    "server-3": 2
}

server_list = []

for server, weight in servers.items():
    server_list.extend([server] * weight)
    
print("Load balancing pattern:")

requests = 12

for i in range(requests):
    server = server_list[i % len(server_list)]
    print(f"Request {i+1} -> {server}")

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/load-balancing$ python3 weighted-load-balancing.py
# Load balancing pattern:
# Request 1 -> server-1
# Request 2 -> server-1
# Request 3 -> server-1
# Request 4 -> server-2
# Request 5 -> server-3
# Request 6 -> server-3
# Request 7 -> server-1
# Request 8 -> server-1
# Request 9 -> server-1
# Request 10 -> server-2
# Request 11 -> server-3
# Request 12 -> server-3

# Server 1 receives more traffic because it has a higher weight.