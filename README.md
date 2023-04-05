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
```
### output
```
{'London': 'United Kingdom', 'Brasilia': 'Brazil', 'Rabat': 'Morroco', 'Stockholm': 'Sweden'}
{'Brasilia': 'Brazil',
 'London': 'United Kingdom',
 'Rabat': 'Morroco',
 'Stockholm': 'Sweden'}

```

