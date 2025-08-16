def average_length_of_strings(list_words):
    word_lenth = []
    for word in list_words:
        word_lenth.append(len(word))
    return(sum(word_lenth) / len(word_lenth))


list_words = []
for i in range(5):
    while(True):
        words = input(f"please enter word {i+1} :")
        if len(words) < 100 :
            list_words.append(words)
            break
        else:
            print("Out of range please try again.")


print(average_length_of_strings(list_words))