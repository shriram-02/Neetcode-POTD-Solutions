class Solution {
public:
    int dp[101][101];
    int suffix[101];

    int solve(vector<int>& piles, int i, int m) {
        int n = piles.size();

        if (i >= n) return 0;

        if (2 * m >= n - i)
            return suffix[i];

        if (dp[i][m] != -1)
            return dp[i][m];

        int ans = 0;

        for (int x = 1; x <= 2 * m; x++) {
            ans = max(ans,
                      suffix[i] - solve(piles, i + x, max(m, x)));
        }

        return dp[i][m] = ans;
    }

    int stoneGameII(vector<int>& piles) {
        int n = piles.size();

        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                dp[i][j] = -1;
            }
        }

        suffix[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + piles[i];
        }

        return solve(piles, 0, 1);
    }
};