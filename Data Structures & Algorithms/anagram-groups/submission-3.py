class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = []
        # temp = []
        # for s1 in strs:
        #     for s2 in strs:
        #         if ''.join(sorted(s1)) == ''.join(sorted(s2)):
        #             temp.append(s2)
        #     if temp not in res:
        #         res.append(temp)
        #     temp = []
            
        
        # print(res)
        # return res


        my_dict = {}
        res = []
        for k, v in enumerate(strs):
            if ''.join(sorted(v)) not in my_dict:
                my_dict[''.join(sorted(v))] = [k]
            else:
                my_dict[''.join(sorted(v))].append(k)
            
        for key, indices in my_dict.items():
            associated_strings = [strs[i] for i in indices]
            res.append(associated_strings)

        print(my_dict)
        return res

            

            
        