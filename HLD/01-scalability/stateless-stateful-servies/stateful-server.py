# stateful server

class Server:
    def __init__(self):
        self.user_sessions = {}

    def login(self, user):
        self.user_sessions[user] = True

    def check_login(self,user):
        return self.user_sessions.get(user, False)

server1 = Server()
server1.login("Dhinesh")

print("Server 1:", server1.check_login("Dhinesh"))

server2 = Server()
print("Server 2:",server2.check_login("Dhinesh"))

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/stateless-stateful-servies$ python3 stateful-server.py
# Server 1: True
# Server 2: False

# Why?
# Because session information exists only inside Server 1.