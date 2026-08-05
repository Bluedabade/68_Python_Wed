from typing import List, Tuple, Dict
import heapq

def network_delay_time(times: List[Tuple[int, int, int]], N: int, K: int) -> int:
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, N+1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, N+1)}
    dist[K] = 0
    pq = [(0, K)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    ans = max(dist.values())
    return -1 if ans == float('inf') else ans


def network_delay_time_with_path(times: List[Tuple[int,int,int]], N: int, K: int):
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, N+1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, N+1)}
    parent = {i: None for i in range(1, N+1)}  
    dist[K] = 0
    pq = [(0, K)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    if any(dist[i] == float('inf') for i in range(1, N+1)):
        return -1, []

    slowest = max(range(1, N+1), key=lambda x: dist[x])
    delay = dist[slowest]

    path = []
    cur = slowest
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return delay, path


# --------------- Quick tests ---------------
if __name__ == "__main__":
    print(network_delay_time([(2,1,1),(2,3,1),(3,4,1)], 4, 2))  # 2
    print(network_delay_time([(1,2,1),(2,3,2),(1,3,4)], 3, 1))  # 3
    print(network_delay_time([(1,2,1),(1,3,2),(2,4,1),(3,4,2),(4,5,1),(5,6,2),(1,6,4)], 6, 1))  # 4

    print(network_delay_time_with_path([(2,1,1),(2,3,1),(3,4,1)], 4, 2))  # (2, [2,3,4])
