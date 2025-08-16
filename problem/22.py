def create_dictionary(list1, list2):
    result = {}
    for key in list1:
        result[key] = ""
    for i, keys in enumerate(result):
        result[keys] = list2[i]
    return(result)


list1 = [1, 2, 3, 4]
list2 = ["blue", "green", "pink", "yellow"]
print(create_dictionary(list1, list2))