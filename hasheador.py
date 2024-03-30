import hashlib

password = input('Introduce la pass a hashear: ')
hash_password = hashlib.sha1(password.encode()).hexdigest()

print (f'La pass hasheada es: {hash_password}')

# Esto es un comentario