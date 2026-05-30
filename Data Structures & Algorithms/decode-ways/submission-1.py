class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp1, dp2 = 1, 1

        for i in range(1, len(s)):
            curr = 0

            if s[i] != '0':
                curr += dp2

            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                curr += dp1

            dp1, dp2 = dp2, curr

        return dp2