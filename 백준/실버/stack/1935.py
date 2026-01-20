import sys
import operator

def input():
    return sys.stdin.readline().strip()

n = int(input())
text = list(input())
stack = []
nums = []
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

for i in range(n):
    nums.append(int(input()))

for i in text:
    if i.isalpha():
        index = ord(i) - ord('A')
        stack.append(nums[index])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(ops[i](b, a))

print("{:.2f}".format(stack.pop()))