class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        stored = {}

        for idx, num in enumerate(nums):
            stored[num] = idx

        for idx, num in enumerate(nums):

            diff = target - num

            if diff in nums: # diff is there

                if stored[diff] != idx: # diff is a diff value
                # find diff
                    return [min(idx, stored[diff]), max(idx, stored[diff])]
            
