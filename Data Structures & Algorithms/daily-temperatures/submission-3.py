class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i , n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                popped_inx = stack.pop()
                output[popped_inx] = i - popped_inx
            stack.append(i)
        return output