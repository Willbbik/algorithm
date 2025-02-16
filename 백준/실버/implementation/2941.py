import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()
    
str = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
strLength = 0
lastIndex = 0
tempStr = ""

for i in range(len(str)):
    tempStr += str[i]
    
    for target in arr:
        if target in tempStr[lastIndex:]:
            cnt += 1
            lastIndex = i+1
            strLength += len(target)
            break

print(cnt + len(str) - strLength)