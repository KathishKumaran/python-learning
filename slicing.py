a=[2,4,6,8,9,7,5]
print(a[1:-1])
print(a[2:6])
print(a[3:])
print(a[:4])
print(a[:])

b=a
print(b)
print(b is a)

c=b[:]
print(c)
print(c is b)
