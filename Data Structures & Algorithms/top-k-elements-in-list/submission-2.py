class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1]))
        print(sorted_dict)
        num, count = list(sorted_dict.keys())[::-1], list(sorted_dict.values())[::-1]
        
        print(num)
        print(count)
        res = []
        i = 0
        while k > 0:
            res.append(num[i])
            i += 1
            k -= 1
        return res
        
        