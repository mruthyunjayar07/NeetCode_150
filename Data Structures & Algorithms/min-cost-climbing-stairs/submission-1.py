class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0

        for i in range(len(cost) - 1, -1, -1):
            curr = cost[i] + min(one, two)
            two = one
            one = curr

        return min(one, two)