#input : treater height kick doubled pumped

st = str(input())
st = st + ' '
word = ''
w = []
space = 0
for i in range(len(st)):
  if st[i] == ' ':
    w.append(word)
    word = ''
    space = space + 1
  elif st[i] != ' ':
    word = word + st[i]
    
def dekho(string):
  ch = ''
  for i in range(len(string)):
    c = 0
    for j in range(len(string)):
      if j == i:
        continue
      if string[i] == string[j]:
        c = c + 1
    if c == 0:
      ch = string[i]
      break
  if ord(ch) >= 97 and ord(ch) <= 122:
    ch = chr(ord(ch)-32)
  return ch

for ele in w:
  word = word + dekho(ele)
print(word)