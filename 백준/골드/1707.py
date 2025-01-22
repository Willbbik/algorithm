from collections import deque

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def bfs(value):
    Q = deque()
    Q.append(value)
    colors[value] = 0
    
    while Q:
        a = Q.popleft()

        for z in maps[a]:
            
            # 첫 방문이라면 원본 노드의 반대 색상
            if(colors[z] == -1):
                Q.append(z)
                # 현재 노드가 1이면, 1-1 == 0
                # 현재 노드가 0이면, 1-0 == 1
                # 즉 현재노드와 다른 값을 가지게 할수있음
                colors[z] = 1 - colors[a]

            # 방문을 했었는데 원본 노드와 같은 색이라면
            # 인접한 노드가 같은 색이라면 이분그래프가 아님
            elif(colors[z] == colors[a]):
                return False
    
    return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split(" "))

    maps = [[] for _ in range(V+1)]
    colors = [-1] * (V+1)
    
    # 인접리스트 구현
    for _ in range(E):
        u, v = map(int, input().split(" "))
        maps[u].append(v)
        maps[v].append(u)
    
    # 전체 그래프 탐색
    result = []
    for i in range(1, V+1):
        if(colors[i] == -1):
            result.append(bfs(i))
    
    if all(result):
        print("YES")
    else:
        print("NO")
