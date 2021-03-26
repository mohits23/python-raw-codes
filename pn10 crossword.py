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
EVADE


5
1,1
1,1,3,2
0,0
1,1,3,2
0,0
5
ASIAN
RISEN
FEAR
CLAWS
FALLS  '''

N = int(input())
c = []
cross = []
#board = []
for i in range(N):
  c = []
  c = input().split(",")
  cross.append(list(map(lambda x:int(x)-1, c)))
  '''ele = []
  for j in range(N):
      ele.append(0)
  board.append(ele)'''

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
board = []
for i in range(N):
    inc = 0
    ele = []
    for j in range(N):
        if inc < len(cross[i]) and j == cross[i][inc]:
            s = 0
            for k in range(0,cross[i][inc+1]+1):
                #board[i][cross[i][inc]+s] = 'X'
                ele.append('X')
            s = s + 1
            inc = inc + 2
        else:
            ele.append(0)
    board.append(ele)    
      

# For Beta Test
for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board[i][j], end = ' ')



direction = {}
flag_A = 0
flag_D = 0
flag = 0
inc = 1
for i in range(N):
    for j in range(N):
        if board[i][j] != 'X':
            if ( (j == 0 and board[i][j+1] == 0) or (j+1 < N and board[i][j-1] == 'X' and board[i][j+1] == 0) )   or   ( (i == 0 and board[i+1][j] == 0)  or (i+1 < N and board[i-1][j] == 'X' and board[i+1][j] == 0) ):
                board[i][j] = inc
                temp_inc = inc
                inc = inc + 1
                flag = 1
        
            if flag == 1:  # For Incrementing Adjacent Numbers 
                board[i][j] = temp_inc 
            
            if ( (j == 0 and board[i][j+1] == 0) or (j+1 < N and board[i][j-1] == 'X' and board[i][j+1] == 0) ):
                '''board[i][j] = inc
                temp_inc = inc
                inc = inc + 1'''
                #flag = 1
                flag_A = 1
            if ( (i == 0 and board[i+1][j] == 0)  or (i+1 < N and board[i-1][j] == 'X' and board[i+1][j] == 0) ):
                if flag_A != 1:
                    '''board[i][j] = inc
                    temp_inc = inc
                    inc = inc + 1'''
                    #flag = 1
                flag_D = 1
        
            '''#if flag == 1:  # For Incrementing Adjacent Numbers
            if flag == 1 and ( (j == 0 and board[i][j+1] == 'X') or (j+1 < N and board[i][j-1] == 'X' and board[i][j+1] == 'X') ):
                board[i][j] = temp_inc - 1
            else:
                board[i][j] = temp_inc '''

            if flag_A == 1 and flag_D ==0:
                direction[ board[i][j] ] = 'A'
                flag_A = 0
            if flag_D == 1 and flag_A == 0:
                direction[ board[i][j] ] = 'D'
                flag_D = 0
            if flag_A == 1 and flag_D == 1:
                direction[ board[i][j] ] = 'AD'
                flag_A = 0
                flag_D = 0
        

# Now For Length Of Each Solution Number
#for i in range(N):
    #for j in range(N):
        
        
                

''' Transpose Concept:

        board[i][j] -----> board[j][i]
        i.e.,
        
          board_2 = []
          for i in range(len(board)):
              board_2.append(board.[i])
              
          board_2.reverse()

    And,

        Split the above "longest" statement from main "or" and mark the Across(A) and Down(D) along with the loop '''


# For Beta Test
print("\n")
for i in range(N):
  print (end = '\n')
  for j in range(N):
    print(board[i][j], end = ' ')


print("\n")
print(direction)






