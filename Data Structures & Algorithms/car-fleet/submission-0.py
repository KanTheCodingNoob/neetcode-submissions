class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        array = [None] * n
        for i in range(n):
            array[i] = (position[i], speed[i])
        
        array.sort(reverse=True)
        stack = []

        for p, s in array:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)