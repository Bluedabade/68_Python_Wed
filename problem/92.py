from typing import List

def min_edit_distance(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    dp: List[List[int]] = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # ลบ
                    dp[i][j-1],    # แทรก
                    dp[i-1][j-1],  # แทนที่
                )
    return dp[n][m]


print(min_edit_distance("kitten", "sitting"))  # 3
print(min_edit_distance("flaw", "lawn"))       # 2
