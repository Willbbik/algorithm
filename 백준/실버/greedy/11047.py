import sys

def input():
    return sys.stdin.readline().strip()


N, K = list(map(int, input().split(" ")))
coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))

coins.reverse()

for i in coins:
    if K >= i:
        cnt += K // i
        K = K % i

print(cnt)