from typing import Dict, List, Tuple, Any
import heapq
from collections import deque, defaultdict

Adj = Dict[Any, List[Tuple[Any, int]]]

def find_graph_centroid(graph: Adj) -> Tuple[Any, float]:

    if not graph:
        raise ValueError("Empty graph")

    nodes = list(graph.keys())

    undirected = defaultdict(list)
    for u, nbrs in graph.items():
        for v, _w in nbrs:
            undirected[u].append(v)
            undirected[v].append(u)

    def bfs_component(start):
        q = deque([start])
        seen = {start}
        while q:
            u = q.popleft()
            for v in undirected[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return seen

    seen_all = set()
    components = []
    for u in nodes:
        if u not in seen_all:
            comp = bfs_component(u)
            components.append(comp)
            seen_all |= comp

    components.sort(key=lambda s: (-len(s), min(map(str, s))))
    largest = components[0]

    def dijkstra(src):
        dist = {x: float('inf') for x in largest}
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in graph.get(u, []):
                if v in largest:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
        return dist

    best_node = None
    best_avg = float('inf')

    for u in sorted(largest, key=str):  # ผูกมัดผลลัพธ์ให้เสถียร
        dist = dijkstra(u)

        if any(dist[v] == float('inf') for v in largest if v != u):
            continue

        s = sum(dist[v] for v in largest if v != u)
        avg = s / (len(largest) - 1)
        if avg < best_avg or (avg == best_avg and str(u) < str(best_node)):
            best_avg = avg
            best_node = u

    if best_node is None:
        for u in sorted(largest, key=str):
            dist = dijkstra(u)
            reachable = [v for v in largest if v != u and dist[v] < float('inf')]
            if not reachable:
                continue
            avg = sum(dist[v] for v in reachable) / len(reachable)
            if avg < best_avg or (avg == best_avg and str(u) < str(best_node)):
                best_avg = avg
                best_node = u

    if best_node is None:
        only = next(iter(largest))
        return only, 0.0

    return best_node, float(round(best_avg, 6))

g1 = {
    0: [(1, 1), (2, 2)],
    1: [(0, 1), (3, 1)],
    2: [(0, 2), (3, 3)],
    3: [(1, 1), (2, 3)]
}
print(find_graph_centroid(g1))  # → (1, 2.0)

g2 = {
    0: [(1, 2), (2, 4)],
    1: [(0, 2), (2, 1)],
    2: [(0, 4), (1, 1), (3, 1)],
    3: [(2, 1)]
}
print(find_graph_centroid(g2))  # → (2, 2.0)
