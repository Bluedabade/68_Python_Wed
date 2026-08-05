from functools import lru_cache

def word_break(s: str, word_set: set) -> bool:
    if not s:
        return False
    if not word_set:
        return False

    max_len = max(len(w) for w in word_set)

    @lru_cache(None)
    def dfs(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, min(len(s), i + max_len) + 1):
            if s[i:j] in word_set and dfs(j):
                return True
        return False

    return dfs(0)

print(word_break("leetcode", {"leet", "code"}))            # True
print(word_break("applepenapple", {"apple", "pen"}))       # True
print(word_break("catsandog", {"cats","dog","sand","and","cat"}))  # False
