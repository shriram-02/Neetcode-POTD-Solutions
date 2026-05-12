class Solution {
    /**
     * @param {number} target
     * @param {MountainArray} mountainArr
     * @return {number}
     */
    findInMountainArray(target, mountainArr) {
        const n = mountainArr.length();

        // Find peak index
        let left = 0, right = n - 1;

        while (left < right) {
            let mid = Math.floor((left + right) / 2);

            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        const peak = left;

        // Binary search ascending part
        let result = this.binarySearch(mountainArr, target, 0, peak, true);

        if (result !== -1)
            return result;

        // Binary search descending part
        return this.binarySearch(mountainArr, target, peak + 1, n - 1, false);
    }

    binarySearch(arr, target, left, right, asc) {
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            let value = arr.get(mid);

            if (value === target)
                return mid;

            if (asc) {
                if (value < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                if (value > target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}