t=('india',4.57,45)
print(t)
print(t[1])
print(len(t))

# iterate using for loop
for items in t:
  print(items)

# concatenate using + operator
print(t+(3.88,89))

# repeat using * operator
print(t*2)

# nested tuples
a=((1,2),(3,4),(5,6),(7,8))
print(a[1][1])

# single element tuple
a=(12,)
print(a)

# empty tuple
a=()
print(a)

def minmax(items):
  return min(items),max(items)
print(minmax([21,4,5,7,23]))