''' 3
    E E S
    S D S
    E D F '''



def recur(start,blocks,r,c,N):
    print("~~~~~~~~~~~~~~~~")
    l = len(start)
    if l == 1:
        if start[0] == 'E' and c+1 < N:
            if blocks[r][c+1] == 'F':
                return 1
            elif blocks[r][c+1] == 'D':
                return 0
            elif blocks[r][c+1] != 'F' and blocks[r][c+1] != 'D':
                temp = recur(blocks[r][c+1],r,c,blocks,N)
                #if temp == 1 or temo == 0:
                return temp            
            
        elif start[0] == 'W' and c-1 < N:
            if blocks[r][c-1] == 'F':
                return 1
            elif blocks[r][c-1] == 'D':
                return 0
            elif blocks[r][c-1] != 'F' and blocks[r][c-1] != 'D':
                temp = recur(blocks[r][c-1],r,c,blocks,N)
                return temp

        elif start[0] == 'N' and r-1 < N:
            if blocks[r-1][c] == 'F':
                return 1
            elif blocks[r-1][c] == 'D':
                return 0
            elif blocks[r-1][c] != 'F' and blocks[r-1][c] != 'D':
                temp = recur(blocks[r-1][c],r,c,blocks,N)            
                return temp

        elif start[0] == 'S' and r+1 < N:
            if blocks[r+1][c] == 'F':
                return 1
            elif blocks[r+1][c] == 'D':
                return 0
            elif blocks[r+1][c] != 'F' and blocks[r+1][c] != 'D':
                temp = recur(blocks[r+1][c],r,c,blocks,N)            
                return temp
            
        else:
            pass
                

N = int(input())

blocks = []
start = []
r = []
c = []
for i in range(N):
    blocks.append(input().split())
    for j in range(len(blocks[i])):
        if i == 0:
            r.append(i)
            c.append(j)
            start.append(blocks[i][j])
    if i != 0:
        r.append(i)
        c.append(0)
        start.append(blocks[i][0])

    
print(blocks)
print(r)
print(c)
print(start)

d = {'E':1, 'W':-1, 'N':-1, 'S':1}
print(d)

safe = 0
for k in range(len(start)):
    res = recur(start[i],blocks,r[i],c[i],N)
    if res == 1:
        print("\tsafe")
        safe = safe + 1
    elif res == 0:
        print("\tD")
        pass
    elif str(res) == 'None':
        print("\tNone")
        pass

print(safe)    
        
            
