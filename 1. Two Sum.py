class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in d:
                return [d[value], i]
            else:
                d[nums[i]] = i
        



a = Solution()
print(a.twoSum(nums = [3,2,4], target = 6))