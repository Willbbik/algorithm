from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
list = [[] for i in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)


def bfs(k):
    Q = deque([k])
    visited[k] = True
    
    while Q:
        a = Q.popleft()

        for i in list[a]:
            if(visited[i] == False):
                visited[i] = True
                Q.append(i)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)