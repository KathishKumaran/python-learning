def lucas():
  yield 2
  a=1
  b=2
  while True:
    yield b
    a,b=b,a+b

for x in lucas():
  print(x)