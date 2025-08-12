#  Here is the solution of the 28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        while True:
            if needle in haystack:
                index = haystack.index(needle)
                return index
            else:
                return -1


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
word = "sadbutsad"
part = "sad"

variable = Solution()
print(variable.strStr(haystack=word,needle=part))

