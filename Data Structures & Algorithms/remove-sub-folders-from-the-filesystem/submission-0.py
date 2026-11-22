class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []

        for f in folder:
            if not ans or not f.startswith(ans[-1] + "/"):
                ans.append(f)

        return ans