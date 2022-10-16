import hashlib

a = hashlib.sha512(open('darkangel-crypt-03.exe', 'rb').read())

print(f'Sha512 hash : {a.hexdigest()}\nFlag to validate : flag{"{"}{a.hexdigest()[:8] + a.hexdigest()[-8:]}{"}"}')