import time

start = time.time()
time.sleep(0.5)
end = time.time()

latency = end - start
print("Latency:",latency,"seconds")

