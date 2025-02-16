import sys
import json
from collections import deque

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()

K = int(input())
cnt = 0

for i in range(K):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    
    # json 형식으로
    for q in range(N):
        data = {
            "value": arr[q],
            "isYn": M == q
        }
        
        Q.append(data)

    # 정렬이 끝나고 원하는 값을 찾을 때까지 방복
    while True:
        data = Q.popleft()
        value = data['value']
        isYn = data['isYn']
        
        # 뒤에 현재 값보다 큰게 존재한다면
        result = any(Q[b]["value"] > value for b in range(len(Q)))

        if(result):
            Q.append(data)
        else:
            cnt += 1

            if(isYn == True):
                break

    print(cnt)
    cnt = 0