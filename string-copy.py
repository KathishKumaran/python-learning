a=[[1,2],[3,4]]
b=a[:]
print(b)
print(a is b)
print(a==b)

print(a[0]==b[0])

a[1].append(5)
print(a)

s=[[1,3]]*4
print(s)
s[2].append(6)
print(s)