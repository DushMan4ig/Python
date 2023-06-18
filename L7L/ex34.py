def check_rhythm(poem):
    lines = poem.split(" ")
    syllables = []
    
    for line in lines:
        words = line.split("-")
        syllables_per_word = []
        
        for word in words:
            syllables_count = sum(1 for char in word if char.lower() in 'aeiouаеёиоуыэюя')
            syllables_per_word.append(syllables_count)
        
        if len(set(syllables_per_word)) != 1:
            return "Пам парам"
        
        syllables.append(sum(syllables_per_word))
    
    if len(set(syllables)) != 1:
        return "Пам парам"
    
    return "Парам пам-пам"

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)