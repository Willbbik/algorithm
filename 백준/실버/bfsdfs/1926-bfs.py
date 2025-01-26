import sys
from collections import deque

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[y][x] = True
    nodeCnt = 1
    
    while Q:
        nX, nY = Q.popleft()
        
        for i in range(4):
            newX = nX + moveX[i]
            newY = nY + moveY[i]
            
            if(visited[newY][newX] == True):
                continue
            
            if(newY >= n or newY < 0 or newX >= m or newX < 0):
                continue
            
            if(maps[newY][newX] == 1):
                visited[newY][newX] = True
                Q.append((newX, newY))
                nodeCnt += 1
                
    return nodeCnt

n, m = map(int, input().split(" "))
maxWidth = 0
cnt = 0
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
maps = []
visited = [[False] * (m+1) for _ in range(n+1)]

for _ in range(n):
    maps.append(list(map(int, input().split(" "))))
    

for y in range(n):
    for x in range(m):
        if(visited[y][x] == False and maps[y][x] == 1):
            cnt += 1
            result = bfs(x, y)
            
            if(result > maxWidth):
                maxWidth = result
                
print(cnt)
print(maxWidth)