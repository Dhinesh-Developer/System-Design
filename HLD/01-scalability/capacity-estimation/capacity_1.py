# Daily users -> request

users = 100_000
requests_per_user = 10

daily_requests = (
    users * requests_per_user
)

print("Daily requests:",daily_requests)

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/capacity-estimation$ python3 capacity_1.py
# Daily requests: 1000000


# 100,000 users
# 10 requests/user/day
# Daily requests: 1000000