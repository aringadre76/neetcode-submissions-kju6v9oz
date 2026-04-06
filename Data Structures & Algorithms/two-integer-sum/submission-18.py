class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        sorted_arr = {}

        for i, n in enumerate(nums):
            sorted_arr[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sorted_arr.keys():
                if sorted_arr[diff] != i:
                    return [min(i, sorted_arr[diff]), max(i, sorted_arr[diff])]
        return []