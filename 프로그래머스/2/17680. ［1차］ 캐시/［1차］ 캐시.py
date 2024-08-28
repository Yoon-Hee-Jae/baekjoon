def solution(cacheSize, cities):
    cache = []  
    total_time = 0 
    
    for city in cities:
        city = city.lower()  
        
        if city in cache:  
            cache.remove(city)  
            cache.append(city)  
            total_time += 1
        else:  
            if len(cache) == cacheSize:  
                if cacheSize > 0:  
                    cache.pop(0)  
            if cacheSize > 0:  
                cache.append(city) 
            total_time += 5
            
    return total_time