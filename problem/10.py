def character_frequency(words):
    result = {}
    for word in words:
        for char in word:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
                pass
    print(result)
words = []
for i in range (5):
    while(True):
        word = input(f"please input word {i+1}: ")
        if(len(word) < 50 ):
            words.append(word)
            break
        else:
            print("Out of range please try again")

character_frequency(words)
