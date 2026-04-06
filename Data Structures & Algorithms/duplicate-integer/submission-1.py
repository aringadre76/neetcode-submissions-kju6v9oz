class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, val in enumerate(nums):
            if idx+1 < len(nums): 
                if nums[idx] * 2 == nums[idx] + nums[idx+1]:
                    return True
        return False
