import sys

def input():
    return sys.stdin.readline().strip()

formula = list(input())
stack = []

for i in formula:
    if i == '(':
        stack.append(i)
    elif i == ')':
        temp = 0

        while stack:
            a = stack.pop()
            if a == '(':
                break
            else:
                temp += a
        stack.append(temp)
        
    elif i == 'H':
        stack.append(1)
    elif i == 'C':  
        stack.append(12)
    elif i == 'O':
        stack.append(16)
    else:
        stack.append(stack.pop() * int(i))

print(sum(stack))