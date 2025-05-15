import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()


N = int(input())
arr = []

for i in range(N):
    arr.append(input())

newArr = sorted(list(set(arr)), key=lambda x: (len(x), x))

for word in newArr:
    print(word)