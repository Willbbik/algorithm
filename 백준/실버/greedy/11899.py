import sys

def input():
    return sys.stdin.readline().strip()


N = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()
stack = [arr[0]]


for i in range(1, len(arr)):
    stack.append(stack[i-1] + arr[i])

print(sum(stack))