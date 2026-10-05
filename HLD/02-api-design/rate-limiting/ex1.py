import time

requests = []

def allow_request():
    current_time = time.time()

    # Remove requests older than 60 seconds
    recent_requests = [
        t for t in requests
        if current_time - t < 60
    ]

    requests.clear()
    requests.extend(recent_requests)

    if len(requests) >= 5:
        return False

    requests.append(current_time)
    return  True

for i in range(10):
    print(i+1, allow_request())



