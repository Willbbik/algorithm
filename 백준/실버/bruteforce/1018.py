import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()

def input():
    return sys.stdin.readline()

N, M = map(int, input().split(" "))
result = []
maps = []

for _ in range(N):
    maps.append(list(input()))

for y in range(N-7):
    for x in range(M-7):
        
        white = 0
        black = 0
        
        for a in range(y, y+8):
            for b in range(x, x+8):
                
                # 짝수인 경우 무조건 첫 칸의 색깔과 같아야함
                if((a + b) % 2 == 0):
                    # 반대색을 칠하는 이유는, 첫블록의 색깔을 올리지 않으려고
                    if(maps[a][b] == 'W'):
                        black += 1
                    if(maps[a][b] == 'B'):
                        white += 1
                else:
                    # 홀수인데 같은 색을 칠하는 이유는, 다시 칠해야 하기 때문에
                    if(maps[a][b] == 'W'):
                        white += 1
                    if(maps[a][b] == 'B'):
                        black += 1
        
        result.append(white)
        result.append(black)

print(min(result))