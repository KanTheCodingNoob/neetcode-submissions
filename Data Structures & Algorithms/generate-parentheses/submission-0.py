class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cLimit = n * 2

        def backtrack(string = [], lCount = 0, rCount = 0):
            if len(string) == cLimit and lCount == rCount:
                res.append(''.join(string))
            if lCount < n:
                lCount += 1
                string.append('(')
                backtrack(string, lCount, rCount)
                string.pop()
                lCount -= 1
            if rCount < n and lCount > rCount:
                rCount += 1
                string.append(')')
                backtrack(string, lCount, rCount)
                string.pop()
                rCount -= 1
        
        backtrack()

        return res