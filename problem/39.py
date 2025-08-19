def remove_word(sentence: str, word_to_remove: str):
    list_word = sentence.split()
    if word_to_remove not in list_word:
        return sentence
    list_word.remove(word_to_remove)
    join_sentence = ' '.join(list_word)
    return(join_sentence)


sentence = "Python is a popular programming language"
word_to_remove ="popularadad"

print(remove_word(sentence,word_to_remove))