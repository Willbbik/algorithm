from collections import deque
from copy import deepcopy

# with open("./data.txt") as file:
#     lines = file.read().strip().split("\n")
    
    
# N = int(lines[0])
N = int(input())
normalCnt = 0
cnt = 0
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
originPicture = []
result = ""

for i in range(N):
    # originPicture.append(list(lines[i+1].strip()))
    originPicture.append(list(input().strip()))

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    
    while Q:
        nowX, nowY = Q.popleft()
        
        for i in range(4):
            nextX = nowX + moveX[i]
            nextY = nowY + moveY[i]
            
            if(nextX >= N or nextY >= N or nextX < 0 or nextY < 0):
                continue
            
            if(visited[nextX][nextY]):
                continue

            if(picture[nowX][nowY] == picture[nextX][nextY]):
                Q.append((nextX, nextY))
                visited[nextX][nextY] = True            


for i in range(2):
    picture = deepcopy(originPicture)
    visited = [[False for _ in range(N)] for _ in range(N)]

    if(i == 1):
        for a in range(N):
            for b in range(N):
                if(picture[a][b] == 'G'):
                    picture[a][b] = 'R'
    
    for j in range(N):
        for k in range(N):
            if(visited[j][k] == False):
                bfs(j, k)
                cnt += 1
                
    if(i == 0):
        result += str(cnt)
    else:
        result += " " + str(cnt)
    cnt = 0
    
print(result)