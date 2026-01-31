# JWT = Header + Payload + Signature
import time
import jwt

secret_key = "secret_key"

def issue_jwt(expiration, user_id, role):
    header = {
        "alg": "HS256",
        "typ": "JWT",
    }

    payload = {
        "user_role": role,
        "user_id": user_id,
        "exp": time.time() + expiration,
    }

    token = jwt.encode(payload, secret_key, algorithm= header['alg'], headers=header)
    return token

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, secret_key, ['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"

token = issue_jwt(5,  1, "user")
print(token)
time.sleep(3)
print(verify_jwt(token))















#==========================How data signature works generally===================#

# from hashlib import sha256
#
# secret_key = "secret_key" #digital sign key
#
# def get_signature(data):
#     return sha256((data+secret_key).encode()).hexdigest()
#
# def sign(data):
#     signature = get_signature(data)
#     message= data + "." + signature
#     return message
#
#
#
# def unsign(message):
#     data, signature = message.split(".")
#     if signature != get_signature(data):
#         raise ValueError("Invalid signature")
#     return data
#
#
# message = "Total: 200"
# signed_message = sign(message)
# print(signed_message)
# hijacked_msg = signed_message.replace("200", "100")
# print(signed_message)
# print(unsign(signed_message))
