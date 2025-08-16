def count_word_occurrences(words):
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return(word_count)


words = ["apple","banana","apple","orange","banana","apple"]
print(count_word_occurrences(words))