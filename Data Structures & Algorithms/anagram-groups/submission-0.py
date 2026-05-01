class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordSet = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in wordSet:
                wordSet[sortedWord] = [word]
            else:
                wordSet[sortedWord].append(word)
        array = []
        for i in wordSet.values():
            array.append(i)
        return array