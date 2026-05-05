class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        boolean a = false, b = false, c = false;

        for (int[] t : triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                if (t[0] == target[0]) a = true;
                if (t[1] == target[1]) b = true;
                if (t[2] == target[2]) c = true;
            }
        }

        return a && b && c;
    }
}