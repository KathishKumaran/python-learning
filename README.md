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


