def gen():
  print('its a')
  yield 1
  print('its b')
  yield 2
  print('its c')
  yield 3
  print('about to return')

result=gen()
print(next(result))
print(next(result))
print(next(result))
print(next(result))