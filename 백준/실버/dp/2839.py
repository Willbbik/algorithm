import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()

N = int(input())

if(N % 5 == 0):
    print(N // 5)
else:
    p = 0
    
    while N > 0:
        N -= 3
        p += 1

        if(N % 5 == 0):
            print(N//5 + p)
            break
        
        if(N == 1 or N == 2):
            print(-1)
            break
        
        if(N == 0):
            print(p)
            break