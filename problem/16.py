def insert_at_front(words):
    result = []
    for word in words:
        print(f"Add word: {word} ->",end="") 
        result.append(word)
        result.reverse()
        print(f"List become{result}")
    return(result)

words = ["apple","kuy", "banana", "cherry"]
print(insert_at_front(words))
