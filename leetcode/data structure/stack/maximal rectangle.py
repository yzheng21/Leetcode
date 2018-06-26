class solution:
    def largestRecArea(self, height):
        stack = []
        i = 0
        area = 0
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                cur = stack.pop()
                width = i if not stack else i - stack[-1] -1
                area = max(area,width * height[cur])
                i -= 1
            i += 1

        while stack:
            cur = stack.pop()
            width = len(height) if not stack else len(height) - stack[-1] -1
            area = max(area, width * height[cur])
        return area

    def maximalRectangle(self,matrix):
        if not matrix:
            return 0
        a = [0 for i in range(len(matrix[0]))]
        maxarea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j] = a[j] + 1 if matrix[i][j] else 0
            maxarea = max(maxarea,self.largestRecArea(a))
        return maxarea

