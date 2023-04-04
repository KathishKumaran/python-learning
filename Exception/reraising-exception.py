
import sys

a={'one':'1','two':'2','three':'3','four':'4'}
def convert(s):
  """ Convert a string to a integer"""
  try:
    number=''
    for i in s:
      number += a[i]
    x=int(number)
    print(f'success! x={x}')
  except (KeyError,TypeError) as e:
    print(f'failed :{e!r}',file=sys.stderr)
    x=-1
    raise
  print (x)
# convert('one'.split())


from math import log

def string_log(s):
  v=convert(s)
  return log(v)

string_log('woe!'.split())
