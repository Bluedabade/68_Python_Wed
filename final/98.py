def min_cut_palindrome_partition(s: str) -> int:
    n = len(s)
    cuts = [i - 1 for i in range(n + 1)]  

    for center in range(n):
        l = r = center
        while l >= 0 and r < n and s[l] == s[r]:
            cuts[r + 1] = min(cuts[r + 1], cuts[l] + 1)
            l -= 1
            r += 1

        l, r = center, center + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cuts[r + 1] = min(cuts[r + 1], cuts[l] + 1)
            l -= 1
            r += 1

    return cuts[n]

print(min_cut_palindrome_partition("aab"))     
print(min_cut_palindrome_partition("abccba"))  
print(min_cut_palindrome_partition("aabbc"))   
print(min_cut_palindrome_partition("banana"))  
