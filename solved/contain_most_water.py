class Solution:
    def maxArea1(self, height):
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
    
    def maxArea(self, height):
        s = 0
        e = len(height) - 1
        res = 0
        while e > s:
            res = max(res, min(height[s], height[e]) * (e - s))
            if height[e] < height[s]:
                e -= 1
            else:
                s += 1
        return res
    

h = [1, 3, 2, 1, 0, 2]
print(Solution().maxArea(h))
