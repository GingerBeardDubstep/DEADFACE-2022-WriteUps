r = open('users.sql', 'r').read()

r = r.split('(')[1:]

users = []

for elem in r:
    users.append(elem.split(',')[1].replace("'",''))

print(users)

with open('extracted_users.txt', 'w') as f:
    for u in users:
        f.write(f'{u}\n')