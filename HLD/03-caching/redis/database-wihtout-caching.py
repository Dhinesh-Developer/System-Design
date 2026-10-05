import time

def database():
    print("Database query...")
    time.sleep(1)

    return{
        "name":"Dhinesh",
        "age":21
    }

start = time.time()
res = database()
end = time.time()

print("Result: ",res)
print("Time:",round(end-start,2),"seconds")


