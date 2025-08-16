def collect_unique_words():
    words = []
    while (len(words) < 5):
        word = input("Enter word: ")
        if word not in words:
            words.append(word)
    return(words)

print(collect_unique_words())