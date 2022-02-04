'''
https://leetcode.com/problems/number-of-visible-people-in-a-queue/
'''

class Solution:
    def nextGreaterLeft(self, heights):
        stk = []
        n = len(heights)
        ans = [0]*n
        for i in range(n-1,-1,-1):
            count = 0
            while len(stk)!=0 and heights[i]>stk[-1]:
                stk.pop()
                count += 1
            if len(stk)!= 0:
                count += 1
            stk.append(heights[i])
            ans[i] = count 
        return ans
 

    def canSeePersonsCount(self, heights: List[int]) -> List[int]: 
        return (self.nextGreaterLeft(heights))
