from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        window = len(s1)

        for r in range(len(s2) - window + 1):
            temp = s2[r:r + window]
            print(temp)  
            tempCount = Counter(temp)
            if tempCount == s1count:
                return True

        return False
