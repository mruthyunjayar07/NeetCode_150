class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robRange(l, r):
            rob1 = rob2 = 0

            for i in range(l, r + 1):
                newRob = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2

        return max(
            robRange(0, len(nums) - 2),
            robRange(1, len(nums) - 1)
        )