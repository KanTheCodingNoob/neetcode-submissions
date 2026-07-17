class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        array = [0] * 26
        l, r = 0, 0
        longest = 0

        while r < n:
            array[ord(s[r]) - ord('A')] += 1
            while (((r - l) + 1) - max(array)) > k:
                array[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, (r-l+1))
            r += 1

        return longest