class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<bool>> reach(numCourses, vector<bool>(numCourses, false));

        for (auto &p : prerequisites) {
            reach[p[0]][p[1]] = true;
        }

        for (int k = 0; k < numCourses; k++) {
            for (int i = 0; i < numCourses; i++) {
                for (int j = 0; j < numCourses; j++) {
                    reach[i][j] = reach[i][j] || (reach[i][k] && reach[k][j]);
                }
            }
        }

        vector<bool> ans;

        for (auto &q : queries) {
            ans.push_back(reach[q[0]][q[1]]);
        }

        return ans;
    }
};