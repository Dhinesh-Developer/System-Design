# CPU scaling simulation

class Server:
    def __init__(self, cpu_cores):
        self.cpu_cores = cpu_cores

    def capacity(self):
        return self.cpu_cores * 100

server = Server(2)

print("CPU cores: ",server.cpu_cores)
print("Capacity: ",server.capacity(), "requests")

#vertical scaling
server.cpu_cores = 8

print("\nAfter scaling:")
print("CPU cores:",server.cpu_cores)
print("Capacity:",server.capacity(),"requests")

# CPU cores:  2
# Capacity:  200 requests

# After scaling:
# CPU cores: 8
# Capacity: 800 requests

