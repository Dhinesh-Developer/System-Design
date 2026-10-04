# Measure python operation latency

import time

start = time.perf_counter()

#simulate work
time.sleep(0.2)
end = time.perf_counter()

latency = end - start

print("Latency:",round(latency * 1000,2), "ms")
# Latency: 200.1 ms
