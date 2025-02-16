import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()

arr = []
cnt = 0
isSuccess = True

N = int(input())

for i in range(N):
    str = input()
    # 마지막 문자열 기록
    beforeStr = str[0]

    for k in range(len(str)):
        # 이미 나왔던 문자열인데 떨어진 경우라면
        if str[k] in arr:
            isSuccess = False
            break
        
        # 문자열이 달라진다면?
        if(beforeStr != str[k]):
            # 이전 문자열 기록
            arr.append(beforeStr)
            # 마지막 문자열 변경
            beforeStr = str[k]
    
    if(isSuccess):
        cnt += 1
    arr = []
    isSuccess = True

print(cnt)