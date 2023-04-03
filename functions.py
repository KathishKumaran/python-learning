def square(x):
   return x * x
print(square(6))

def launch():
  print('hello')
launch()

def odd_or_even(n):
  if n%2==0:
    print('even')
  print('odd')
odd_or_even(5)

def nth_root(r,n):
   return r ** (1/n)
# print(nth_root(5,0.5))

def ordinal_suffix(value):
  s=str(value)
  if s.endswith('11'):
    return 'th'
  if s.endswith('12'):
    return 'td'
  if s.endswith('13'):
    return 'gh'
# print(ordinal_suffix(113))

def ordinal(value):
  return str(value)
# print(ordinal(613))

def display_nth_root(r,n):
  root=nth_root(r,n)
  message='The'+ ordinal(n) + " is there " \
  + str(r)+" yes "+ str(root)
  print('message',message)
display_nth_root(5,0.5)