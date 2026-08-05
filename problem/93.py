from collections import defaultdict, Counter
from typing import List, Dict

def group_anagrams(words: List[str], by_frequency: bool = False) -> Dict[int, List[List[str]]]:
    def signature(word: str):
        cnt = [0] * 26
        for ch in word:
            cnt[ord(ch) - 97] += 1
        return tuple(cnt)

    freq = Counter(words)

    buckets = defaultdict(lambda: defaultdict(list))
    for w in words:
        buckets[len(w)][signature(w)].append(w)

    result: Dict[int, List[List[str]]] = {}
    for length, sig2group in buckets.items():
        groups = list(sig2group.values())

        if by_frequency:
            groups.sort(key=lambda g: (-sum(freq[w] for w in g), [min(g)]))
        else:
            groups.sort(key=lambda g: (-len(g), [min(g)]))

        result[length] = groups

    return result
words1 = ["bat", "tab", "cat", "act", "tac", "rat", "tar", "art", "star", "rats"]
print(group_anagrams(words1))

words2 = ["listen", "silent", "enlist", "inlets", "google", "gogole", "elgoog", "cat", "tac", "act"]
print(group_anagrams(words2))
