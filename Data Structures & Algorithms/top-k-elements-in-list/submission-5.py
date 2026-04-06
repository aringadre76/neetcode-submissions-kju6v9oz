class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq = [[] for _ in range(len(nums)+1)]
        print(freq)

        for key, value in count.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            # print(i)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
            