from typing import List
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))

            return ans

        res = dfs(amount)
        return -1 if res == float('inf') else res