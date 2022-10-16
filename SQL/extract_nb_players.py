r = open('users.sql', 'r').read()

r = r.split('(')[1:]

print(len(r))