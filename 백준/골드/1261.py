from collections import deque

# with open ('./data.txt', 'r') as file:
#     lines = file.read().strip().split("\n")

# M=열=X축, N=행=Y축
# M, N = map(int, lines[0].split(" "))
M, N = map(int, input().split(" "))

graph = []
dist = [[-1] * M for _ in range(N)]
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]

for i in range(N):
    # graph.append(list(map(int, lines[i+1].strip())))
    graph.append(list(map(int, input().strip())))

def bfs(x, y):
    Q = deque()
    Q.append((y, x))
    dist[y][x] = graph[y][x]
    
    while Q:
        nowY, nowX = Q.popleft()
        
        for i in range(4):
            nextX = nowX + moveX[i] # 열
            nextY = nowY + moveY[i] # 행
            
            if(nextX >= M or nextX < 0 or nextY >= N or nextY < 0):
                continue

            # 첫 방문
            if(dist[nextY][nextX] == -1):
                if(graph[nextY][nextX] == 0):
                    dist[nextY][nextX] = dist[nowY][nowX]
                    Q.appendleft((nextY, nextX))
                else:
                    dist[nextY][nextX] = dist[nowY][nowX] + 1
                    Q.append((nextY, nextX))

            else: # 첫 방문이 아닐 때
                # (최단경로 업데이트)
                if(dist[nextY][nextX] > dist[nowY][nowX] + graph[nextY][nextX]):
                    dist[nextY][nextX] = dist[nowY][nowX] + graph[nextY][nextX]

bfs(0, 0)
print(dist[N-1][M-1])