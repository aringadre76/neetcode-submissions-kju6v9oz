public class Solution {
    public int Search(int[] nums, int target) {
        return BinarySearch(0, nums.Length - 1, nums, target);
    }

    private int BinarySearch(int l, int r, int[] nums, int target) {
        if (l > r) {
            return -1;
        }

        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] < target) {
            return BinarySearch(mid + 1, r, nums, target);
        }
        else {
            return BinarySearch(l, mid - 1, nums, target);
        }
    }
}