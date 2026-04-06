class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_streak, val, res = 0, 0, 0
        
        nums = sorted(nums)
        for num in nums:
            curr_streak = 0
            val = num
            while True:
                val +=1
                curr_streak+=1

                if (val not in nums):
                    break
            
            if curr_streak > res:
                res = curr_streak
        
        return res