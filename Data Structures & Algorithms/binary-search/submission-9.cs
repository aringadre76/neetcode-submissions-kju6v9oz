public class Solution {
    public int Search(int[] nums, int target) {
        
        int l = 0;
        int r = nums.Length - 1;
        

        while (l <= r) {
            int mid = (l+r) / 2;

            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] < target) { // we throw away left slice
                l = mid + 1;
            }
            else { // throw away right slice
                r = mid -1;
            }
        }

        return -1;
    }

        
}