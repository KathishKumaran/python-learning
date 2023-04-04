a='he is good in all the works and he is such a wonderfull person to speak'.split()

del a[5]
print(a)
a.remove('is')
print(a)

i=a.index('such')
del a[i]
print(a)
