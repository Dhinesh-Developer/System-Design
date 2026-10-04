# stateless server

class Server:
    def request(self, username):
        print(f"Request handled for {username}")

server1 = Server()
server2 = Server()

server1.request("Dhinesh")
server2.request("Dhinesh")

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/stateless-stateful-servies$ python3 stateless-server.py
# Request handled for Dhinesh
# Request handled for Dhinesh