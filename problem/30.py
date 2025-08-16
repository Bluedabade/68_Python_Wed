def calculate_set_differences(set1, set2):
    return(set1.difference(set2), set2.difference(set1))
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
print(calculate_set_differences(set1, set2))