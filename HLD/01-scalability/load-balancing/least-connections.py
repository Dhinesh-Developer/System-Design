servers = ["server-1","server-2","server-3"]

for request in range(5):

    selected_server = min(servers,key=servers.get)
    print(f"Request {request+1} -> {selected_server}")
    servers[selected_server] += 1

# min(..., key=servers.get) finds the server with the fewest active connections.