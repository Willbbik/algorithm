import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

A, B, C = map(int, input().split(" "))

arr = []
arr.append(A)
arr.append(B)
arr.append(C)
arr.sort()

print(arr[1])