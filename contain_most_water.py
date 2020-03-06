class Solution:
    def maxArea(self, height):
        res = 0
        data = {}
        for i in range(len(height)):
            area = 0
            if height[i] not in data:
                for j in range(i+1,len(height)):
                    area = max(area, min(height[i], height[j]) * (j - i))
                data[i] = area
                res = max(res, area)
        return res


h = [1, 3, 2, 1, 0, 2]
print(Solution().maxArea(h))
