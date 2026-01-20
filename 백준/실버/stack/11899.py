import sys

def input():
    return sys.stdin.readline().strip()

text = input()

stack = []

for i in text:
    if i == '(':
        stack.append(i)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

print(len(stack))