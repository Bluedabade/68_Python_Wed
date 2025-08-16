def contains_vowel(word):
    vowel = ['a','e','i','o','u']
    is_vowel = False
    for char in word:
        if char.lower() in vowel:
            is_vowel = True
    return(is_vowel)
word = input("Enter your word: ")
print(contains_vowel(word))
