from typing import List, Tuple
from collections import defaultdict
import heapq
def find_itinerary(tickets: List[Tuple[str, str]]) -> List[str]:
    graph = defaultdict(list)
    for u, v in tickets:
        heapq.heappush(graph[u], v)

    route = []
    stack = ["JFK"]  

    while stack:
        cur = stack[-1]
        if graph[cur]:
            nxt = heapq.heappop(graph[cur])
            stack.append(nxt)
        else:
            route.append(stack.pop())

    route.reverse()  

    if len(route) != len(tickets) + 1:
        return []  
    return route

print(find_itinerary([("MUC","LHR"),("JFK","MUC"),("SFO","SJC"),("LHR","SFO")]))
print(find_itinerary([("JFK","KUL"),("JFK","NRT"),("NRT","JFK")]))
