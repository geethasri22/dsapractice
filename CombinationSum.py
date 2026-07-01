class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # sort to handle duplicates
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(list(path))
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, remaining - candidates[i])  # move forward
                path.pop()  # undo choice

        backtrack(0, [], target)
        return res
