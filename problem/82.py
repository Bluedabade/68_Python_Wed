def find_permutations(s: str) -> list:
    if len(s) == 1:
        return [s]
    
    perms = []
    for i in range(len(s)):
        first = s[i]               
        remaining = s[:i] + s[i+1:]  
        for p in find_permutations(remaining):
            perms.append(first + p)
    return perms

result = find_permutations("abc")
print(result)
