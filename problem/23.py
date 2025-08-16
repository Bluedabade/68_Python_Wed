def create_dictionary(tuple1, tuple2):
    result = {}
    for key in tuple1:
        result[key] = ""
    for i, keys in enumerate(result):
        result[keys] = tuple2[i]
    return(result)


tuple1 = (1, 2, 3, 4)
tuple2 = ("ant", "cat", "dog", "cow")
print(create_dictionary(tuple1, tuple2))