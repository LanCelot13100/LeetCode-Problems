
#  Here is the solution of the 136. Single Number LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  Here is the solution:
        new_list = []
        bad_list = []

        for row in nums:
            if row in new_list:
                bad_list.append(row)
                continue
            new_list.append(row)

        for row2 in bad_list:
            while row2 in nums:
                nums.remove(row2)

        number = nums[0]
        return number


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [2,2,1]

variable = Solution()
print(variable.singleNumber(nums=numbers))

