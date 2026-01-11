import sys

def input():
    return sys.stdin.readline()

n = int(input())
stack = []

for i in range(n):
    arr = list(map(int, input().split()))
    command = arr[0]

    if command == 1:
        stack.append(arr[1])
    elif command == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)