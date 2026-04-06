class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        alpha_sorted = []
        for s in strs:
            s_sorted = ''.join(sorted(s))
            alpha_sorted.append(s_sorted)
        print(alpha_sorted)
        
        temp = []
        for a in alpha_sorted:
            for s in strs:
                if a == ''.join(sorted(s)):
                    temp.append(s)
            if temp not in res:
                res.append(temp)
            temp = []
            
        
        print(res)
        return res

            

            
        