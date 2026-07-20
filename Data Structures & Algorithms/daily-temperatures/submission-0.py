class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        array = [0] * n

        for i in range(n):
            while (len(stack) > 0) and (temperatures[i] > stack[-1][1]):
                temp = stack.pop()
                array[temp[0]] = i - temp[0]
            stack.append((i, temperatures[i]))
        
        return array