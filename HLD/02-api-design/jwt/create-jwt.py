# create JWT with python

# Install:
#     pip install PyJWT

import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "change-this-secret"

payload = {
    "sub":"101",
    "role":"user",
    "exp":datetime.now(timezone.utc) + timedelta(minutes=30)
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    "HS256"
)

print(token)

# dhinesh@Arise:~/Desktop/System-Design$ /usr/bin/python3 /home/dhinesh/Desktop/System-Design/HLD/02-api-design/jwt/create-jwt.py
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDEiLCJyb2xlIjoidXNlciIsImV4cCI6MTc5MTE2MDA4Nn0.5o5oc9E-AvHurqTTAED3bfm0FbsRiw8Rr0QLLR3g6Bc