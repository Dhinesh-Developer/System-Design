import uuid

trace_id = str(uuid.uuid4())
print("trace_id:",trace_id)

print("Calling user service")
print("trace_id:",trace_id)

print("Calling order service")
print("trace_id:",trace_id)

print("Calling payment service")
print("trace_id:",trace_id)

# trace_id: c176127a-bf70-41e4-9c43-0bdb819cd6b2
# Calling user service
# trace_id: c176127a-bf70-41e4-9c43-0bdb819cd6b2
# Calling order service
# trace_id: c176127a-bf70-41e4-9c43-0bdb819cd6b2
# Calling payment service
# trace_id: c176127a-bf70-41e4-9c43-0bdb819cd6b2