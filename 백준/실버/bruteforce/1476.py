import sys

# with open("./data.txt", "r") as file:
    # def input():
    #     return file.readline().strip()
    
def input():
    return sys.stdin.readline()


E, S, M = map(int, input().split(" "))
e = 0
s = 0
m = 0
year = 0

while True: 
    year += 1
    
    e += 1
    s += 1
    m += 1
    
    if(e > 15):
        e = 1
    
    if(s > 28):
        s = 1
    
    if(m > 19):
        m = 1

    if(E == e and S == s and M == m):
        break

print(year)