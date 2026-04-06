class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1: return [[strs[0]]]
        elif len(strs) == 0: return [[""]]
        
        res = [None] * len(strs)
        
        for i in range(len(strs)):
            res[i] = self.count(strs[i]) 
        
        print(res)
        
        realRes = []
        for i in range(len(strs)):
            outer = strs[i]
            outerList = []
            for j in range(len(strs)):
                
                comp = strs[j]
                if res[i] == res[j]:
                    outerList.append(j)

            if outerList not in realRes:
                realRes.append(outerList)
        print(realRes)

        defTheRes = []
        for i in range(len(realRes)):
            comb = []
            for j in range(len(realRes[i])):
                comb.append(strs[realRes[i][j]])
            defTheRes.append(comb)

        print(defTheRes)
        return defTheRes

    def count(self, string: str): 
        count = [0] * 26
        
        for c in string:
            count[ord(c) - ord("a")] += 1
        return count
