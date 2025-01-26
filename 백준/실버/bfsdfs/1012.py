import sys
from collections import deque

# 우 하 좌 상 (시계방향)
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
cnt = 0

def bfs(x, y):
    Q = deque()
    Q.append((y, x))
    graph[y][x] = 0
    
    while Q:
        y, x = Q.popleft()
        
        for i in range(4):
            newY = y + moveY[i]
            newX = x + moveX[i]
            
            if(newY < 0 or newX < 0 or newY >= n or newX >= m):
                continue
            
            if(graph[newY][newX] == 1):
                Q.append((newY, newX))
                graph[newY][newX] = 0
    
    
T = int(input())

for _ in range(T):
    # m=가로, n=세로, k=심어져있는배추개수
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    
    # 그래프 그리기
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 인접 행렬 그래프이기 때문에 전체를 순환하면서 확인
    for y in range(n):
        for x in range(m):
            if(graph[y][x] == 1):
                bfs(x, y)
                cnt+=1
    print(cnt)
    cnt = 0