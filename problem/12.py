def replace_characters(word):
    word = word.replace("a","@")
    word = word.replace("l","1")
    word = word.replace("o","0")
    return(word)

word = input("Please input word: ")
print(replace_characters(word))