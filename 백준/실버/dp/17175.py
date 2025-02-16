import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()
    
    
N = int(input())
dp = [1] * (N + 1)

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[N])