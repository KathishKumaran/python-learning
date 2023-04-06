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

