from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)

            if buying:
                return max(
                    dfs(i + 1, 0) - prices[i],
                    cooldown
                )
            else:
                return max(
                    dfs(i + 2, 1) + prices[i],
                    cooldown
                )

        return dfs(0, 1)