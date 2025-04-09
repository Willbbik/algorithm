## [1차] 비밀지도

# 10진수 > 2진수 변환
def to_binary_number(number, n):    
    return bin(number)[2:].zfill(n)

def solution(n, arr1, arr2):
    maps1 = [to_binary_number(num, n) for num in arr1]
    maps2 = [to_binary_number(num, n) for num in arr2]
    result = []

    for row1, row2 in zip(maps1, maps2):
        line = ''
        for a, b in zip(row1, row2):
            line += '#' if a == '1' or b == '1' else ' '
        result.append(line)
    
    return result