
import time

start = time.time()
print("TRACE: request started")
time.sleep(0.1)

print("TRACE: user service")
time.sleep(0.2)

print("TRACE: order service")
time.sleep(0.3)

print("TRACE: payment service")
total = time.time() - start

print("TRACE: total time:",total)

# TRACE: request started
# TRACE: user service
# TRACE: order service
# TRACE: payment service
# TRACE: total time: 0.6004724502563477
