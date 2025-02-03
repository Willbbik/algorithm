import sys

with open("./data.txt", "r") as file:
    def input():
        return file.readline().strip()

# def input():
#     return sys.stdin.readline()

    N = int(input())

    days = [0] * (N+1)
    moneys = [0] * (N+1)
    dp = [0] * (N+1)

    for i in range(1, N+1):
        T, P = map(int, input().split())
        days[i] = T
        moneys[i] = P


    for i in range(1, N+1):

        # 현재까지 할 수 있는 상담 개수 구하기.
        arr = []
        for j in range(1, N+1):
            if(i == j + days[j] <= N):
                arr.append(moneys[j])
                
        print(dp)
        # 지금 2-7, 5-7에서 2-7을 선택해서 45가 아니라 50으로 나오는중
        
        if(arr):
            dp[i] += dp[i-1] + max(arr)
        else:
            dp[i] = dp[i-1]
    
    print(dp)