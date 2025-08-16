def remove_word_from_list(words):
    remove_word = input("Which word u want to remove?: ")
    if remove_word in words:
        words.remove(remove_word)
    return(words)
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape","honeydew", "kiwi", "lemon"]
print(remove_word_from_list(words))