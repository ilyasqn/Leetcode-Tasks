class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        nums[:] = [num for num in nums if num != val]
        k = len(nums)
        
        return k, nums
    





a = Solution()
print(a.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))