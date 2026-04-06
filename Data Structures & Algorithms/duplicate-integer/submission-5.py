class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        nums.sort()
        previous = nums[0]

        for i in range(1, len(nums)):
            if previous == nums[i]:
                return True
            previous = nums[i]
        return False