import sys
import math

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline()
    
def input():
    return sys.stdin.readline()

N, K, I = map(int, input().split(" "))
nowRound = 1
meet = False
stop = False

while not stop:
    if(N < 2):
        stop = True
        break

    # 라운드 (for문이 끝나면 1라운드 종료)
    for i in range(1, N, 2):
        a = i
        b = i+1
        
        # 김씨와 임씨가 대결하는 라운드라면
        if((K == a and I == b) or (K == b and I == a)):
            meet = True
            stop = True
            break
    
    if(not meet):
        nowRound += 1
        K = math.floor((K+1) / 2)
        I = math.floor((I+1) / 2)
        
        if(N % 2 != 0):
            N = math.floor((N+1)/2)    
        else:
            N = math.floor(N/2)
    
if(meet):
    print(nowRound)
else:
    print(-1)
        
            