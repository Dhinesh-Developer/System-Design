import redis

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

client.set("name","Dhinesh")
value = client.get("name")
print("Value:",value)

# (venv) dhinesh@Arise:~/Desktop/System-Design/HLD/03-caching/redis$ p
# ython3 test.py
# Value: Dhinesh