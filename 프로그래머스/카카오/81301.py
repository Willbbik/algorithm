import re

number_list = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def solution(s):
    
    pattern = re.compile(r'zero|one|two|three|four|five|six|seven|eight|nine|\d+', re.IGNORECASE)
    matches = pattern.findall(s)
    
    result = ''
    for number in matches:
        if number in number_list:
            result += number_list[number]
        else:
            result += number
    
    return int(result)