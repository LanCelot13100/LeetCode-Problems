
#  Here is the solution of the  35. Search Insert Position LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #  If target in the 'nums' list, then return its index
        if target in nums:
            return nums.index(target)
        #  If target is not in the 'nums' list but still in the range of the first and last numbers, them add the 'target' number to the 'nums' list and sort it to return its index
        elif not target in nums and target in range(nums[0],nums[-1]):
            nums.append(target)
            nums.sort()
            return nums.index(target)
        #  If the 'target' number is less than the first number in the 'nums' list, then return 0
        elif target < nums[0]:
            return 0
        #  If the 'target' number is more than the last number in the nums list, then add the 'target' number to the 'nums' list and return its index
        else:
            nums.append(target)
            return nums.index(target)



#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
my_list = [1,3,5]
number = 4

smth = Solution()
print(smth.searchInsert(nums=my_list,target=number))

