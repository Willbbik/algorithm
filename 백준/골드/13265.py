import sys
from collections import deque
   
    

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

def bfs(node):
    Q = deque()
    Q.append(node)
    colors[node] = 0
    
    while Q:
        a = Q.popleft()
        
        for b in maps[a]:
            # 연결
            if(colors[b] == -1):
                Q.append(b)
                colors[b] = 1 - colors[a]
                
            # 연결된 노드인데 현재 노드와 같은 색상이라면
            # 인접리스트가 아님
            if(colors[b] != -1 and colors[b] == colors[a]):
                return False

    return True


T = int(input())

# 테스트 케이스 개수만큼 반복
for _ in range(T):
    
    n, m = map(int, input().split(" "))
    result = []
    
    # 인접 리스트
    maps = [[] for _ in range(n + 1)]
    colors = [-1] * (n + 1)
    
    # 동그라미 연결
    for _ in range(m):
        x, y = map(int, input().split(" "))
        
        maps[x].append(y)
        maps[y].append(x)
    
    # 동그라미 색칠
    for i in range(1, n+1):
        if(colors[i] == -1):
            result.append(bfs(i))


    if(all(result)):
        print("possible")
    else:
        print("impossible")