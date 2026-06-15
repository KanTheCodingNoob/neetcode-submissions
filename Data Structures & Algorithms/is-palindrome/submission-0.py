class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = []
        for c in s:
            if c != ' ' and (c >= '0' and c <= '9') or (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                newString.append(c.lower())
        
        p1, p2 = 0, len(newString) -1
        while p1 < p2:
            if newString[p1] != newString[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True