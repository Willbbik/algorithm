import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
result = []
cur = 1

for next in target: 

    while cur <= next:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack and stack[-1] == next:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit(0)

print("\n".join(result))