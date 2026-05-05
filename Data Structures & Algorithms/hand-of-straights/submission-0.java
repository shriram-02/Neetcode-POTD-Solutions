class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;

        java.util.Map<Integer, Integer> count = new java.util.TreeMap<>();
        
        for (int num : hand) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for (int num : count.keySet()) {
            int freq = count.get(num);
            if (freq > 0) {
                for (int i = 0; i < groupSize; i++) {
                    int curr = num + i;
                    if (count.getOrDefault(curr, 0) < freq) {
                        return false;
                    }
                    count.put(curr, count.get(curr) - freq);
                }
            }
        }

        return true;
    }
}