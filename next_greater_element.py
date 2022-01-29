'''
https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/#
'''

class Solution:
    def nextLargerElement(self,arr,n):
        ans = [-1]*n
        stk = []
        stk.append(0)
        top = 0
        for i in range(1, n):
            while len(stk)!=0 and arr[i] >= arr[stk[top]]:
                ans[stk[top]]=arr[i]
                stk.pop()
                top -= 1
            stk.append(i)
            top += 1 
            
        return ans
