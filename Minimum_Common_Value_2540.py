
#  Here is the solution of the 2540. Minimum Common Value LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        bad_set = set()
        new_set = set()

        #  Here we have to delete all duplicates from the 'nums1' and 'nums2' lists
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        #  Now we have to turn both of these lists into one by extending the first list
        nums1.extend(nums2)

        for i in nums1:
            #  If 'i' is in the bad_set (obviously not), it's getting appended to this one, otherwise it's getting appended to the 'new_set'
            if i in bad_set:
                new_set.add(i)
            else:
                bad_set.add(i)

        #  Turn the 'new_set' set into a list
        new_list = list(new_set)

        if len(new_list) == 0:
            return -1
        else:
            #  Define the minimal number and return it
            right_int = min(new_list)
            return right_int


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers1 = [1,1,2]
numbers2 = [2,4]

variable = Solution()
print(variable.getCommon(nums1=numbers1,nums2=numbers2))
