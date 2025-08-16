def set_operations(set1, set2):
    return(sorted(set1.union(set2)) , sorted(set1.intersection(set2)))


set1 = {'a', 'e', 'i', 'o', 'u'}
set2 = {'h', 'e', 'l', 'l', 'o'}
print(set_operations(set1, set2))