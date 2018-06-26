class solution:
    def maxarea(self,height):
        left,right = 0,len(height)
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -=  1
            ans = max(ans, area)
        return ans