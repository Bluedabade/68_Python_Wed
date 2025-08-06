def sort_word_in_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = ' '.join(words)
    return sorted_sentence

sentence = "This is a man world"
sorted_result = sort_word_in_sentence(sentence)
print(f"sentence is : {sorted_result}")