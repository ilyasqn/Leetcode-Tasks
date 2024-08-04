class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char for char in s if char.isalnum()).lower()
        
        return s[::] == s[::-1]


a = Solution()
print(a.isPalindrome(s = ""))