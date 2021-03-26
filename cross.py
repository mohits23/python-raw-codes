'''  TEST CASE:
5
5,1
1,1,3,1,5,1
0,0
1,1,3,1,5,1
1,1
5
ACNE
PLEAS
EVEN
CALVE
EVADE   '''

N = int(input())
c = []
cross = []
board = []
for i in range(N):
  c = []
  c = input().split(",")
  cross.append(list(map(lambda x:int(x)-1, c)))
  ele = []
  for j in range(N):
      ele.append(0)
  board.append(ele)

M = int(input())
word = []
d = {}
for i in range(M):
  word.append(input())
  d[word[i]] = len(word[i])
  
#board = []
#board = [[0]*N]* N

'''board = []
for i in range(N):
    ele = []
    for j in range(N):
        ele.append(0)
    board.append(ele) '''
  
#print(cross)
#print(word)
#print(d)
#print(board)

print("\n")
print(d)

print("\n")
for i in range(N):
  l = len(cross[i])
  for j in range(0,l,2):

    s = 0
    for k in range(0,cross[i][j+1]+1):
      board[i][cross[i][j]+s] = 'X'
      s = s + 1    
      

for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board[i][j], end = ' ')

