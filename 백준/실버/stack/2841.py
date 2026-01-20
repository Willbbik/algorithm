import sys

def input():
    return sys.stdin.readline().strip()

arr = list(map(int, input().split()))
stack = [[] for _ in range(7)]
count = 0

for i in range(arr[0]):

    temp = list(map(int, input().split()))
    K = temp[0]
    P = temp[1]

    if not stack[K] or stack[K][-1] < P:
        stack[K].append(P)
        count += 1
    else:
        while True:
            if not stack[K] or stack[K][-1] < P:
                stack[K].append(P)
                count += 1
                break
            elif stack[K][-1] == P:
                break
            else:
                stack[K].pop()
                count += 1

print(count)