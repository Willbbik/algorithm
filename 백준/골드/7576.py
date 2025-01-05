from collections import deque

# with open('./data.txt', 'r') as file:
#     lines = file.read().strip().split('\n')

# M, N = map(int, lines[0].split())
M, N = map(int, input().split())

box = []
for i in range(N):
    # box.append(list(map(int, lines[i+1].split())))
    box.append(list(map(int, input().split())))

moveX = [1, 0, -1, 0]
moveY = [0, -1, 0, 1]
Q = deque()

# 익은 토마토 먼저 전부 담기
for x in range(N):
    for y in range(M):
        if(box[x][y] == 1):
            Q.append((x, y))

while Q:
    nowX, nowY = Q.popleft()
    
    for i in range(4):
        nextX = nowX + moveX[i]
        nextY = nowY + moveY[i]
        
        if(nextX >= N or nextY >= M or nextX < 0 or nextY < 0):
            continue
        
        if(box[nextX][nextY] != 0):
            continue

        Q.append((nextX, nextY))
        box[nextX][nextY] = box[nowX][nowY] + 1


maxDay = max(map(max, box))
hasZero = any(0 in row for row in box)

if(maxDay == 1):
    print(0)
elif(hasZero):
    print(-1)
else:
    print(maxDay-1)