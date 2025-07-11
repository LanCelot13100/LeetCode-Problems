
#  Here is the solution of the 268. Missing Number LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  Here is the solution:
        new_list = []

        nums.sort()
        full_nums = list(range(0,nums[-1] + 1))

        if full_nums == nums:
            full_nums.append(full_nums[-1] + 1)

        for i in full_nums:
            if not i in nums:
                new_list.append(i)

        result = new_list[0]
        return result


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [0,1]

variable = Solution()
print(variable.missingNumber(nums=numbers))
