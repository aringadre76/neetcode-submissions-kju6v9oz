class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False


        count_t, count_s = [0] * 10000, [0] * 10000

        for i in range(0, len(s)):

            count_t[ord(s[i])] += 1
            count_s[ord(t[i])] += 1

        return count_t == count_s