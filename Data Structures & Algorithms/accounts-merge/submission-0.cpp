class Solution {
public:
    vector<int> parent;

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }

    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        parent.resize(n);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        unordered_map<string, int> emailToAccount;

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < accounts[i].size(); j++) {
                string email = accounts[i][j];

                if (emailToAccount.count(email)) {
                    unite(i, emailToAccount[email]);
                } else {
                    emailToAccount[email] = i;
                }
            }
        }

        unordered_map<int, set<string>> merged;

        for (auto& [email, idx] : emailToAccount) {
            int root = find(idx);
            merged[root].insert(email);
        }

        vector<vector<string>> result;

        for (auto& [idx, emails] : merged) {
            vector<string> account;
            account.push_back(accounts[idx][0]);

            for (auto& email : emails) {
                account.push_back(email);
            }

            result.push_back(account);
        }

        return result;
    }
};