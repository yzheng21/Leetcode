class solution:
    def traprainwater(self,heights):
        if not heights or len(heights) < 2:
            return 0
        left,right = 0, len(heights)-1
        left_height = heights[left]
        right_height = heights[right]
        result = 0
        while left < right:
            if left_height < right_height:
                left += 1
                if heights[left] <= left_height:
                    result += left_height - heights[left]
                else:
                    left_height = heights[left]
            else:
                right -= 1
                if heights[right] <= right_height:
                    result += right_height - heights[right]
                else:
                    right_height = heights[right]
        return result
