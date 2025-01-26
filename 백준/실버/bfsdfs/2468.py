import sys
from collections import deque

# with open('./data.txt', 'r') as file:
#     lines = file.read().strip().split('\n')
    
# N = int(lines[0])
N = int(sys.stdin.readline())

moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
graph = [[0] * N for _ in range(N)]

# 그래프 그리기
for i in range(N):
    # arr = list(map(int, lines[i+1].split()))
    arr = list(map(int, input().split()))
    for k in range(N):
        graph[i][k] = arr[k]
        
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    
    while Q:
        a, b = Q.popleft()
        
        for i in range(4):
            nextX = a + moveX[i]
            nextY = b + moveY[i]

            # 범위를 벗어났거나 물에 잠긴 경우 스킵
            if(nextX >= N or nextY >= N or nextX < 0 or nextY < 0):
                continue
            
            if(visited[nextX][nextY] == True or graph[nextX][nextY] <= r):
                continue

            visited[nextX][nextY] = True
            Q.append((nextX, nextY))

# 그래프에서 최고 높이 값
maxRegion = max(map(max, graph))
counts = []

for r in range(maxRegion+1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N): #행
        for k in range(N):  #열
            if(graph[i][k] > r and not visited[i][k]):
                bfs(i, k)
                cnt += 1
    
    counts.append(cnt)

print(max(counts))