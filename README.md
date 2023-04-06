# String
* Can be enclosed in a single quotes or double quotes.
* \ (backslash) can used to escape single quotes

```
# single quotes
a='he is a good cricketer'
print(a)

# double quotes
b="he is a good person"
print(b)

# \ to escape single quotes
c="he doesn\'t like this"
d='he doesn\'t like this'
print(c)
print(d)
```

# Srings with Newlines
> Multiline strings: Spread the literal across multiple lines

```
# Multiline strings

a="""This
    is new
    look"""
print(a)

b="This is\nnew\nlook"
print(b)

c='''This
    is new
    look'''
print(c)

d='This is\nnew\nlook'
print(d)
```

> Escape Sequences: Embed escape sequences in a single line literals

```
# Escape Sequence

a="he is a \' and powerfull preacher"
print(a)

b="he is a \" and powerfull preacher"
print(b)

c="he is a \" and \' powerfull preacher"
print(c)

d="he is a \" and \" powerfull preacher"
print(d)

e='he is a \" and \' powerfull preacher'
print(e)

f='he is \\ good'
print(f)
```

## Universal Newlines
* Python translates \n to the appropriate newline sequence for our platform

## String Features
* Python comes to the rescue with its raw strings. Raw strings doesn't support any escape sequences.
* To create a raw string, prefix the openning quote with the lowercase r
* We can use the string constructor to create string representation of other types such as integers or floats

```
# String Features

a=r'C:\Users\Project\Lutosa'
print(a)

b=str(477)
print(b)

g=4

c='tamil nadu'
d=c[4]
print(d)
e=type(c[4])
print(e)
print(type(b))
print(type(g))

f="cat"
h=f.capitalize()
print(h)
print(f)
```

## Unicode in Strings
* str is unicode
* By default Python3 source encoding is UTF-8
* \u ,\xe5 ,\345

```
# unicode

a='\u00e6'
b='\xf8'
c='\345'

print(a)
print(b)
print(c)
```

## Bytes
* Data type for sequence of bytes
* Raw binary data
* Fixed-width single-byte encodings
* prefixed by the lowercase b

```
# Bytes

a=b'god'
print(a)
b=b'god is good'
print(b[0])
print(b[1])
print(b.split())
```

## Encode/Decode
```
# Encode/Decode

song='Have a nice day'
data=song.encode('utf8')
print(data)

result=data.decode('utf8')
print(result)
```

## List
* Python list, such as those returned by the string split method are sequence of objects
* Lists are mutable (elements can be removed or replaced or inserted or appended)

```
# List

a=[1,2,3]
print(a)
b=[]
a[1]='apple'
print(a)
b.append('orange')
print(b)
c=list('damaged')
print(c)
d=['apple',
    'ball',
    'cat',
    'dog']
print(d)
```
### output
```
[1, 2, 3]
[1, 'apple', 3]
['orange']
['d', 'a', 'm', 'a', 'g', 'e', 'd']
['apple', 'ball', 'cat', 'dog']
```

## Dict
* Dictionaries are completely fundamental to python language and are very widely used
* maps keys to values
* also known as maps or associative arrays

```
a={'a':'python','b':'python1','c':'python3'}
print(a['b'])
a['d']='python2'
print(a)
b={}
print(b)
```
### output
```
python1
{'a': 'python', 'b': 'python1', 'c': 'python3', 'd': 'python2'}
{}
```
## For-loop

```
a=['london','delhi','new york','canada']
for b in a:
   print(b)

c={'green':'34434','black':'8765','red':'5277'}
for d in c:
  print(d,c[d])

```
## output
```
london
delhi
new york
canada
green 34434
black 8765
red 5277
```
## Example:
```
from urllib.request import urlopen
story=urlopen('http://sixty-north.com/c/t.txt')
story_words=[]
story_decode_words=[]
for line in story:
   line_words=line.split()
   line_decode=line.decode('utf-8').split()
   for word in line_words:
     story_words.append(word)
   for word in line_decode:
    story_decode_words.append(word)
print(story_words)
print(story_decode_words)

```

## output
```
[b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom', b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the', b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of', b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the', b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct', b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the', b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its', b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', b'superlative', b'degree', b'of', b'comparison', b'only']
['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'Light', 'it', 'was', 'the', 'season', 'of', 'Darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'Heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']
```

## Function
* Functions are defined using the def keyword followed by the function name , an argument list in the parenthesis and a colon to start a new block.
* The code inside the function block must be intended
* We use return keyword to return a value from the function

## dunder
* our way of pronouncing special names
* Instead of "underscore underscore name underscore underscore" we will say "dunder name"
```
def square(x):
   return x * x
print(square(6))

def launch():
  print('hello')
launch()

def odd_or_even(n):
  if n%2==0:
    print('even')
  print('odd')
odd_or_even(5)

def nth_root(r,n):
   return r ** (1/n)
# print(nth_root(5,0.5))

def ordinal_suffix(value):
  s=str(value)
  if s.endswith('11'):
    return 'th'
  if s.endswith('12'):
    return 'td'
  if s.endswith('13'):
    return 'gh'
# print(ordinal_suffix(113))

def ordinal(value):
  return str(value)
# print(ordinal(613))

def display_nth_root(r,n):
  root=nth_root(r,n)
  message='The'+ ordinal(n) + " is there " \
  + str(r)+" yes "+ str(root)
  print('message',message)
display_nth_root(5,0.5)
```
## output
```
36
hello
odd
message The0.5 is there 5 yes 25.0
```

## Function

* A function is a block of code which only runs when it is called.

* You can pass data, known as parameters, into a function.

* A function can return data as a result.

## Assigning variable

```
a=2
b=4
print(a)

a=b
print(a)

a=10
print(10)
```
### output
```
2
4
10
```

## id()
* Returns a unique integer identifiers for an object that is constant for life of a object.

```
a=4
print(id(a))

b=5
print(id(b))

b=a
print(id(a)==id(b))

t=10
print(id(t))
t +=2
print(id(t))
```
### output
```
9793184
9793216
True
9793376
9793440
```
## Mutable objects

```
a=[1,2,3]
print(a)
b=a
print(b)
b[1]=5
print(b)
print(a)
print(b is a)
```
### output
```
[1, 2, 3]
[1, 2, 3]
[1, 5, 3]
[1, 5, 3]
True
```

* Python doesn't have the variables in the sense of boxes holding a value
* Python has named reference to the object

## Value Vs Identity Equality

* The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory.

```
a=[1,23,4]
b=[1,23,4]
print(a==b)
print(a is b)
```
### output
```
True
False
```

## Passing Arguments and Return Values
* Function arguments are transferred using pass-by-object-reference
* Reference to objects are copied, not the object themselves

```
a=[1,2,3,4]
def modify(b):
  b.append(23)
  print("b=",b)
modify(a)
print("a=",a)

# Replacing arguments Values
c=[1,2,3,4]
def modify(d):
  d=[33,44,55]
  print("d=",d)
modify(a)
print("c=",c)

# Mutable arguments
def replace_contents(e):
  e[0]=23
  e[1]=56
  e[2]=67
  print("e=",e)
f=[1,4,5,6]
replace_contents(f)
print("f=",f)

# Return semantics
def f(d):
  return d
c=[1,2,3]
e=f(c)
print("e----------",e)
print(c is e)
```
### output
```
b= [1, 2, 3, 4, 23]
a= [1, 2, 3, 4, 23]
d= [33, 44, 55]
c= [1, 2, 3, 4]
e= [23, 56, 67, 6]
f= [23, 56, 67, 6]
e---------- [1, 2, 3]
True
```

## function Arguments
* Arguments with default values must come after those without default values

```
def banner(message,border="_"):
  line=border * len(message)
  print(line)
  print(message)
  print(line)
banner("blue")
banner("tree, plants","*")
banner(border='+',message="geen")
banner('white, red',border="^")
```
### output
```
____
blue
____
************
tree, plants
************
++++
geen
++++
^^^^^^^^^^
white, red
^^^^^^^^^^
```

## Default Value Evaluation
* Remember that def is a statement executed at the runtime
* Default arguments are evaluated when def is executed
* immutable default value don't cause problems
* Mutable default value can cause confusing effects
* So always use immutable object for default values

```
# Mutable default values

def add(menu=[]):
  menu.append('ten')
  return menu
numbers=['one','two']
print(add(numbers))
print(add())
print(add())
print(add())

# Immutable default values

def addition(menu=None):
  if menu is None:
    menu=[]
  menu.append('one')
  return menu
print(addition())
print(addition())
print(addition())
```
### output
```
['one', 'two', 'ten']
['ten']
['ten', 'ten']
['ten', 'ten', 'ten']
['one']
['one']
['one']
```

## Python's Type System
* Dynamic typing means the type of an object reference isn't resolved untill the program is running and need not specified up front when the program is written
* Python will not generally perform implicit conversions between types

```
def add(a,b):
  return a+b
print(add(2,3))

# print(add("the sum is",12))     type error
```

## Scopes in Python

* LEGB
* L - Local
* E - Enclosing
* G - Global
* B - Built-in
* Local : inside the current function
* Enclosing : inside the enclosing function
* Global : at the top level of the module
* Built-in : in the secial builtins modules
* scopes in python do no correspond to the source code
* for-loop and the like do not introduce new nested scopes

```
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
   global count
   count=c
   print('-----------',count)

show()
set_value(5)
show()
```
### output

```
1
5
1
------- 1
----------- 5
------- 5
```

## tuple
* immutable sequences of arbitrary objects
* Tuples have the similar syntax to list

```
t=('india',4.57,45)
print(t)
print(t[1])
print(len(t))

# iterate using for loop
for items in t:
  print(items)

# concatenate using + operator
print(t+(3.88,89))

# repeat using * operator
print(t*2)

# nested tuples
a=((1,2),(3,4),(5,6),(7,8))
print(a[1][1])

# single element tuple
a=(12,)
print(a)

# empty tuple
a=()
print(a)

def minmax(items):
  return min(items),max(items)
print(minmax([21,4,5,7,23]))
```
### output

```
('india', 4.57, 45)
4.57
3
india
4.57
45
('india', 4.57, 45, 3.88, 89)
('india', 4.57, 45, 'india', 4.57, 45)
4
(12,)
()
(4, 23)
```
## Tuple unpacking
* destructuring operation that unpacks data structures into named reference

```
def minmax(items):
  return min(items),max(items)
lower,upper=minmax([21,4,5,7,23])
print(lower)
print(upper)

# nested tuple
(a,(b,(c,d)))=(1,(2,(3,4)))
print(a)
print(b)
print(c)
print(d)

# swap
e='ball'
f='cat'
e,f=f,e
print(f)
print(e)

print(tuple([3,5,6,7,3]))
print(tuple('congratulations'))
print(5 in (1,2,3,4,5,6,7))
print(5 not in (5,6,7,8))
```
### output
```
4
23
1
2
3
4
ball
cat
(3, 5, 6, 7, 3)
('c', 'o', 'n', 'g', 'r', 'a', 't', 'u', 'l', 'a', 't', 'i', 'o', 'n', 's')
True
False
```
### strings
* strings are immutable. you cannot modify them in place
* use str.join() to join strings

### str.join()
* concatenation with + results in temporaries
* str.join() inserts a new separator between a collection of string
* call join() on the separator string

```
animals=';'.join(['tiger','lion','zebra'])
print(animals)

ani_split=animals.split(';')
print(ani_split)

ani=''.join(['kathish','kumaran'])
print(ani)
```
### output
```
tiger;lion;zebra
['tiger', 'lion', 'zebra']
kathishkumaran
```
### partition
```
a='unforgettable'.partition('forget')
print(a)

department,separator,country='civil:india'.partition(':')
print(department)
print(country)
```
### output
```
('un', 'forget', 'table')
civil
india
```
### string formatting
```
import math

a= 'the age of {0} is {1}'.format('jim',20)
print(a)

b='he is {0} in {1}. god is {0} all the {2}'.format('goog','all','time')
print(b)

c='he is {} in {} our {}'.format('good','all','situation')
print(c)

d='Curent position {latitude} {longitude}'.format(latitude='30N',longitude='29E')
print(d)

e='position x={pos[0]},y={pos[1]},z={pos[2]}'.format(pos=(23,34,56))
print(e)

f='math constants: pi={m.pi},e={m.e}'.format(m=math)
print(f)

g='math constants: pi={m.pi:.3f},e={m.e:.2f}'.format(m=math)
print(g)

value=4*20
h='the value is {value}'.format(value=value)
print(h)
```
### output
```
the age of jim is 20
he is goog in all. god is goog all the time
he is good in all our situation
Curent position 30N 29E
position x=23,y=34,z=56
math constants: pi=3.141592653589793,e=2.718281828459045
math constants: pi=3.142,e=2.72
the value is 80
```
### f-string
```
import math
import datetime

g=f'math constants: pi={math.pi:.3f},e={math.e:.2f}'
print(g)

value=4*20
h=f'the value is {value}'
print(h)

g=f'math constants: pi={math.pi},e={math.e}'
print(g)

b=f'the current time is {datetime.datetime.now().isoformat()}'
print(b)
```
### output
```
math constants: pi=3.142,e=2.72
the value is 80
math constants: pi=3.141592653589793,e=2.718281828459045
the current time is 2023-04-03T13:25:13.535274
```

## Range
* sequence representing an arithmetic progression of integers
### range() signature
> range(stop)

> range(start,stop)

> range(statr,stop,step)

```
for i in range(5):
  print(i)

a=list(range(5,10))
b=list(range(10,20,2))
print(a)
print(b)

s=[1,4,5,7,8]
for i in range(len(s)):
  print (s[i])

for v in s:
  print (v)

```
### output
```
0
1
2
3
4
[5, 6, 7, 8, 9]
[10, 12, 14, 16, 18]
1
4
5
7
8
1
4
5
7
8
```
### enumerate
* constructs an iterable of (index,value) tuble around another iterable object

```
a=[23,44,67,4,2,233]
for i in enumerate(a):
  print (i)

for i,b in enumerate(a):
  print(f'i={i},b={b}')
```
### output
```
(0, 23)
(1, 44)
(2, 67)
(3, 4)
(4, 2)
(5, 233)
i=0,b=23
i=1,b=44
i=2,b=67
i=3,b=4
i=4,b=2
i=5,b=233
```
## Set
* unordered collection of unique elements
* sets are mutable
* each elements in a set must be immutable
* common use of set is to efficiently remove duplicate items from the series of object
* sets are iterable, although the order is arbitrary

```
a={1,45,76,87,98,4,23}
print(a)

b=set([32,45,76,12,23,67])
print(b)

# iteration
for i in a:
  print(i)

print(32 in b)
print(76 not in b)

# add
a.add(12)
print(a)

# update
b.update([2,3])
print(b)

# remove
b.remove(76)
print(b)

# discard
b.discard(23)
print(b)

# copy
e=b.copy()
print(e)


```
### output
```
{1, 98, 4, 76, 45, 23, 87}
{32, 67, 12, 76, 45, 23}
1
98
4
76
45
23
87
True
False
{1, 98, 4, 76, 45, 12, 23, 87}
{32, 2, 67, 3, 12, 76, 45, 23}
{32, 2, 67, 3, 12, 45, 23}
{32, 2, 67, 3, 12, 45}
{32, 2, 67, 3, 12, 45}
```
> set algebra:union,difference,intersection,subset,superset and disjoints

```
a={'hai','hello','hey'}
b={'hai','how','what','where'}
c={'hai'}
d={'where'}
e={'wherever'}

# union
print(a.union(b))
print(a.union(b)==b.union(a))

# intersection
print(a.intersection(b))
print(a.intersection(b)==b.intersection(a))

# difference
print(a.difference(b))
print(a.difference(b)==b.difference(a))

print(a.symmetric_difference(b))
print(a.symmetric_difference(b)==b.symmetric_difference(a))

# subset
print(d.issubset(b))
print(b.issubset(d))

# superset
print(d.issuperset(b))
print(b.issuperset(d))

# disjoints
print(d.isdisjoint(e))
print(b.isdisjoint(c))
```
### output
```
{'hey', 'hello', 'how', 'hai', 'what', 'where'}
True
{'hai'}
True
{'hey', 'hello'}
False
{'hey', 'hello', 'what', 'how', 'where'}
True
True
False
False
True
True
False
```

## Dictionaries
* keys must be immutable
* values may be mutable
* As with lists, dictionary copy is shallow

```
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
```
### output
```
{'raja': 23, 'siva': 34, 'mari': 54, 'rajesh': 34}
{'a': 'alpha', 'b': 'beta', 'c': 'gamma'}
----------- {'a': 'alpha', 'b': 'beta', 'c': 'gamma'}
e--- {'a': 'alpha', 'b': 'beta', 'c': 'gamma'}
{'a': 'alpha', 'b': 'beta', 'c': 'gamma', 'd': 'dog', 'e': 'elephant'}
e-----> {'a': 'alpha', 'b': 'beta', 'c': 'gamma', 'd': 'domestic', 'e': 'elephant', 'f': 'fox'}
```
### Dictionary Iteration
* Dictionaries yields the next key on each iteration
* Values can be retrieved using the square bracket operator

### dict.update()
* adds entries from one dictionaries to another
* calls this on the dictionary that is to be updated

### dict.items()
* iterates over keys and values in tandem
* yields a (key,value) tuple on each iteration

```
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

```
### output
```
one====>green
green
red
yellow
one
two
three
one======>green
two======>red
three======>yellow
two====>red
green
red
yellow
one
two
three
one======>green
two======>red
three======>yellow
three====>yellow
green
red
yellow
one
two
three
one======>green
two======>red
three======>yellow
```
### pprint
* without the "as pp" ,the pprint function would mask the pprint module
* This kind of duplicate naming is probably best avoided in your own API's

```
from pprint import pprint as pp

z={'H':1,'J':3,'K':7,'D':8}
print(z)

# delete
del z['K']
print(z)

h={'H':[1,3,4,7],'J':3,'K':7,'D':8}
print(h)
h['H'] += [8,9,0]
print(h)
h['N'] =[4,6,8]
print(h)

from pprint import pprint as pp

pp(h)


```
### output
```
{'H': 1, 'J': 3, 'K': 7, 'D': 8}
{'H': 1, 'J': 3, 'D': 8}
{'H': [1, 3, 4, 7], 'J': 3, 'K': 7, 'D': 8}
{'H': [1, 3, 4, 7, 8, 9, 0], 'J': 3, 'K': 7, 'D': 8}
{'H': [1, 3, 4, 7, 8, 9, 0], 'J': 3, 'K': 7, 'D': 8, 'N': [4, 6, 8]}
{'D': 8, 'H': [1, 3, 4, 7, 8, 9, 0], 'J': 3, 'K': 7, 'N': [4, 6, 8]}
```

## Protocols
* a set of operations that a type must support to implement the protocol
* do not need to be defined as interfaces or base classes
* Types only need to provide functioning implementations

> protocol:container (str,list,dict,range,tuple,set,bytes)

> protocol:sized (str,list,dict,range,tuple,set,bytes)

> protocol:iterable (str,list,dict,range,tuple,set,bytes)

> protocol:sequence (str,list,dict,range,tuple)

> protocol:mutable sequence (list)

> protocol:mutable set (set)

> protocol:mutable mapping (dict)

## Lists
### negative indices
* index from the end of sequences using negative numbers
* the last element is at index -1

```
a=[1,-4,6,8.9,9]
print(a[-1])
print(a[-5])
print(a[0])
print(a[-0])
print(a[2])
```
### output
```
9
1
1
1
6
```

### slicing
* Extended form of indexing for referring to a portion of a list or other sequences
* Syntax: a_list[start:stop]

```
a=[2,4,6,8,9,7,5]
print(a[1:-1])
print(a[2:6])
print(a[3:])
print(a[:4])
print(a[:])

b=a
print(b)
print(b is a)

c=b[:]
print(c)
print(c is b)
```
### output
```
[4, 6, 8, 9, 7]
[6, 8, 9, 7]
[8, 9, 7, 5]
[2, 4, 6, 8]
[2, 4, 6, 8, 9, 7, 5]
[2, 4, 6, 8, 9, 7, 5]
True
[2, 4, 6, 8, 9, 7, 5]
False
```

```
a=[[1,2],[3,4]]
b=a[:]
print(b)
print(a is b)
print(a==b)

print(a[0]==b[0])

a[1].append(5)
print(a)

s=[[1,3]]*4
print(s)
s[2].append(6)
print(s)
```
### output
```
[[1, 2], [3, 4]]
False
True
True
[[1, 2], [3, 4, 5]]
[[1, 3], [1, 3], [1, 3], [1, 3]]
[[1, 3, 6], [1, 3, 6], [1, 3, 6], [1, 3, 6]]
```
### list.index()
* find the location of an object in a list
* returns the index of the first item element which is equal to the argument

```
a='he is good in all the works and he is such a wonderfull person to speak'.split()
print(a)
i=a.index('works')
print(i)
print(a[i])
b=a.count('he')
print(b)
```
### output
```
['he', 'is', 'good', 'in', 'all', 'the', 'works', 'and', 'he', 'is', 'such', 'a', 'wonderfull', 'person', 'to', 'speak']
6
works
2
```
### del
* remove an element from a list by index
* Syntax:del a_list[index]

```
a='he is good in all the works and he is such a wonderfull person to speak'.split()

del a[5]
print(a)
a.remove('is')
print(a)

i=a.index('such')
del a[i]
print(a)
```
### output
```
['he', 'is', 'good', 'in', 'all', 'works', 'and', 'he', 'is', 'such', 'a', 'wonderfull', 'person', 'to', 'speak']
['he', 'good', 'in', 'all', 'works', 'and', 'he', 'is', 'such', 'a', 'wonderfull', 'person', 'to', 'speak']
['he', 'good', 'in', 'all', 'works', 'and', 'he', 'is', 'a', 'wonderfull', 'person', 'to', 'speak']
```
### list.insert()
* insert an item into a list
* accepts an item and index of the new item

```
a='my name is kathish'.split()
a.insert(4,'kumaran')
print(a)
print(' '.join(a))

m=[1,3,4,6,8]
n=[2.4,6,8,9]
o=m+n
print(o)
o+=[89,100]
print(o)
o.extend([101,102])
print(o)
```
### output
```
['my', 'name', 'is', 'kathish', 'kumaran']
my name is kathish kumaran
[1, 3, 4, 6, 8, 2.4, 6, 8, 9]
[1, 3, 4, 6, 8, 2.4, 6, 8, 9, 89, 100]
[1, 3, 4, 6, 8, 2.4, 6, 8, 9, 89, 100, 101, 102]
```
### list.reverse() and list.sort()
* common operations that modify a list in place
* sort method accepts two arguments (key and reverse)

```
a=[1,2,3,43]
# reverse
a.reverse()
print(a)

# sort
a.sort()
print(a)
a.sort(reverse=True)
print(a)
```
### output
```
[43, 3, 2, 1]
[1, 2, 3, 43]
[43, 3, 2, 1]
```
### key parameter to list.sort()
* can be any called object that accepts a single parameter
* items passed to callable and sorted on its return value
```
a='strong  is very he'.split()
a.sort(key=len)
print(a)
```
### output
```
['is', 'he', 'very', 'strong']
```
## Reversing and Sorting into copies
* reversed and sorted are out-of-place equivalents to list.reverse() and list.sort()
* They return a reverse iterator and a new list, respectively

```
x=[4,2,6,2,7]
y=sorted(x)
print(y)
z=[56,34,12,77,89]
j=reversed(z)
print(j)
print(list(j))
```
### output
```
[2, 2, 4, 6, 7]
<list_reverseiterator object at 0x7fcb33e5d970>
[89, 77, 12, 34, 56]
```
## Exceptions
## Exception Handling

> Mechanism for interrupting normal program flow and continuing in surrounding context or code block

> Python Exceptions are similar to exceptions in languages like java and c++

### Exceptions:Key concepts
## 1.Raising an exception
* the event of interrupting normal flow is called the act of raising an exception

## 2.Handling an exception
* the raised exception must be handled upon which control flow is transferred to the exception handler

## 3.Unhandled Exception
* If an exception propagates up the callstack to the start of the program then an unhandled exception will cause the program to terminate

## 4.Exception Objects
* An exception object containing information about where and why an exception event occured is transported from the point at which the exception was raised to the exception handler so that the handler can interrogate the exception object and take appropriate action

## Exception and control flow
```

a={'one':'1','two':'2','three':'3','four':'4'}

def convert(s):
  number=''
  for i in s:
    number += a[i]
  x=int(number)
  return x

print(convert('one two three four'.split()))

# print(convert('around two three'.split()))      kerError
```
### output
```
1234
```
## Handling Exceptions
```
a={'one':'1','two':'2','three':'3','four':'4'}
def convert(s):
  """ Convert a string to a integer"""
  try:
    number=''
    for i in s:
      number += a[i]
    x=int(number)
    print(f'success! x={x}')
  except KeyError:
    print('failed in keyerror')
    x=-1
  except TypeError:
    print('failed in typeerror')
    x=-1
  print (x)
convert('one'.split())
convert('five'.split())
convert(5)
```
### output
```
success! x=1
1
failed in keyerror
-1
failed in typeerror
-1
```

> Exceptions resulting from programmer error:
* Indentation error
* Syntax error
* Name error

> these should always never be caught


## Exceptions and protocol
* sequences should raise Indexerror for out of bound indexing
* Exceptions must be implemented and documented correctly
* Existing built-in exceoptions are often the right one to use

## common exception types
### IndexError
* An integer index is out of range

### ValueError
* An object is of correct type but has an inappropriate value

### KeyError
* A lookup in a mapping failed

## Comprehensions
* concise syntax for describing lists, sets and dictionaries
* readable and expressive
* close to natural languages

### list Comprehensions

```
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
```
### output
```
['My', 'name', 'is', 'kathish']
[2, 4, 2, 7]
[1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
```

### Set Comprehensions
```
from math import factorial

f={len(str(factorial(x))) for x in range(20)}
print(f)
```
### output
```
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
```

## Dictionary Comprehensions
* Dictionary comprehensions don't work directly on dict sources
* use dict.items() to get keys and values from dict sources

```
country_to_capital={'United Kingdom':'London',
                    'Brazil':'Brasilia',
                    'Morroco':'Rabat',
                    'Sweden':'Stockholm'}

capital_to_country={capital:country for country,capital in country_to_capital.items()}
print(capital_to_country)

from pprint import pprint as pp

pp(capital_to_country)

a= ['hai','hello','fox','hotel','elephant']
b={x[0]:x for x in a}
print(b)
```
### output
```
{'London': 'United Kingdom', 'Brasilia': 'Brazil', 'Rabat': 'Morroco', 'Stockholm': 'Sweden'}
{'Brasilia': 'Brazil',
 'London': 'United Kingdom',
 'Rabat': 'Morroco',
 'Stockholm': 'Sweden'}
{'h': 'hotel', 'f': 'fox', 'e': 'elephant'}

```
## Filtering Comprehensions
```
from math import sqrt

def is_prime(x):
  if x<2:
    return False
  for i in range(2, int(sqrt(x))+1):
    if x%i == 0:
      return False
  return True

print([x for x in range(101) if is_prime(x)])

from pprint import pprint as pp

prime_square_divisors={x*x :(1,x,x*x) for x in range(20) if is_prime(x)}
pp(prime_square_divisors)
```
### output
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
{4: (1, 2, 4),
 9: (1, 3, 9),
 25: (1, 5, 25),
 49: (1, 7, 49),
 121: (1, 11, 121),
 169: (1, 13, 169),
 289: (1, 17, 289),
 361: (1, 19, 361)}
```
## Iteration Protocols

> Iterable: can be passed to iter() to produce an iterator

> Iterator: can be passed to next() to get the next value in the sequences

```
a=['one','two','three','four']
b=iter(a)
c=next(b)
print(c)
d=next(b)
print(d)


def first(a):
  b=iter(a)
  try:
    c=next(b)
    print(c)
  except StopIteration:
    raise ValueError('a is empty')
first(['one','two','three','four'])
first({'one','two','three','four'})
# first(set())                               ValueError
```
### output
```
one
two
one
three
```
## Generator Functions
* iterable defined by functions
* lazy evaluation
* can model sequences with no definite end
* composable into pipelines

### yield
* Generator function must include atleast one yield statement

```
def gen():
  print('its a')
  yield 1
  print('its b')
  yield 2
  print('its c')
  yield 3
  print('about to return')

result=gen()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
```
### output
```
its a
1
its b
2
its c
3
about to return
Traceback (most recent call last):
  File "generator-comprehension.py", line 14, in <module>
    print(next(result))
StopIteration
```
### maintaining state in generator
```
def take(count,iterable):
  counter=0
  for item in iterable:
    if counter==count:
      return
    counter+=1
    yield item

def distinct(iterable):
  seen=set()
  for item in iterable:
    for item in seen:
      continue
    yield item
    seen.add(item)

def run_pipeline():
  items=[3,6,6,2,1,1]
  for item in take(3,list(distinct(items))):
    print (item)

run_pipeline()
```
### output
```
3
3
3
```

## Laziness and the Infinite
* Generators only do enough work to produce requested data
* This allows generators to model infinite (or just very large) sequences
* Examples of such sequences are sensor readings, mathematical sequences and contents of large files

```
def lucas():
  yield 2
  a=1
  b=2
  while True:
    yield b
    a,b=b,a+b

for x in lucas():
  print(x)
```
## Generator Expressions
* To recreate generator from a generator expression, you must execute the expression again

```
a=(x*x for x in range(1,10))
print(list(a)[-10:])
print(list(a))
```
### output
```
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[]
```

## Classes
* Define the structure and behaviour of objects
* Act as a template for creating new objetcs
* Classes control an object's initial state, attributes and methods
* Classes can make complex problem tractable
* But they can make simple problem unnecessarily complex
* Python let you strike the right balance between the functions and classes

```
class Flight:

  def number(self):
    print ('SN06')
f=Flight()
f.number()

# same
Flight.number(f)
```
### output
```
SN06
SN06
```
## __init__()
* Instance method for initializing new object
* It is an initializer not a constructor
* self is similar to this in java , c# , c++

### why _number?
* Avoid name clash with number()
* By convention, implementation details start with underscore

```
class Flight:

  def __init__(self,number):
    self._number=number

  def number(self):
    return self._number

f=Flight('SN06')
print(f._number)
print(f.number())
print(Flight.number(f))
```
### output
```
SN06
SN06
SN06
```
```
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

f=Flight('SN06')
print(f._number)
# g=Flight('060')
# print(g._number)
# h=Flight('sn060')
i=Flight('snabd')
# print(h._number)
print(i._number)
```
### output
```
SN06
Traceback (most recent call last):
  File "init-instance.py", line 20, in <module>
    i=Flight('snabd')
  File "init-instance.py", line 7, in __init__
    raise ValueError(f"Invalid airline code '{number}'")
ValueError: Invalid airline code 'snabd'
```
### Example:
```
class Flight:
  """ A flight with a particular passenger aircraft"""

  def __init__(self,number,aircraft):
    if not number[:2].isalpha():
      raise ValueError(f"no airline code in '{number}'")
    if not number[:2].isupper():
      raise ValueError(f"Invalid airline code '{number}'")
    if not (number[2:].isdigit() and int(number[2:])<=9999):
      raise ValueError(f"invalid route number '{number}'")

    self._number=number
    self._aircraft=aircraft

  def aircraft_model(self):
    return self._aircraft.model()

  def number(self):
    return self._number

  def airline(self):
    return self._number[:2]



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

f=Flight('BA758',Aircraft('G-EUPT','Airbus 0ES',num_rows=22,num_seats_per_row=7))
print(f.aircraft_model())

```
### output
```
Airbus 0ES
```

### Example : Booking seats
```
class Flight:
  """ A flight with a particular passenger aircraft"""

  def __init__(self,number,aircraft):
    if not number[:2].isalpha():
      raise ValueError(f"no airline code in '{number}'")
    if not number[:2].isupper():
      raise ValueError(f"Invalid airline code '{number}'")
    if not (number[2:].isdigit() and int(number[2:])<=9999):
      raise ValueError(f"invalid route number '{number}'")

    self._number=number
    self._aircraft=aircraft
    rows,seats=self._aircraft.seating_plan()
    self._seating=[None]+[{letter:None for letter in seats}for _ in rows]

  def aircraft_model(self):
    return self._aircraft.model()

  def number(self):
    return self._number

  def airline(self):
    return self._number[:2]

  def allocate_seat(self,seat,passenger):
    rows,seat_letters=self._aircraft.seating_plan()
    letter=seat[-1]
    if letter not in seat_letters:
      raise ValueError(f'Invalid seat letter {letter}')

    row_text=seat[:-1]
    try:
      row=int(row_text)
    except ValueError:
      raise ValueError(f'Invalid seat row {row_text}')

    if row not in rows:
      raise ValueError(f'Invalid row number {row}')

    if self._seating[row][letter] is not None:
      raise ValueError(f'seat {seat} already occupied ')

    self._seating[row][letter]=passenger




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

f=Flight('BA758',Aircraft('G-EUPT','Airbus 0ES',num_rows=22,num_seats_per_row=7))
print(f.allocate_seat('12A','Ram'))
# print(f.allocate_seat('12A','kumar'))

from pprint import pprint as pp

pp(f._seating)

```
### output
```
None
[None,
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': 'Ram', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}]
 ```

 ### Example: console card printer
 ```
 class Flight:
  """ A flight with a particular passenger aircraft"""

  def __init__(self,number,aircraft):
    if not number[:2].isalpha():
      raise ValueError(f"no airline code in '{number}'")
    if not number[:2].isupper():
      raise ValueError(f"Invalid airline code '{number}'")
    if not (number[2:].isdigit() and int(number[2:])<=9999):
      raise ValueError(f"invalid route number '{number}'")

    self._number=number
    self._aircraft=aircraft
    rows,seats=self._aircraft.seating_plan()
    self._seating=[None]+[{letter:None for letter in seats}for _ in rows]

  def aircraft_model(self):
    return self._aircraft.model()

  def number(self):
    return self._number

  def airline(self):
    return self._number[:2]

  def allocate_seat(self,seat,passenger):
    row,letter=self._parse_seat(seat)

    if self._seating[row][letter] is not None:
      raise ValueError(f'seat {seat} already occupied ')

    self._seating[row][letter]=passenger

  def _parse_seat(self,seat):
    rows,seat_letters=self._aircraft.seating_plan()
    letter=seat[-1]
    if letter not in seat_letters:
      raise ValueError(f'Invalid seat letter {letter}')

    row_text=seat[:-1]
    try:
      row=int(row_text)
    except ValueError:
      raise ValueError(f'Invalid seat row {row_text}')

    if row not in rows:
      raise ValueError(f'Invalid row number {row}')

    return row,letter

  def relocate_passenger(self,from_seat,to_seat):

    from_row,from_letter=self._parse_seat(from_seat)
    if self._seating[from_row][from_letter] is None:
      raise ValueError(f'No passenger to allocate in seat {from_seat}')

    to_row,to_letter=self._parse_seat(to_seat)
    if self._seating[to_row][to_letter] is not None:
      raise ValueError(f'seat {to_seat} is already occupied')

    self._seating[to_row][to_letter]=self._seating[from_row][from_letter]
    self._seating[from_row][from_letter]=None

  def num_availbale_seats(self):
    return sum(sum(1 for s in row.values() if s is None)
               for row in self._seating
               if row is not None)

  def make_boarding_cards(self,card_printer):
    for passenger,seat in sorted(self._passenger_seats()):
      card_printer(passenger,seat,self.number(),self.aircraft_model())

  def _passenger_seats(self):
    row_numbers,seat_letters=self._aircraft.seating_plan()
    for row in row_numbers:
      for letter in seat_letters:
        passenger=self._seating[row][letter]
        if passenger is not None:
          yield (passenger,f"{row}{letter}")


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

def console_card_printer(passenger,seat,flight_number,aircraft):
  output=f"| Name:{passenger}"       \
         f"  Flight:{flight_number}" \
         f"  seat:{seat}"            \
         f"  aircraft:{aircraft}"    \
         "  |"
  banner="+"+"-"* (len(output)-2)+"+"
  border="|"+" "* (len(output)-2)+"|"
  lines=[banner,border,output,border,banner]
  card="\n".join(lines)
  print(card)
  print()

def make_flight():
  f=Flight('BA758',Aircraft('G-EUPT','Airbus 0ES',num_rows=22,num_seats_per_row=7))
  f.allocate_seat('12A','Ram')
  f.allocate_seat('12B','kumar')
  f.allocate_seat('12C','rajesh')
  f.allocate_seat('12D','bennison')
  f.allocate_seat('12E','gibson')
  return f
f=make_flight()
f.relocate_passenger('12A','15D')


# f=Flight('BA758',Aircraft('G-EUPT','Airbus 0ES',num_rows=22,num_seats_per_row=7))
# print(f.allocate_seat('12A','Ram'))
# # print(f.allocate_seat('12A','kumar'))

# from pprint import pprint as pp

# pp(f._seating)
# print(f.num_availbale_seats())

print(f.make_boarding_cards(console_card_printer))

```
### output
```
+--------------------------------------------------------+
|                                                        |
| Name:Ram  Flight:BA758  seat:15D  aircraft:Airbus 0ES  |
|                                                        |
+--------------------------------------------------------+

+-------------------------------------------------------------+
|                                                             |
| Name:bennison  Flight:BA758  seat:12D  aircraft:Airbus 0ES  |
|                                                             |
+-------------------------------------------------------------+

+-----------------------------------------------------------+
|                                                           |
| Name:gibson  Flight:BA758  seat:12E  aircraft:Airbus 0ES  |
|                                                           |
+-----------------------------------------------------------+

+----------------------------------------------------------+
|                                                          |
| Name:kumar  Flight:BA758  seat:12B  aircraft:Airbus 0ES  |
|                                                          |
+----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                           |
| Name:rajesh  Flight:BA758  seat:12C  aircraft:Airbus 0ES  |
|                                                           |
+-----------------------------------------------------------+

None
```

## File I/O and Resource Management
### Resources
* Program element that must be released or closed after use
* Python provide special syntax for managing resources

## open()
* Open a file for reading or writing
* file:the path to the file (required)
* mode: read,write or append, plus binary or text
* encoding: encoding to use in a text mode
* open() returns a file-like object

### open() mode
#### mode:
* r-read
* w-write
* a-append
#### selector
* b-binary
* t-text

> wb - write binary

> at - append text

### write()
* write() returns the number of codepoints written. Don't sum these values to determine file length

```
f=open('learning.txt',mode='wt',encoding='utf-8')

f.write('what are you doing man\n')
f.write('I am doing learning\n')
f.write('out of memory')
f.close()
exit()
```
### reading text
```
f=open('learning.txt',mode='rt',encoding='utf-8')
print(f.read(23))
print(f.read())
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readlines())
f.close()
```
### output
```
what are you doing man

I am doing learning
out of memory

what are you doing man

I am doing learning

out of memory
['what are you doing man\n', 'I am doing learning\n', 'out of memory']
```
### file iteration
* use sys.stdout.write() instead of print.It won't add new lines like print()

```
import sys

f=open('learning.txt',mode='rt',encoding='utf-8')
for line in f:
  # print(line)
  sys.stdout.write(line)
f.close()
```
### output
```
what are you doing man
I am doing learning
out of memoryHai How are you
I am fine
what about you
I am good
```
### with-block
* control flow structure for managing resources
* can be used with any objects - such as files - which support the context-manager protocol

## file-like-objects
* object that behave like file
* a semi-formal protocol
* file behaviours are too varied for a fully specified protocol
* use a EAFP approach with file like objects when necessary

```
def words_per_line(flo):
  return [len(line.split()) for line in flo.readlines()]

with open('learning.txt',mode='rt',encoding='utf-8') as real_file:
  wpl=words_per_line(real_file)
print(wpl)
print(type(real_file))

from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as web_file:
  c=words_per_line(web_file)
print(c)
print(type(web_file))

```
### output
```
[5, 4, 6, 3, 3, 3]
<class '_io.TextIOWrapper'>
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 7, 8, 14, 12, 8]
<class 'http.client.HTTPResponse'>
```

## context-manager:
```
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
```
### output
```
open fridge door
finding bacon
Taking bacon
close fridge door
None
```