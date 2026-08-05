from typing import List

def can_partition_k_subsets(nums: List[int], k: int) -> bool:
    total = sum(nums)
    if k <= 0 or total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target:
        return False

    used = [False] * len(nums)

    def backtrack(bucket_idx: int, start: int, curr_sum: int) -> bool:
        if bucket_idx == k - 1:
            return True
        if curr_sum == target:
            return backtrack(bucket_idx + 1, 0, 0)

        prev = -1  
        for i in range(start, len(nums)):
            if used[i] or nums[i] == prev:
                continue
            nxt = curr_sum + nums[i]
            if nxt > target:
                continue

            used[i] = True
            if backtrack(bucket_idx, i + 1, nxt):
                return True
            used[i] = False
            prev = nums[i]
            if curr_sum == 0:
                break
        return False

    return backtrack(0, 0, 0)

print(can_partition_k_subsets([4,3,2,3,5,2,1], 4))  # True
print(can_partition_k_subsets([1,2,3,4], 3)) 