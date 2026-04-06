class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        left, right = 0, len(nums)-1

        while left <= right:
            middy = (left + right) // 2

            if nums[middy] > target:
                right = middy - 1
            elif nums[middy] < target:
                left = middy + 1 
            else: return middy
        
        return -1
