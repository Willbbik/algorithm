import sys

with open("./data.txt", "r") as file:
    def input():
        return file.readline().strip()

# def input():
#     return sys.stdin.readline().strip()

    N, M = map(int, input().split())
    
    moveX = [-1, 0, 1]
    maps = []
    dp = [[0] * M for _ in range(N)]
    
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    
    dp[0][0] = dp[0][0]
    dp[0][1] = dp[0][1]
    dp[0][2] = dp[0][2]
    dp[0][3] = dp[0][3]
    
    
    
    for x in range(M):
        for y in range(N):
            for i in range(3):
                newX = x + moveX[i]
                newY = y + 1
                
                if(newY > N or newX < 0 or newX > M):
                    continue
                
                
                
