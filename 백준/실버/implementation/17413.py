import sys

# with open("./data.txt", "r") as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline().strip()

S = input()
isTag = False
stack = []
str = ""

# 정상 출력해야 하는 경우
# ㄴ 태그 안에 있을 때

# 반대 출력 할 때
# ㄴ 태그 밖에 있을 때

# 언제 출력?
# 공백, 닫힘 태그, 열림 태그, 맨 마지막

for i in range(len(S)):
    
    if(S[i] == "<"):
        if(isTag == False):
            for a in range(len(stack)):
                str += stack.pop()

        isTag = True
        stack.append(S[i])
        
    elif(S[i] == " "):
        if(isTag == False):
            for a in range(len(stack)):
                str += stack.pop()
        
            str += S[i]
        else:
            stack.append(S[i])
    elif(S[i] == ">"):
        for a in range(len(stack)):
            str += stack[a]
            
        stack = []
        isTag = False
        str += S[i]

    elif(i == len(S)-1):
        stack.append(S[i])

        if(isTag == False):
            for a in range(len(stack)):
                str += stack.pop()
        else:
            for a in range(len(stack)):
                str += stack[a]
    else: 
        stack.append(S[i])
        
print(str.strip())