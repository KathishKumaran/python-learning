def minmax(items):
  return min(items),max(items)
lower,upper=minmax([21,4,5,7,23])
print(lower)
print(upper)

# nested tuple
(a,(b,(c,d)))=(1,(2,(3,4)))
print(a)
print(b)
print(c)
print(d)

# swap
e='ball'
f='cat'
e,f=f,e
print(f)
print(e)

print(tuple([3,5,6,7,3]))
print(tuple('congratulations'))
print(5 in (1,2,3,4,5,6,7))
print(5 not in (5,6,7,8))