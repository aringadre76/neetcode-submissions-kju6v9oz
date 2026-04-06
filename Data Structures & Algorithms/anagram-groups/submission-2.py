class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        temp = []
        for s1 in strs:
            for s2 in strs:
                if ''.join(sorted(s1)) == ''.join(sorted(s2)):
                    temp.append(s2)
            if temp not in res:
                res.append(temp)
            temp = []
            
        
        print(res)
        return res

            

            
        