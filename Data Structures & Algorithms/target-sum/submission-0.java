class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for (int num : nums) sum += num;
        
        if ((sum + target) % 2 != 0 || Math.abs(target) > sum) return 0;
        
        int subsetSum = (sum + target) / 2;
        
        int[] dp = new int[subsetSum + 1];
        dp[0] = 1;
        
        for (int num : nums) {
            for (int i = subsetSum; i >= num; i--) {
                dp[i] += dp[i - num];
            }
        }
        
        return dp[subsetSum];
    }
}