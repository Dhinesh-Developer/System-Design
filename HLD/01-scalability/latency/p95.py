# calculate P95 latency
# this is more useful in real system design

latencies = [
    20, 22, 25, 27, 30,
    32, 35, 40, 40, 200
]

latencies.sort()

index = int(0.95* len(latencies)) - 1
p95 = latencies[index]

print("Latencies:",latencies)
print("P95 latency:", p95, "ms")

# Latencies: [20, 22, 25, 27, 30, 32, 35, 40, 40, 200]
# P95 latency: 40 ms

