
#  Here is the solution of the 283. Move Zeroes LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #  Here is the solution:

        #  Firstly, we have to create the special list for those integers that we want to move
        zero_list = []

        #  Secondly, we have to declare the integers that we want to move by assigning them to variables
        i = 0

        #  While the assigned integers in the main list, we have to remove them from the list and move them to the created one
        while i in nums:
            nums.remove(0)
            zero_list.append(0)

        #  Finally, we have to modify the main list by extending that with the created list and return that
        nums.extend(zero_list)
        return nums


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [0,0,1]


variable = Solution()
print(variable.moveZeroes(nums=numbers))
