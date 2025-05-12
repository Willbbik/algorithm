import sys

# with open('./data.txt', 'r') as file:
#     def input():
#         return file.readline().strip()

    
def input():
    return sys.stdin.readline()

n = int(input())
arr = list(map(int, input().split(" ")))

for i in range(n-1, 0, -1):
    if(arr[i-1] < arr[i]):
        for k in range(n-1, 0, -1):
            if(arr[i-1] < arr[k]):
                arr[i-1], arr[k] = arr[k], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()

print(-1)