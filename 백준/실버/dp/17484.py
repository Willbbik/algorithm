import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()

N, M = map(int, input().split())

maps = []
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N+1)]

for _ in range(N):
    maps.append(list(map(int, input().split())))

for i in range(M):
    dp[0][i] = [maps[0][i], maps[0][i], maps[0][i]]

for y in range(1, N):
    for x in range(M):
        for i in range(3):
            
            # 맨 왼쪽이면 왼쪽 대각선의 위의 값을
            # 맨 오른쪽이면 오른쪽 대각선 위의 값을
            # 비교하지 않겠단 의미
            if((x == 0 and i == 0) or (x == M-1 and i == 2)):
                continue
            
            # 왼쪽 대각선 위에서 왔을때의 최소 값
            if(i == 0):
                # x-1의 이유는 현재x위치보다 항상 1 작아야 하기 때문에
                a = dp[y-1][x-1][1] + maps[y][x]    # 바로 위
                b = dp[y-1][x-1][2] + maps[y][x]    # 오른쪽 대각선 위
                dp[y][x][i] = min(dp[y][x][i], a, b)

            # 위에서 왔을때의 최소 값
            if(i == 1):
                a = dp[y-1][x][0] + maps[y][x]    # 왼쪽 대각선 위
                b = dp[y-1][x][2] + maps[y][x]    # 오른쪽 대각선 위
                dp[y][x][i] = min(dp[y][x][i], a, b)

            # 오른쪽 대각선 위에서 왔을때의 최소 값
            if(i == 2):
                # x+1의 이유는 현재x위치보다 항상 1 커야 하기 때문에
                a = dp[y-1][x+1][0] + maps[y][x]    # 왼쪽 대각선 위
                b = dp[y-1][x+1][1] + maps[y][x]    # 바로 위
                dp[y][x][i] = min(dp[y][x][i], a, b)
            

result = 1e9

for i in range(M):
    result = min(result, min(dp[N-1][i]))

print(result)