
a={'one':'1','two':'2','three':'3','four':'4'}

def convert(s):
  number=''
  for i in s:
    number += a[i]
  x=int(number)
  return x

print(convert('one two three four'.split()))

# print(convert('around two three'.split()))      kerError
