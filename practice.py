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
