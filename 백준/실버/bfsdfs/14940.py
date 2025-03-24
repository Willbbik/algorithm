import sys
from collections import deque

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

def bfs(y, x):
    Q = deque()
    Q.append((y, x))
    visited[y][x] = True
    arr[y][x] = 0
    
    while Q:
        a, b = Q.popleft()
        
        for i in range(4):
            ny = a + moveY[i]
            nx = b + moveX[i]
            
            if(0 > ny or ny >= n or 0 > nx or nx >= m):
                continue
        
            if(visited[ny][nx] == False and arr[ny][nx] == 1):
                arr[ny][nx] = arr[a][b] + 1
                visited[ny][nx] = True
                Q.append((ny, nx))
    

moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]

n, m = map(int, input().split(" "))
arr = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split(" "))))

for y in range(n):
    for x in range(m):
        if(arr[y][x] == 2 and visited[y][x] == False):
            bfs(y, x)

for y in range(n):
    for x in range(m):
        if(visited[y][x] == False and arr[y][x] != 0):
            arr[y][x] = -1

for y in range(n):
    print(" ".join(map(str, arr[y])))