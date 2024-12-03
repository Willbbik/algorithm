import sys
from collections import deque

# with open("./data.txt", "r") as f:
#     input_data = f.read().splitlines()
    
input = sys.stdin.read
input_data = input().splitlines()


N = int(input_data[0])
M = int(input_data[1])
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

# 노드 서로 연결
for line in input_data[2:]:
    a,b=map(int, line.split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
cnt = 0

Q = deque([1])
while Q:
    c=Q.popleft()
    for i in graph[c]:
        if visited[i]!=True:
            Q.append(i)
            visited[i] = True
            cnt += 1

print(cnt)
            
    
    

