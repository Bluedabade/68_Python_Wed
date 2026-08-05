from typing import List

def max_sum_with_one_deletion(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return arr[0]

    keep = arr[0]            
    delete = float('-inf')   
    ans = arr[0]

    for i in range(1, n):
        x = arr[i]
        new_delete = max(delete + x, keep)  
        keep = max(keep + x, x)            
        delete = new_delete
        ans = max(ans, keep, delete)

    return ans


print(max_sum_with_one_deletion([1, -2, 0, 3]))   
print(max_sum_with_one_deletion([1, -2, -2, 3]))  
print(max_sum_with_one_deletion([-1, -1, -1, -1]))
