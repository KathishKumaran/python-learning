a=4
print(id(a))

b=5
print(id(b))

b=a
print(id(a)==id(b))

t=10
print(id(t))
t +=2
print(id(t))