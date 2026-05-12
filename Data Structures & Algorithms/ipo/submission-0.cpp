class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        vector<pair<int, int>> projects;

        for (int i = 0; i < profits.size(); i++) {
            projects.push_back({capital[i], profits[i]});
        }

        sort(projects.begin(), projects.end());

        priority_queue<int> maxHeap;

        int i = 0;
        int n = projects.size();

        while (k--) {
            while (i < n && projects[i].first <= w) {
                maxHeap.push(projects[i].second);
                i++;
            }

            if (maxHeap.empty())
                break;

            w += maxHeap.top();
            maxHeap.pop();
        }

        return w;
    }
};