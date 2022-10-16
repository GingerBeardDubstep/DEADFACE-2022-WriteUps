# Note : The id of the student role is : 1 (cf line 233 in sql file)
total_users = 2400 # see extract_palyers.py

r = open('role_assigned.sql', 'r').read()

print(len(r.split('(')) - len(r.split(',1)'))) # nb_total users - nb_students