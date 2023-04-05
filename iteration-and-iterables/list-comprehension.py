words='My name is kathish'.split()
print(words)

a=[len(word) for word in words]
print(a)


# similar to
# lengths=[]
# for word in words:
#   lengths.append(len(word))
# print(lengths)

from math import factorial

f=[len(str(factorial(x))) for x in range(20)]
print(f)