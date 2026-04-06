class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count_s, count_t = [0] * 10000, [0] * 10000

        for i in range(0, len(t)):
            count_s[ord(s[i])] += 1
            count_t[ord(t[i])] += 1
        return count_s == count_t
