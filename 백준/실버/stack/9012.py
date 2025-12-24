import sys

# with open('./data.txt', 'r') as file:
#     def input():
#         return file.readline().strip()
    
def input():
    return sys.stdin.readline()

n = int(input())

for i in range(0, n, 1):
    stack = []
    arr = list(input())

    for a in arr:
        if a == '(':
            stack.append(a)
        
        if a == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
            
# 시작 괄호는 stack에 넣고, 종료 괄호면 pop 해주기.
# 종료 괄호인데 stack이 비었다는건 잘못된 괄호 문자열. = NO
# stack이 비어있지않으면 미완성 괄호가 있기에 = NO