
#  Here is the solution of the  69. Sqrt(x) LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #  Here is the solution:
        while val in nums:
            nums.remove(val)
        return len(nums)


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
my_list = [0,1,2,2,3,0,4,2]
number = 2

smth = Solution()
print(smth.removeElement(nums=my_list,val=number))

