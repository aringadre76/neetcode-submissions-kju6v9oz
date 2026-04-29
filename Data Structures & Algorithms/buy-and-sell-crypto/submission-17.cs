public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;


        while (r < prices.Length) {
            int diff = prices[r]-prices[l];
            if (diff > 0) { // some profit
                if (diff > profit) { // current max profit
                    profit = diff;
                }
            }
            else { // absolutely 0 profit
                l = r;
            }
            r++;
        }
        return profit;
    }
}
