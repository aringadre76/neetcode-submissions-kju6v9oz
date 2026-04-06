class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, value in enumerate(nums):
            my_dict[index] = value

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        print(sorted_dict)

        items = list(sorted_dict.items())

        left = 0
        right = len(items) - 1

        while left <= right:
            left_key, left_value = items[left]
            right_key, right_value = items[right]
            
            if left_value + right_value < target:
                left += 1
            elif left_value + right_value > target:
                right -= 1
            else:
                if left_key > right_key:
                    return [right_key, left_key]
                else:
                    return [left_key, right_key]