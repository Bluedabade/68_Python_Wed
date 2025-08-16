def separate_by_index(word):
    even_char = ""
    odd_char = ""
    if(len(word) > 100):
        print("out of range")
        return(None)
    for i , char in enumerate(word):
        if i == 0 or i % 2 == 0 :
            even_char += char
        else:
            odd_char += char
    print(even_char, odd_char)    
    
    


word = input("Enter word: ")
separate_by_index(word)