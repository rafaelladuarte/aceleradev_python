import jwt


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        return jwt.decode(token, 'acelera', algorithms=['HS256'])
    except jwt.InvalidSignatureError:
<<<<<<< HEAD
        return {'error': 2}
=======
        return {'error': 2}
>>>>>>> 4a3abaaf20bdb6f66f0bc7a66227e8795f67e5cc
