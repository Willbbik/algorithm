import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()


N = int(input())
arr = set(map(int, input().split(" ")))

M = int(input())
findArr = list(map(int, input().split(" ")))

for index in findArr:
    if index in arr:
        print(1)
    else:
        print(0)