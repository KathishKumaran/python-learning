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
------- 1
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