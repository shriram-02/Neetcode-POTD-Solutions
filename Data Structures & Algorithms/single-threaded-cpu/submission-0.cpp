class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();

        vector<array<long long, 3>> arr;

        for (int i = 0; i < n; i++) {
            arr.push_back({tasks[i][0], tasks[i][1], i});
        }

        sort(arr.begin(), arr.end());

        priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > pq;

        vector<int> ans;

        long long time = 0;
        int i = 0;

        while (i < n || !pq.empty()) {
            if (pq.empty() && time < arr[i][0]) {
                time = arr[i][0];
            }

            while (i < n && arr[i][0] <= time) {
                pq.push({arr[i][1], arr[i][2]});
                i++;
            }

            auto [procTime, idx] = pq.top();
            pq.pop();

            time += procTime;
            ans.push_back(idx);
        }

        return ans;
    }
};