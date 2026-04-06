class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        l, r = 0, len(nums) - 1
        
        while l <= r:
            midIdx = (l + r) // 2

            if nums[midIdx] == target:
                return midIdx

            if nums[midIdx] > target:
                r = midIdx - 1
            
            if nums[midIdx] < target:
                l = midIdx + 1

        return -1
        