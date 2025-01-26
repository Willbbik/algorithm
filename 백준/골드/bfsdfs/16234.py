from collections import deque
import math

# with open ('./data.txt', 'r') as file:
#     lines = file.read().strip().split("\n")

# N, L, R = map(int, lines[0].split(" "))
N, L, R = map(int, input().split(" "))

moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
start = True
temp = []
graph = []
day = 0

for i in range(N):
    # arr = list(map(int, lines[i+1].split(" ")))
    arr = list(map(int, input().split(" ")))
    graph.append(arr)
        

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[y][x] = True
    union = []
    union.append((x, y))
    
    while Q:
        nowX, nowY = Q.popleft()
        
        for i in range(4):
            nX = nowX + moveX[i]
            nY = nowY + moveY[i]
            
            if(nX >= N or nX < 0 or nY >= N or nY < 0):
                continue
            
            if(visited[nY][nX]):
                continue
            
            a = abs(graph[nowY][nowX] - graph[nY][nX])
            
            if(L <= a and a <= R):
                visited[nY][nX] = True
                Q.append((nX, nY))
                union.append((nX, nY))

    if(len(union) <= 1):
        return 0

    result = math.floor(sum(graph[d][c] for c, d in union) / len(union))

    for c, d in union:
        graph[d][c] = result

    return 1

while start:
    visited = [[False] * N for _ in range(N)]
    temp = 0

    for y in range(N):
        for x in range(N):
            if(visited[y][x] == False):
                temp += bfs(x, y)

    if(temp == 0):
        start = False
        break
    
    day += 1

print(day)