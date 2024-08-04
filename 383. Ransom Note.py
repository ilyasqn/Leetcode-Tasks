class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magazine_sorted = ''.join(sorted(magazine))
        ransomNote_sorted = ''.join(sorted(ransomNote))
        
        
        i = 0
        j = 0
        while i < len(ransomNote_sorted) and j < len(magazine_sorted):
                if ransomNote_sorted[i] == magazine_sorted[j]:
                    i += 1
                j += 1
                
        return i == len(ransomNote_sorted)
        
a = Solution()
print(a.canConstruct(ransomNote = "bg", magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))




# test case 1:
# ransomNote = "aa", magazine = "ab"
# false
#
# tes case 2:
# ransomNote = "aa", magazine = "aab"
# true
#
# test case 3:
# ransomNote = 'bg', magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
# true

# test case 4:
# ransomNote = 'aab', magazine = "baa"
# true


# chejaccdae, "geceeibccchjejhdd"
# false