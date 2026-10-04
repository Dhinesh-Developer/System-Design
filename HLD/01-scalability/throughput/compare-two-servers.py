# compare two servers:

server_a = {
    "name":"Server A",
    "requests": 5000,
    "time": 10
}

server_b = {
    "name":"Server B",
    "requests": 8000,
    "time": 10
}

throughput_a = (server_a["requests"]/ server_a["time"])
throughput_b = (server_b["requests"]/ server_b["time"])

print(server_a["name"],":",throughput_a,"RPS")
print(server_b["name"],":",throughput_b,"RPS")

# Server A : 500.0 RPS
# Server B : 800.0 RPS
