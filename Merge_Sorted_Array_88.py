
#  Here is the solution of the 88. Merge Sorted Array LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #  While the addition of given 'lens' of elements is not equal to the addition of amounts of elements from both list
        while not (m + n) == len(nums1) + len(nums2):
            if (m + n) != len(nums1) + len(nums2):
                #  Remove the lat element:
                nums1.pop(-1)

        #  Now we merge these two lists
        nums1.extend(nums2)
        #  And sort them
        nums1.sort()
        print(nums1)


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
list1 = [1]
list2 = []

num1 = 1
num2 = 0

variable = Solution()
variable.merge(nums1=list1,m=num1,nums2=list2,n=num2)

