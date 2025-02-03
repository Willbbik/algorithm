import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()

N = int(input())

# N+1일째 되는날까지 금액 계산이 필요하기 때문에.
dp = [0] * (N+1)
days = [0] * (N)
moneys = [0] * (N)

for i in range(0, N):
    T, P = map(int, input().split())
    days[i] = T
    moneys[i] = P

# N+1일째 되는날 완료되는 상담이 있는지 확인하기 위해서 N+1
for i in range(N+1):

    arr = []
    for k in range(0, i):
        if(k + days[k] <= i):
            # 상담 완료 시점에
            # 상담 시작일 금액 + 상담 시작일까지 모아뒀던 돈
            arr.append(moneys[k] + dp[k])
    
    if(arr):
        dp[i] = max(arr)
    else:
        dp[i] = dp[i-1]

print(max(dp))