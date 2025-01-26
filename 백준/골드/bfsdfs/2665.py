from collections import deque

# with open('./data.txt', 'r') as file:
#     lines = file.read().strip().split("\n")
    
# N = int(lines[0])
N = int(input())

graph = []
dist = [[-1] * N for _ in range(N)]
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]

for i in range(N):
    # graph.append(list(map(int, lines[i+1])))
    graph.append(list(map(int, input())))


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    dist[y][x] = 0
    
    while Q:
        nowX, nowY = Q.popleft()
        
        for i in range(4):
            nX = nowX + moveX[i]
            nY = nowY + moveY[i]

            if(nX >= N or nX < 0 or nY >= N or nY < 0):
                continue
            
            # 첫 방문이라면
            if(dist[nY][nX] == -1):
                if(graph[nY][nX] == 1):
                    dist[nY][nX] = dist[nowY][nowX]
                    Q.appendleft((nX, nY))
                else:
                    dist[nY][nX] = dist[nowY][nowX] + 1
                    Q.append((nX, nY))
            
bfs(0, 0)
print(dist[N-1][N-1])