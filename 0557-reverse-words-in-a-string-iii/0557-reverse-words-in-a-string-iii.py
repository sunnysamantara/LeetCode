class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        rev=""
        for word in words:
            rev += word[::-1] +" "
        
        return rev.strip()