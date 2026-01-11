import sys

def input():
    return sys.stdin.readline().strip()

left = list(input())
right = []
n = int(input())

for i in range(n):
    arr = list(input().split())

    if arr[0] == 'L' and left:
        right.append(left.pop())
    elif arr[0] == 'D':
        if right:
            left.append(right.pop())
    elif arr[0] == 'B' and left:
        left.pop()
    elif arr[0] == 'P':
        left.append(arr[1])

right.reverse()
print("".join(left) + "".join(right))