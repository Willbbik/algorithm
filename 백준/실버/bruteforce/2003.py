import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline()
    
def input():
    return sys.stdin.readline()

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
cnt = 0
total = 0
endPointer = 0

for startPointer in range(N):
    while total < M and endPointer < N:
        total += arr[endPointer]
        endPointer += 1
        
    if(total == M):
        cnt += 1
    
    total -= arr[startPointer]

print(cnt)