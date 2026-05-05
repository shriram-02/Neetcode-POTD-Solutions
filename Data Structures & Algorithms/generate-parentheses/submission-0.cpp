class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack("", 0, 0, n, result);
        return result;
    }

    void backtrack(string curr, int open, int close, int n, vector<string>& result) {
        if (curr.size() == 2 * n) {
            result.push_back(curr);
            return;
        }

        if (open < n) {
            backtrack(curr + "(", open + 1, close, n, result);
        }

        if (close < open) {
            backtrack(curr + ")", open, close + 1, n, result);
        }
    }
};