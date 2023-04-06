class RefrigeratorRaider:

  def open(self):
    print('open fridge door')

  def take(self,food):
    print(f'finding {food}')
    if food=='deep fried pizza':
      raise RuntimeError('Health warning')
    print(f'Taking {food}')

  def close(self):
    print('close fridge door')

def raid(food):
  r=RefrigeratorRaider()
  r.open()
  r.take(food)
  r.close()

print(raid('bacon'))
