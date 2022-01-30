'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
may check youtube for explanation if needed.
'''

class Solution:
    def NextSmallLeft(self, heights):
        stk = []
        left = [-1]*len(heights)
        top = -1
        for i in reversed(range(len(heights))):
            if i == len(heights)-1:
                stk.append(len(heights)-1)
                top += 1
            else:
                while (len(stk)!=0 and heights[i] < heights[stk[top]]):
                    left[stk[top]] = i 
                    stk.pop()
                    top -= 1
                stk.append(i)
                top += 1
        return left
        
    def NextSmallRight(self, heights):
        stk = []
        right = [len(heights)]*len(heights)
        top = -1
        for i in range(len(heights)):
            if i == 0:
                stk.append(i)
                top += 1
            else:
                while len(stk)!=0 and heights[i] < heights[stk[top]]:
                    right[stk[top]] = i 
                    stk.pop()
                    top -= 1
                stk.append(i)
                top += 1
        return right

    def largestRectangleArea(self, heights) -> int:
        if len(heights) == 1:
            return heights[0]
        if heights.count(heights[0])==len(heights):
            return (sum(heights))

        left = self.NextSmallLeft(heights)
        right = self.NextSmallRight(heights)

        ans = []
        for i in range(len(heights)):
            ans.append(heights[i]*(right[i]-left[i]-1))
        return max(ans)
      
      
