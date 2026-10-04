import time

# servers
servers = {
    "Server-1":0,
    "Server-2":0,
    "Server-3":0
}

#Database
database_capacity = 5

#requests
requests = 15

start = time.perf_counter()

for request in range(1, requests+1):
    # Load balancing
    server_names = list(servers.keys())

    selected_servers = server_names[(request-1) %len(server_names)]
    servers[selected_servers] += 1

    print(f"Request {request} -> {selected_servers}")
    #simulate processing
    time.sleep(0.01)

end = time.perf_counter()

# Metrics

total_time = end - start
throughput = requests/total_time

average_latency = (total_time/requests)

print("\n-----------------")
print("SYSTEM RESULTS")
print("--------------")

print("Requests:",requests)
print("Servers:",servers)
print("Throughput:",round(throughput,2),"requests/sec")
print("Average latency:",round(average_latency*1000,2),"ms")
print("\nRequest handled:")

for server,count in servers.items():
    print(server,":",count)

# ----------------------------------output ---------------------
# Request 1 -> Server-1
# Request 2 -> Server-2
# Request 3 -> Server-3
# Request 4 -> Server-1
# Request 5 -> Server-2
# Request 6 -> Server-3
# Request 7 -> Server-1
# Request 8 -> Server-2
# Request 9 -> Server-3
# Request 10 -> Server-1
# Request 11 -> Server-2
# Request 12 -> Server-3
# Request 13 -> Server-1
# Request 14 -> Server-2
# Request 15 -> Server-3

# -----------------
# SYSTEM RESULTS
# --------------
# Requests: 15
# Servers: {'Server-1': 5, 'Server-2': 5, 'Server-3': 5}
# Throughput: 98.29 requests/sec
# Average latency: 10.17 ms

# Request handled:
# Server-1 : 5
# Server-2 : 5
# Server-3 : 5
