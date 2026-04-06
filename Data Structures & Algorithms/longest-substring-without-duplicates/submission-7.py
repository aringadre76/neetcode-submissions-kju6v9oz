class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = ""
        window = 1
        l, r, = 0, window
        if ''.join(dict.fromkeys(s)) == s:
            return len(s)

        
        for window_size in range(len(s)):
            l, r, = 0, window_size
            for i in range(len(s)):
                if len(''.join(dict.fromkeys(s[l:r])))>len(longest) and ''.join(dict.fromkeys(s[l:r])) in s[l:r]: 
                    longest = ''.join(dict.fromkeys(s[l:r]))

                l+=1
                r+=1
        print(longest)
        return 1 if len(s) == 1 else len(longest)