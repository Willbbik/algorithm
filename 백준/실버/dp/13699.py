import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()

N = int(input())
dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[N])