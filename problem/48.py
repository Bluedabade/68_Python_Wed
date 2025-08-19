def cumulative_sum(n: int) -> int:
    result = 0
    for i in range(1,n+1):
        result+=i
    return result


n = 5

print(cumulative_sum(n))