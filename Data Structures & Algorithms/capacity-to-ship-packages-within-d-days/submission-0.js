class Solution {
    /**
     * @param {number[]} weights
     * @param {number} days
     * @return {number}
     */
    shipWithinDays(weights, days) {
        let left = Math.max(...weights);
        let right = weights.reduce((a, b) => a + b, 0);

        const canShip = (capacity) => {
            let daysNeeded = 1;
            let currentWeight = 0;

            for (let weight of weights) {
                if (currentWeight + weight > capacity) {
                    daysNeeded++;
                    currentWeight = 0;
                }

                currentWeight += weight;
            }

            return daysNeeded <= days;
        };

        while (left < right) {
            let mid = Math.floor((left + right) / 2);

            if (canShip(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}