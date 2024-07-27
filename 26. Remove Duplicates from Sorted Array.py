class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums[:] = sorted(list(set(nums)))
        k = len(nums)
        
        return k
        



a = Solution()
print(a.removeDuplicates(nums = [-1,0,0,0,0,3,3]))