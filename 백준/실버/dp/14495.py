import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline().strip()


N = int(input())

if(N < 3):
    print(1)
else:
    arr = [0] * (N+1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 1
    arr[3] = 2

    for i in range(4, N):
        arr[i] = arr[i-1] + arr[i-3]

    print(arr[N-1])
    