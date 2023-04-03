names_ages=[('raja',23),('siva',34),('mari',54),('rajesh',34)]
a=dict(names_ages)
print(a)

b=dict(a='alpha',b='beta',c='gamma')
print(b)

c=b.copy()
print("-----------",c)

e=dict(c)
print('e---',e)
d=dict(d='dog',e='elephant')
e.update(d)
print(e)

e.update(d='domestic',f='fox')
print('e----->',e)