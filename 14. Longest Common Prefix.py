class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if "" in strs:
            return strs[0]
        
        
        strs = sorted(strs)
        fword = strs[0]
        lword = strs[len(strs) - 1]
        prefix = ''
        
        
        
        for i in range(len(fword)):
            if lword.startswith(fword):
                prefix = max(prefix, fword)
            fword = fword[:-1]

        return prefix
        
        
        
    
            
            
        
#When Strings are sorted alphabetically, the possibility of characters to be least
#common is between 1st and last member of the sorted strings.




a = Solution()
print(a.longestCommonPrefix(strs = ["flower","flow","flight"]))