class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_area = 0
        area=0
        while i<j:
            if height[i] < height[j]:
                
                area = min(height[i],height[j]) * (j-i)
                max_area=max(max_area,area)
                i+=1
            elif height[i]>height[j]:
                
                area = min(height[i],height[j]) * (j-i)
                max_area=max(max_area,area)
                j=j-1
            else:
                area = min(height[i],height[j]) * (j-i)
                max_area=max(max_area,area)
                i+=1
        return max_area