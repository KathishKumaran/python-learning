colors=dict(one='green',two='red',three='yellow')
for key in colors:
  print(f'{key}====>{colors[key]}')

  # for only values
  for value in colors.values():
    print(value)

# keys only
  for key in colors.keys():
    print(key)

# key and values
  for key,value in colors.items():
    print(f'{key}======>{value}')

