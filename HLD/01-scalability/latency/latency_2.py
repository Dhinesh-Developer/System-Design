# Measure multiple requests.

import time
latencies = []

for i in range(5):
    start = time.perf_counter()

    #simulate request
    time.sleep(0.05 + i * 0.02)

    end = time.perf_counter()
    latency = (end-start) * 1000

    latencies.append(latency)

print("Latencies:")

for latency in latencies:
    print(round(latency,2), "ms")

average = sum(latencies)/len(latencies)

print("\nAverage latency:",round(average,2),"ms")

# Latencies:
# 50.25 ms
# 70.19 ms
# 90.13 ms
# 110.08 ms
# 130.11 ms

# Average latency: 90.15 ms