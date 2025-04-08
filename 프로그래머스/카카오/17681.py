
# 10진수 > 2진수 변환 (5자리 채워서)
def to_binary_number(number):
    binaryStr = str(bin(number))    
    return binaryStr.replace("0b", "").zfill(5)



def solution(n, arr1, arr2):
    
    maps = [[""] * n for __ in range(n)]
    
    for num in arr1:
        to_binary_number(num)