a={'one':'1','two':'2','three':'3','four':'4'}
def convert(s):
  """ Convert a string to a integer"""
  try:
    number=''
    for i in s:
      number += a[i]
    x=int(number)
    print(f'success! x={x}')
  except KeyError:
    print('failed in keyerror')
    x=-1
  except TypeError:
    print('failed in typeerror')
    x=-1
  print (x)
convert('one'.split())
convert('five'.split())
convert(5)



