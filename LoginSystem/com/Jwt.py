from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time

secret_key = ''
auth_salt = ''

def genToken(expires, payload):
    s = Serializer(
        secret_key=secret_key,
        salt=auth_salt,
        expires_in=expires)
    return s.dumps(payload).decode()

def parseToken(token):
    s = Serializer(secret_key=secret_key, salt=auth_salt)
    return s.loads(token)

if __name__ == '__main__':
    token = genToken(10, {'uid':'123', 'username':'cck'})
    print(token)
    print(parseToken(token))