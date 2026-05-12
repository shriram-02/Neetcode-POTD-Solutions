class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = 0;
        
        int curMax = 0, maxSum = nums[0];
        int curMin = 0, minSum = nums[0];
        
        for (int x : nums) {
            curMax = max(x, curMax + x);
            maxSum = max(maxSum, curMax);
            
            curMin = min(x, curMin + x);
            minSum = min(minSum, curMin);
            
            total += x;
        }
        
        if (maxSum < 0) return maxSum;
        
        return max(maxSum, total - minSum);
    }
};