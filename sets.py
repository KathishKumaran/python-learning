a={1,45,76,87,98,4,23}
print(a)

b=set([32,45,76,12,23,67])
print(b)

# iteration
for i in a:
  print(i)

print(32 in b)
print(76 not in b)

# add
a.add(12)
print(a)

# update
b.update([2,3])
print(b)

# remove
b.remove(76)
print(b)

# discard
b.discard(23)
print(b)

# copy
e=b.copy()
print(e)


