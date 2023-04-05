a=['one','two','three','four']
b=iter(a)
c=next(b)
print(c)
d=next(b)
print(d)


def first(a):
  b=iter(a)
  try:
    c=next(b)
    print(c)
  except StopIteration:
    raise ValueError('a is empty')
first(['one','two','three','four'])
first({'one','two','three','four'})
# first(set())                               ValueError