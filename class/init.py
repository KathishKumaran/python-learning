class Flight:

  def __init__(self,number):
    self._number=number

  def number(self):
    return self._number

f=Flight('SN06')
print(f._number)
print(f.number())
print(Flight.number(f))