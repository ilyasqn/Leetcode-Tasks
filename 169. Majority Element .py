class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # d = {i: nums.count(num) for i, num in enumerate(nums)}
        #
        # max_index = max(d, key=d.get)
        #
        # return nums[max_index]
        
        count = 0
        res = -1
        for i in range(len(nums)):
            if nums[i] == res:
                count += 1
            elif count == 0:
                res = nums[i]
                count = 1
            else:
                count -= 1
        return res

a = Solution()
print(a.majorityElement(nums = [6,6,6,7,7]))