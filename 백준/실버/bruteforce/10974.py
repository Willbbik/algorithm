import sys

with open("./data.txt", "r") as file:
    def input():
        return file.readline().strip()

# def input():
#     return sys.stdin.readline().strip()

    N = int(input())
    arr = []
    
    def backTracking():
        if(len(arr) == N):
            print(arr)
            return
        
        for a in range(1, N+1):
            if a not in arr:
                arr.append(a)
                backTracking()
                arr.pop()

    backTracking()