r = open('term_courses.sql', 'r').read()

values = r.split('(')
values = [a.replace('),', '').replace(')', '') for a in values]
values = [','.join(a.split(',')[1:-1]) for a in values]
values = [a for a in values if ',2' in a]
print(len(set(values)))