def solution(n, words):
    used_words = set()  
    prev_word = "" 
    
    for i, word in enumerate(words):
        if i > 0:
            prev_word = words[i - 1]
        
        player = (i % n) + 1
        
        turn = (i // n) + 1
        
        
        if word in used_words or (prev_word and word[0] != prev_word[-1]):
            return [player, turn]
         
        
        used_words.add(word)
    
    
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))  # [3, 3]
