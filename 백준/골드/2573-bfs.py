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

    while Q:
        nowX, nowY = Q.popleft()
        
        for i in range(4):
            newX = nowX + moveX[i]
            newY = nowY + moveY[i]

            if(newY >= N or newY < 0 or newX >= M or newX < 0):
                continue

            if(visited[newY][newX]):
                continue
            
            if(maps[newY][newX] == 0):
                maps[nowY][nowX] = max(0, maps[nowY][nowX] - 1)
            
            if(maps[newY][newX] > 0):
                Q.append((newX, newY))
                visited[newY][newX] = True


N, M = map(int, input().split(" "))

moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
maps = []
result = True
year = 0
cnt = 0

for _ in range(N):
    maps.append(list(map(int , input().split(" "))))

while result:
    visited = [[False] * (M+1) for _ in range(N+1)]
    waters = [[0] * (M+1) for _ in range(N+1)]

    # 빙하 덩어리 개수 구하기
    for y in range(N):
        for x in range(M):
            if(visited[y][x] == False and maps[y][x] != 0):
                cnt +=1
                bfs(x, y)
                
                if(cnt >= 2):
                    break

    if(cnt >= 2):
        print(year)
        result = False
    else:
        isNotAble = all(maps[y][x] == 0 for y in range(N) for x in range(M))
        
        if(isNotAble):
            print(0)
            result = False
        else:
            cnt = 0
            year += 1