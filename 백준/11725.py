import sys
from collections import deque


# with open('./data.txt', 'r') as file:
#     data = file.read().strip()
    
# lines = data.split('\n')  # 줄 단위로 나눔
# N = int(lines[0])
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
maps = [0] * (N+1)

for i in range(1, N):
    # a, b = map(int, lines[i].split())
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    Q = deque([1])

    while Q:
        a = Q.popleft()
        
        for i in graph[a]:
            if(maps[i] == 0):
                maps[i] = a
                Q.append(i)
bfs()

for i in range(2, N+1):
    print(maps[i])