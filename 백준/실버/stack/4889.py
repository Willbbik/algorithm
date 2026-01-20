import sys

def input():
    return sys.stdin.readline().strip()

idx = 1

while True:
    text = input()

    if text.startswith("-"):
        break

    arr = list(text)
    stack = []

    for i in arr:
        if i == '{':
            stack.append(i)
            continue
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    num = 0

    for i in range(0, len(stack), 2):
        if stack[i] == stack[i+1]:
            num += 1
        else:
            num += 2

    print(f"{idx}. {num}")
    idx += 1