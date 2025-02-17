import sys
from collections import Counter

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()

# 산술평균
def fun1():
    value = sum(arr) / N
    return round(value)

# 중앙값
def fun2():
    tempArr = arr
    tempArr.sort()
    
    idx = len(tempArr) // 2
    return arr[idx]

# 최빈값
def fun3():
    count = Counter(arr) 
    tempArr = count.most_common()
    maxCnt = tempArr[0][1]
    modes = []
    
    for data in tempArr:
        if(data[1] == maxCnt):
            modes.append(data[0])
    
    if(len(modes) > 1):
        return sorted(modes)[1]
    else:
        return modes[0]

# 최대값 최소값 사이 범위
def fun4():
    return max(arr) - min(arr)
        

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))
    
print(fun1())
print(fun2())
print(fun3())
print(fun4())