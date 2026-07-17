class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char = [0] * 26
        s2_char = [0] * 26

        for c in s1:
            s1_char[ord(c) - ord('a')] += 1
        
        n1 = len(s1)
        n2 = len(s2)
        l, r = 0, 0
        while r < n2:
            s2_char[ord(s2[r]) - ord('a')] += 1
            
            if (r - l + 1) == n1:
                if s1_char == s2_char:
                    return True
                else:
                    s2_char[ord(s2[l]) - ord('a')] -= 1
                    l += 1
            r += 1
        return False