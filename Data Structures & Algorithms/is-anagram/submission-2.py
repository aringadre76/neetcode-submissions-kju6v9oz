class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = [0] * 26, [0] * 26

        print(s_count)

        if len(s) != len(t): return False

        for i in range(len(s)):
            s_count[ord(s[i])-ord("a")] = s_count[ord(s[i])-ord("a")] + 1
            t_count[ord(t[i])-ord("a")] = t_count[ord(t[i])-ord("a")] + 1
        
        if s_count != t_count: return False
        
        return True


