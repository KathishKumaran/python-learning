def banner(message,border="_"):
  line=border * len(message)
  print(line)
  print(message)
  print(line)
banner("blue")
banner("tree, plants","*")
banner(border='+',message="geen")
banner('white, red',border="^")
