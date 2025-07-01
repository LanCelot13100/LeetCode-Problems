

#  Here is the solution of the 2089. Find Target Indices After Sorting Array LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  Here is the solution:
        new_list = []
        nums.sort()

        #  Here we have to add all indices of the target in the 'nums' list
        for row1 in nums:
            if row1 == target:
                new_list.append(nums.index(row1))

        final_list = []
        adding = 0
        #  And if there are more than one, they will be increased one by one
        for row2 in new_list:
            row2 += adding
            final_list.append(row2)
            adding += 1

        #  And here we have to return the list of needed indices
        return final_list


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [1,2,5,2,3]
number = 5

variable = Solution()
print(variable.targetIndices(nums=numbers,target=number))
