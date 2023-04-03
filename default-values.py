# Mutable default values

def add(menu=[]):
  menu.append('ten')
  return menu
numbers=['one','two']
print(add(numbers))
print(add())
print(add())
print(add())

# Immutable default values

def addition(menu=None):
  if menu is None:
    menu=[]
  menu.append('one')
  return menu
print(addition())
print(addition())
print(addition())