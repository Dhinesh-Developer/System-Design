import time

number_of_requests = 100_000

start = time.time()

for _ in range(number_of_requests):
    # simulate processing a request
    res = 10+20
end = time.time()

duration = end-start

rps = number_of_requests / duration

print("Requests:",number_of_requests)
print("Time:",round(duration,4),"seconds")
print("RPS:",round(rps,2))


# Requests: 100000
# Time: 0.009 seconds
# RPS: 11094868.27