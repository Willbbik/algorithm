import sys
sys.setrecursionlimit(10**6)

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

def dfs(x, y, count):
    visited[y][x] = True
    
    for i in range(4):
        newX = x + moveX[i]
        newY = y + moveY[i]
        
        if(visited[newY][newX] == True):
            continue
        
        if(newY >= n or newY < 0 or newX >= m or newX < 0):
            continue
        
        if(maps[newY][newX] == 1):
            visited[newY][newX] = True
            count = dfs(newX, newY, count)
            
    return count + 1
            


n, m = map(int, input().split(" "))
maxWidth = 0
cnt = 0
moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
maps = []
visited = [[False] * (m+1) for _ in range(n+1)]
for _ in range(n):
    maps.append(list(map(int, input().split(" "))))


for y in range(n):
    for x in range(m):
        if(visited[y][x] == False and maps[y][x] == 1):
            cnt += 1
            result = dfs(x, y, 0)
            
            if(result > maxWidth):
                maxWidth = result

print(cnt)
print(maxWidth)