class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    splitArray(nums, k) {
        let left = Math.max(...nums);
        let right = nums.reduce((sum, num) => sum + num, 0);

        const canSplit = (maxSum) => {
            let subarrays = 1;
            let currentSum = 0;

            for (let num of nums) {
                if (currentSum + num > maxSum) {
                    subarrays++;
                    currentSum = 0;
                }

                currentSum += num;
            }

            return subarrays <= k;
        };

        while (left < right) {
            let mid = Math.floor((left + right) / 2);

            if (canSplit(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}