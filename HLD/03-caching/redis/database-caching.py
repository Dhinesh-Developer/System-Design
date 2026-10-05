import time

database = {
    1:{
        "name":"Dhinesh",
        "age":21
    }
}

cache = {}

def get_user(user_id):
    #check cache
    if user_id in cache:
        print("CACHE HIT")
        return cache[user_id]
    print("CACHE MISS")

    #Database
    time.sleep(1)
    user = database[user_id]

    # Store in cache
    cache[user_id] = user
    return user

print(get_user(1))
print(get_user(1))
    
