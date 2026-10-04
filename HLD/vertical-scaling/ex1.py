# Ex 1: Simulate increasing server capacity

server_capacity = 100
requests = 80

print("Server capacity:",server_capacity)
print("Incoming requests:",requests)

if requests <= server_capacity:
    print("Server can handle the requests")
else:
    print("Server is overloaded")

#Upgrade the server

server_capacity = 200
print("\nAfter vertical scaling:")
print("New server capacity:",server_capacity)

if requests <= server_capacity:
    print("Server can now handle the requests")
else:
    print("Server is still overloaded")    



