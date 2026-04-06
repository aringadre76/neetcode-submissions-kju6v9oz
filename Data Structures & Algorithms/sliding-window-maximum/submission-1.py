class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = nums[0:k]
        result = [0] * (len(nums) - k + 1)
        for i in range(len(nums)-k+1):
            print(f"curr: {curr}")
            result[i] = max(curr)
            if i + k < len(nums):
                del curr[0]
                curr.append(nums[i+k])
            # result[i] = max(curr)

        return result