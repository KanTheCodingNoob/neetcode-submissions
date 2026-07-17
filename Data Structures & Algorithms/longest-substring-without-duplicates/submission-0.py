class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        maxLen = 0
        encountered = set()
        l, r = 0, 0
        dupe = None

        while r < n:
            if s[r] not in encountered:
                encountered.add(s[r])
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                dupe = s[r]
                while l < r:
                    encountered.remove(s[l])
                    if s[l] == dupe:
                        l += 1
                        break
                    l += 1
        return maxLen
