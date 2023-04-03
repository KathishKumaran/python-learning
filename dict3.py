from pprint import pprint as pp

z={'H':1,'J':3,'K':7,'D':8}
print(z)

# delete
del z['K']
print(z)

h={'H':[1,3,4,7],'J':3,'K':7,'D':8}
print(h)
h['H'] += [8,9,0]
print(h)
h['N'] =[4,6,8]
print(h)

from pprint import pprint as pp

pp(h)


