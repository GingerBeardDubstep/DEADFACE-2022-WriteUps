user_id = 1440

r = open('passwords.sql', 'r').read()

r = r.split('(')[1:]

for l in r:
    if str(user_id) in l.split(',')[0]:
        print(l.split(',')[1].replace("'",''))