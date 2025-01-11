from collections import deque


# with open('./data.txt', 'r') as file:
#     data = file.read().split(" ")

data = input().split(" ")

N, K = map(int, data)
MAX = 200000
graph = [-1] * (MAX + 1)


def bfs(now, taret):
    Q = deque()
    Q.append(now)
    graph[now] = 0
    
    while Q:
        current = Q.popleft()
        
        if(current == taret):
            return graph[current]
        
        a = current * 2
        b = current + 1
        c = current - 1
        
        # 순간이동 먼저
        if(a <= MAX and graph[a] == -1):
            graph[a] = graph[current]
            Q.appendleft(a)
          
        if(c >= 0 and graph[c] == -1):
            graph[c] = graph[current] + 1
            Q.append(c)
            
        if(b <= MAX and graph[b] == -1):
            graph[b] = graph[current] + 1
            Q.append(b)
        
            
print(bfs(N, K))