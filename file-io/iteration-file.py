import sys

f=open('learning.txt',mode='rt',encoding='utf-8')
for line in f:
  # print(line)
  sys.stdout.write(line)
f.close()