class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        vector<bool> dp(n, false);
        dp[0] = true;

        int reachable = 0;

        for (int i = 1; i < n; i++) {
            if (i >= minJump && dp[i - minJump])
                reachable++;

            if (i > maxJump && dp[i - maxJump - 1])
                reachable--;

            dp[i] = (reachable > 0 && s[i] == '0');
        }

        return dp[n - 1];
    }
};