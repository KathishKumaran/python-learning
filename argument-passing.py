a=[1,2,3,4]
def modify(b):
  b.append(23)
  print("b=",b)
modify(a)
print("a=",a)

# Replacing arguments Values
c=[1,2,3,4]
def modify(d):
  d=[33,44,55]
  print("d=",d)
modify(a)
print("c=",c)

# Mutable arguments
def replace_contents(e):
  e[0]=23
  e[1]=56
  e[2]=67
  print("e=",e)
f=[1,4,5,6]
replace_contents(f)
print("f=",f)

# Return semantics
def f(d):
  return d
c=[1,2,3]
e=f(c)
print("e----------",e)
print(c is e)