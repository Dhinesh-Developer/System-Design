requests = 0

def handle_request():
    global requests

    requests += 1
    print("Total requests:",requests)

handle_request()
handle_request()
handle_request()    

# Total requests: 1
# Total requests: 2
# Total requests: 3

