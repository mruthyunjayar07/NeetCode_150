class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        win_count = [0] * 26

        # Build initial frequency counts
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            win_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == win_count:
            return True

        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            win_count[ord(s2[i]) - ord('a')]           += 1  # add new right char
            win_count[ord(s2[i - len(s1)]) - ord('a')] -= 1  # remove old left char

            if s1_count == win_count:
                return True

        return False