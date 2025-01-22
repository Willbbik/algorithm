from collections import deque

with open("./data.txt", "r") as r:
    data = r.read().strip().split("\n")
    
K = int(data[0])
# K = int(input())
result = []

# 연결된 정점은 같은 색이 아니어야함

def bfs(value):
    Q = deque()
    Q.append(value)
    colors[value] = 0
    
    while Q:
        a = Q.popleft()

        for i in maps[a]:
            
            # 첫 방문이라면 원본 노드의 반대 색상
            if(colors[i] == -1):
                Q.append(i)
                colors[i] = 1- colors[a]

            # 방문을 했었는데 원본 노드와 같은 색이라면
            elif(colors[i] != -1 and colors[i] == colors[a]):
                return False
            
            # 방문을 했엇는데 원본 노드와 다른 색이라면
            elif(colors[i] != -1 and colors[i] != colors[a]):
                continue
    
    return True


for k in range(K):
    V, E = map(int, data[0+k].split(" "))
    # V, E = map(int, input().split(" "))

    maps = [[] for _ in range(V)]
    colors = [-1] * V
    
    for i in range(E):
        a, b = map(int, data[0+k+(i+1)].split(" "))
        # a, b = map(int, input().split(" "))
        
        maps[a].append(b)
        maps[b].append(a)
    
    for i in range(V):
        if(colors[i] == -1):
            bfs(i)
    
    if all(maps):
        print("YES")
    else:
        print("NO")

