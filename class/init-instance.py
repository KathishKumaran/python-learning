class Flight:

  def __init__(self,number):
    if not number[:2].isalpha():
      raise ValueError(f"no airline code in '{number}'")
    if not number[:2].isupper():
      raise ValueError(f"Invalid airline code '{number}'")
    if not (number[2:].isdigit() and int(number[2:])<=9999):
      raise ValueError(f"invalid route number '{number}'")
    self._number=number

  def number(self):
    return self._number

f=Flight('SN060')
print(f._number)
# g=Flight('060')
# print(g._number)
# h=Flight('sn060')
# i=Flight('snabd')
# print(h._number)
# print(i._number)