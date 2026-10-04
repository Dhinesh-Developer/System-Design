# Distribute requests across servers

servers = ["server-1","server-2","server-3"]

requests = 10

for request in range(1, requests+1):
    server = servers[(request-1) % len(servers)]

    print(f"Request {request} -> {server}")
    

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/horizontal-scaling$ python3 ex2.py
# Request 1 -> server-1
# Request 2 -> server-2
# Request 3 -> server-3
# Request 4 -> server-1
# Request 5 -> server-2
# Request 6 -> server-3
# Request 7 -> server-1
# Request 8 -> server-2
# Request 9 -> server-3
# Request 10 -> server-1
