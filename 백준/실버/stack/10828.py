
import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()
        

class custom_stack:    
    def __init__(self):
        self.arr = []
    
    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if not self.arr:
            print(-1)
        else:
            print(self.arr.pop())

    def size(self):
        print(len(self.arr))
    
    def empty(self):
        if not self.arr:
            print(1)
        else:
            print(0)
    
    def top(self):
        if not self.arr:
            print(-1)
        else:
            print(self.arr[-1])
        
n = int(input())
stack = custom_stack()

for i in range(0, n, 1):
    command = input().split(" ")
    
    match command[0]:
        case 'push':
            stack.push(int(command[1]))
        case 'pop':
            stack.pop()
        case 'size':
            stack.size()
        case 'empty':
            stack.empty()
        case 'top':
            stack.top()