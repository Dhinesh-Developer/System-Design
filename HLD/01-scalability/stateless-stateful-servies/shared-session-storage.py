# stateless shared storage

# Server 1 ─┐
# Server 2 ─┼── Redis
# Server 3 ─┘

redis = {}

class Server:
    def login(self, user):
        # store session outside server
        redis[user] = "logged_in"

    def check_login(self,user):
        return redis.get(user) == "logged_in"

server1 = Server()
server2 = Server()

server1.login("Dhinesh")

print("Server 1:",server1.check_login("Dhinesh"))
print("Server 2:",server2.check_login("Dhinesh"))

# dhinesh@Arise:~/Desktop/System-Design/HLD/01-scalability/stateless-stateful-servies$ python3 shared-session-storage.py
# Server 1: True
# Server 2: True