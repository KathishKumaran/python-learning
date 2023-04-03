import math

a= 'the age of {0} is {1}'.format('jim',20)
print(a)

b='he is {0} in {1}. god is {0} all the {2}'.format('goog','all','time')
print(b)

c='he is {} in {} our {}'.format('good','all','situation')
print(c)

d='Curent position {latitude} {longitude}'.format(latitude='30N',longitude='29E')
print(d)

e='position x={pos[0]},y={pos[1]},z={pos[2]}'.format(pos=(23,34,56))
print(e)

f='math constants: pi={m.pi},e={m.e}'.format(m=math)
print(f)

g='math constants: pi={m.pi:.3f},e={m.e:.2f}'.format(m=math)
print(g)

value=4*20
h='the value is {value}'.format(value=value)
print(h)