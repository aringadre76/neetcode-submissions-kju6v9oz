class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for idx, val in enumerate(nums):
            left = nums[0:idx]
            right = nums[idx+1:len(nums)]
            print(left)
            print(right)
            product = math.prod(left+right)
            res.append(product)
        print(res)
        return res
            