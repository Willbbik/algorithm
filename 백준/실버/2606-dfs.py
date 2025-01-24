import sys

# with open("./data.txt", "r") as f:
#     def input():
#         return f.readline().strip()
    
def input():
    return sys.stdin.readline()

def dfs(node):
    visited[node] = True
    global cnt
    
    for e in maps[node]:
        if(visited[e] == False):
            cnt += 1
            dfs(e)


N = int(input())
K = int(input())
global cnt

maps = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

# 노드 연결
for _ in range(K):
    a, b = map(int, input().split(" "))

    maps[a].append(b)
    maps[b].append(a)
    
dfs(1)
print(cnt)