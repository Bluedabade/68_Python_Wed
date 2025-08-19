def find_words_of_length(words, length):
    result = []
    for word in words:
        if len(word) == length:
            result.append(word)
    return result

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
length = 6

print(find_words_of_length(words, length))