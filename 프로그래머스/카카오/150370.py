# level 1
# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    
    year, month, day = map(int, today.split("."))
    yearInt = (year - 2000) * 336
    monthInt = month * 28
    currentDayInt = yearInt + monthInt + day
    
    hashmap = {}
    result = []
    
    for term in terms:
        key, value = term.split(" ")
        hashmap[key] = int(value)
    
    index = 1
    
    # 약관
    for privacie in privacies:
        date, term = privacie.split(" ")

        nYear, nMonth, nDay = map(int, date.split("."))
        nYearInt = (nYear - 2000) * 336
        nMonthInt = nMonth * 28
        privacieDateInt = nYearInt + nMonthInt + nDay
        
        between = currentDayInt - privacieDateInt
        termMonth = hashmap[term]

        if(between >= termMonth * 28):
            result.append(index)

        index += 1
    
    return result

# solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])