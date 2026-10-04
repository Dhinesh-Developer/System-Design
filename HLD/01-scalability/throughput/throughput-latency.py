# Throughput vs Latency

import time
requests = 200

start = time.perf_counter()

for _ in range(requests):
    #simulate processing
    time.sleep(0.01)

end = time.perf_counter()
total_time = end-start

throughput = requests/total_time

average_latency = (total_time/requests)

print("Total time:",round(total_time,2),"seconds")
print("Throughput:",round(throughput,2),"requests/sec")
print("Average latency:",round(average_latency * 1000,2),"ms")

# Total time: 2.03 seconds
# Throughput: 98.63 requests/sec
# Average latency: 10.14 ms
