class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if target ==  nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: # SORTED LEFT

                if target > nums[mid] or target < nums[l]: # we want right side
                    l = mid + 1
                
                else:                                      # we want left side
                    r = mid - 1
            
            elif nums[r] >= nums[mid]: # SORTED RIGHT

                if target < nums[mid] or target > nums[r]: # we want left side 
                    r = mid -1
                else:
                    l = mid + 1

        return -1
                


