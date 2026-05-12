class Solution {
public:
    long long minEnd(int n, int x) {
        long long ans = x;
        long long k = n - 1;

        for (int bit = 0; bit < 63; bit++) {
            if ((x & (1LL << bit)) == 0) {
                if (k & 1LL) {
                    ans |= (1LL << bit);
                }
                k >>= 1;
            }
        }

        return ans;
    }
};
