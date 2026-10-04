# Demonstrate why adding server's doesn't always help

application_servers = 10
app_capacity = 500

database_capacity = 1000

total_app_capacity = (
    application_servers * app_capacity
)

system_capacity = min(total_app_capacity, database_capacity)

print("Application capacity: ")
print(total_app_capacity, "requests/sec")

print("Database capacity: ")
print(database_capacity, "requests/sec")

print("Actual System capacity: ")
print(system_capacity, "requests/sec")


# Even though:
# 10 × 500 = 5000 RPS

# the database only supports:
# 1000 RPS

# Therefore:
# Actual system capacity = 1000 RPS
# This is a very important HLD lesson.

# -------------------------------------
# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/bottlenecks$ python3 bottleneck_3.py
# Application capacity: 
# 5000 requests/sec
# Database capacity: 
# 1000 requests/sec
# Actual System capacity: 
# 1000 requests/sec