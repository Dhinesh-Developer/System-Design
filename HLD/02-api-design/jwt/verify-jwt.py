import jwt


SECRET_KEY = "change-this-secret"


def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except jwt.ExpiredSignatureError:

        return {
            "error": "Token expired"
        }

    except jwt.InvalidTokenError:

        return {
            "error": "Invalid token"
        }

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDEiLCJyb2xlIjoidXNlciIsImV4cCI6MTc5MTE2MDA4Nn0.5o5oc9E-AvHurqTTAED3bfm0FbsRiw8Rr0QLLR3g6Bc"
decoded = verify_token(token)

print(decoded)

# dhinesh@Arise:~/Desktop/System-Design$ /usr/bin/python3 /home/dhinesh/Desktop/System-Design/HLD/02-api-design/jwt/verify-jwt.py
# {'sub': '101', 'role': 'user', 'exp': 1791160086}