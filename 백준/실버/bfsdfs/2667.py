from collections import deque

n = int(input())
cnt = 0
mapCnts = []
arr = []
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]

def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    arr[b][a] = 0
    mapCnt = 1
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            ny = y + moveY[i]
            nx = x + moveX[i]
        
            if(ny < 0 or nx < 0 or ny >= n or nx >= n):
                continue
            
            if(arr[ny][nx] == 1):
                Q.append((nx, ny))
                arr[ny][nx] = 0
                mapCnt += 1

    mapCnts.append(mapCnt)

    
for i in range(n):
    arr.append(list(map(int, input())))

for y in range(n):
    for x in range(n):
        if(int(arr[y][x]) == 1):
            bfs(x, y)
            cnt += 1
            

mapCnts.sort()
print(cnt)
for i in range(cnt):
    print(mapCnts[i])
