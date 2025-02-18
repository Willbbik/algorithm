import json
import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()

    # 탑다운 방식으로 찾다가 찾으면 바로 종료하는 느낌으로다가.
    # 정사각형의 최대 크기는 min(N or M) * min(N or M)이 된다.

N, M = map(int, input().split(" "))
arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

# 정사각형이기에 최소값이 곧 길이
minValue = min(N, M)

for a in range(minValue-1, 0, -1):

    # 한칸씩 줄일때마다 상하좌우로 한칸씩 이동하면서 찾아야함.
    for y in range(N):
        for x in range(M):

            yIndex = y + a
            xIndex = x + a
        
            if(yIndex >= N or xIndex >= M):
                continue
            
            isSame = arr[y][x] == arr[y][xIndex] == arr[yIndex][x] == arr[yIndex][xIndex]
            
            if(isSame):
                # 한 변의 길이 * 한 변의 길이
                line = xIndex - x + 1
                
                print(line * line)
                exit()

print(1)