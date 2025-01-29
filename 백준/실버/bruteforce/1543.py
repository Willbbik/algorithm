import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline()
    
def input():
    return sys.stdin.readline().strip()

str = input()
targetStr = input()

print(str.count(targetStr))