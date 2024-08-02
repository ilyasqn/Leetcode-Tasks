class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return len(s.split()[-1])




a = Solution()
print(a.lengthOfLastWord(s = "Hello World"))