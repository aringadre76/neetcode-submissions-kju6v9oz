class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for key, val in enumerate(nums):
            indices[val] = key

        # print(indices.values())

        for key, val in enumerate(nums):
            diff = target - val
            # print(diff)
            if diff in indices:
                if indices[diff] is not key:
                    return [min(indices[diff], key), max(indices[diff], key)]
