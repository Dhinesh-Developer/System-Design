# Auto vertical scaling simulation

server_capacity = 100

traffic = [50, 80, 120, 180, 250]

for request in traffic:

    print("\nIncoming requests:",request)
    print("Current capacity:",server_capacity)

    if request > server_capacity:
        print("Server overloaded!!")

        #Increase server capacity
        server_capacity *= 2

        print("Vertical scaling performed")
        print("New capacity:",server_capacity)

    else:
        print("Server is healthy")    


# dhinesh@Arise:~/Desktop/System-Design/HLD/vertical-scaling$ python3 ex3.py

# Incoming requests: 50
# Current capacity: 100
# Server is healthy

# Incoming requests: 80
# Current capacity: 100
# Server is healthy

# Incoming requests: 120
# Current capacity: 100
# Server overloaded!!
# Vertical scaling performed
# New capacity: 200

# Incoming requests: 180
# Current capacity: 200
# Server is healthy

# Incoming requests: 250
# Current capacity: 200
# Server overloaded!!
# Vertical scaling performed
# New capacity: 400