#  Here is the solution of the 14. Longest Common Prefix LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        base_prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(base_prefix):
                base_prefix = base_prefix[:-1]

        return base_prefix




#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
line = ["flower","flow","flight"]

variable = Solution()
print(variable.longestCommonPrefix(strs=line))
