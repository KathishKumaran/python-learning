class Aircraft:

  def __init__(self,registration,model,num_rows,num_seats_per_row):
    self._registration=registration
    self._model=model
    self._num_rows=num_rows
    self._num_seats_per_row=num_seats_per_row

  def registration(self):
    return self._registration

  def model(self):
    return self._model

  def seating_plan(self):
    return (range(1,self._num_rows+1),'ABCDEFGHJK'[:self._num_seats_per_row])

a=Aircraft('G-EUPT','Airbus 0ES',num_rows=22,num_seats_per_row=7)
print(a.registration())
print(a.model())
print(a.seating_plan())

