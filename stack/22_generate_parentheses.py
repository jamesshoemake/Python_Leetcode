from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openC, closedC):
            if openC == closedC == n:
                res.append("".join(stack))

            if openC < n:
                stack.append("(")
                backtrack(openC+1, closedC)
                stack.pop()

            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC+1)
                stack.pop()
        backtrack(0, 0)
        return res
