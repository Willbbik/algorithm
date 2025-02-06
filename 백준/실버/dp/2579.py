import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()

def solvedp():
    if(N == 1):
        print(arr[0])
        return
    if(N == 2):
        print(arr[0] + arr[1])
        return
    if(N == 3):
        print(max(arr[2]+arr[1], arr[2]+arr[0]))
        return

    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[2]+arr[1], arr[2]+arr[0])

    for i in range(3, N):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])

    print(dp[N-1])

N = int(input())
arr = [0] * (N+1)
dp = [0] * (N+1)

for i in range(0, N):
    arr[i] = int(input())

solvedp()