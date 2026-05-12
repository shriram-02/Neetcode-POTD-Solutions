class Solution {
public:
    unordered_map<string, vector<pair<string, double>>> graph;

    double dfs(string src, string dst, unordered_set<string>& visited, double product) {
        if (src == dst)
            return product;

        visited.insert(src);

        for (auto& neighbor : graph[src]) {
            string next = neighbor.first;
            double value = neighbor.second;

            if (!visited.count(next)) {
                double result = dfs(next, dst, visited, product * value);

                if (result != -1.0)
                    return result;
            }
        }

        return -1.0;
    }

    vector<double> calcEquation(vector<vector<string>>& equations,
                                vector<double>& values,
                                vector<vector<string>>& queries) {

        for (int i = 0; i < equations.size(); i++) {
            string a = equations[i][0];
            string b = equations[i][1];
            double val = values[i];

            graph[a].push_back({b, val});
            graph[b].push_back({a, 1.0 / val});
        }

        vector<double> answer;

        for (auto& q : queries) {
            string src = q[0];
            string dst = q[1];

            if (!graph.count(src) || !graph.count(dst)) {
                answer.push_back(-1.0);
                continue;
            }

            unordered_set<string> visited;
            answer.push_back(dfs(src, dst, visited, 1.0));
        }

        return answer;
    }
};