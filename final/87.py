from functools import lru_cache
from math import inf
from typing import List

def tsp(graph: List[List[int]]) -> int:
    n = len(graph)
    ALL = (1 << n) - 1

    @lru_cache(None)
    def dp(pos: int, mask: int) -> int:
        if mask == ALL:
            return graph[pos][0] if graph[pos][0] != 0 or pos == 0 else inf
        best = inf
        for nxt in range(n):
            if not (mask & (1 << nxt)):
                w = graph[pos][nxt]
                if w == 0 and pos != nxt:  # เผื่อบางกราฟใช้ 0 แทนไม่มีเส้นทาง
                    continue
                cand = w + dp(nxt, mask | (1 << nxt))
                if cand < best:
                    best = cand
        return best

    return dp(0, 1)

g1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(g1))                    

g2 = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]
print(tsp(g2))                  
