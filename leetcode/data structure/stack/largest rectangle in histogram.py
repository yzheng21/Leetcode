class solution:
    def largestRectangleArea(self,height):
        if not height or len(height) == 0:
            return 0
        stack = []
        area = 0
        i = 0
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if not stack else i - stack[-1] -1
                area = max(area,width*height[curr])
                i -= 1
            i += 1

        while stack:
            curr = stack.pop()
            width = len(height) if not stack else len(height) - stack[-1] -1
            area = max(area,width*height[curr])
        return area

s = solution()
height = [2,1,5,6,2,3]
print(s.largestRectangleArea(height))