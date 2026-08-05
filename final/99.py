from typing import List, Tuple

def min_meeting_rooms(intervals: List[Tuple[int, int]]) -> int:
    if not intervals:
        return 0
    starts = sorted(s for s, _ in intervals)
    ends   = sorted(e for _, e in intervals)
    i = j = 0
    rooms = max_rooms = 0

    while i < len(starts):
        if starts[i] < ends[j]:
            rooms += 1           
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1           #
            j += 1
    return max_rooms



print(min_meeting_rooms([(0,30),(5,10),(15,20)]))        
print(min_meeting_rooms([(7,10),(2,4)]))                 
print(min_meeting_rooms([(1,5),(2,6),(3,8),(5,7),(8,9)]))

