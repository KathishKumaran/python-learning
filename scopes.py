# Before

count=1
def show():
  print(count)

def set_value(c):
   count=c
   print(count)

show()
set_value(5)
show()

# After

count=1
def show():
  print('-------',count)

def set_value(c):
   count=c
   print('-----------',count)

show()
set_value(5)
show()