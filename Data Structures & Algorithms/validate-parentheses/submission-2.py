class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(', '}': '{', ']': '['}

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if hashmap[c] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0