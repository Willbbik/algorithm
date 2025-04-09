def solution(cacheSize, cities):
    
    arr = []
    cnt = 0
    
    for city in cities:
        
        city = city.lower()
    
        if city in arr:
            arr.remove(city)
            arr.insert(0, city)
            cnt += 1
        else:
            cnt += 5

            if(cacheSize == 0):
                continue
            elif(len(arr) >= cacheSize):
                arr.pop(cacheSize-1)
            arr.insert(0, city)

    return cnt