from collections import deque

# with open("./data.txt", "r") as f:
#     data = f.readline()

N, K = map(int, input().split())
MAX = 10 ** 5
visited = [0]* (MAX+1)

def bfs(n):
    q = deque()
    q.append(n)
    
    while q:
        a = q.popleft()
        
        if(a == K):
            q.clear()
            return visited[a]
        
        for i in (a-1, a+1, a*2):
            if(i >= 0 and i <= MAX and visited[i] == 0):
                q.append(i)
                visited[i] = visited[a] + 1
    
print((bfs(N)))
    
