class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        for idx, val in enumerate(nums):
            l, r = 0, len(nums) - 1

            while(l < idx and r > idx):
                if val + nums[l] + nums[r] == 0:
                    sumList = [nums[l], val, nums[r]]
                    if sumList not in res:
                        res.append([nums[l], val, nums[r]]) 
                    r -= 1
                    l += 1
                elif  val + nums[l] + nums[r] > 0:
                    r -= 1
                elif  val + nums[l] + nums[r] < 0:
                    l += 1


        print("res: ")
        print(res)
        return res
                    
