import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

for i in range(n):
    text = list(input())
    left = []
    right = []
    
    for a in text:
        if a == '<':
            if left:
                right.append(left.pop())
        elif a == '>':
            if right:
                left.append(right.pop())
        elif a == '-':
            if left:
                left.pop()
        else:
            left.append(a)
    
    right.reverse()
    print("".join(left) + "".join(right))