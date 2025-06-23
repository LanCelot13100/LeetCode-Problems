
#  Here is the solution of the  69. Sqrt(x) LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  Here is the solution:
        new_list = []
        bad_list = []
        #  Here is the loop that fills the 'bad_list' with numbers that are being repeated in the array
        for row in nums:
            if row in new_list:
                bad_list.append(row)
                continue
            new_list.append(row)
        #  And here all repeated numbers that were placed in the 'bad_list' are being removed from the 'nums' parameter
        for row2 in bad_list:
            nums.remove(row2)
        #  After all, we have the changed 'nums' list as a parameter and the returned len of numbers in this list
        return len(nums)



#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [0,0,0,0,3]

variable = Solution()
print(variable.removeDuplicates(numbers))
print(type(variable))
