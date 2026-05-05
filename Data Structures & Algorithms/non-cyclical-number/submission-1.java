class Solution {
    public boolean isHappy(int n) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            int sum = 0;
            
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            
            n = sum;
        }
        
        return n == 1;
    }
}