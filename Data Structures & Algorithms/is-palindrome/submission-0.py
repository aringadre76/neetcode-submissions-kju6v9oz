class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pattern = r'[a-z]|[0-9]'

        l, r = 0, len(s) - 1
        

        while l < r:
            print(s[l] + s[r])
            if re.match(pattern, s[l]) and re.match(pattern, s[r]):
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            else:
                if not (re.match(pattern, s[l])) and not (re.match(pattern, s[r])):
                    l+=1
                    r-=1
                elif not (re.match(pattern, s[l])):
                    l+=1
                elif not (re.match(pattern, s[r])):
                    r-=1
        return True