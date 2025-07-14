
#  Here is the solution of the 66. Plus One LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #  Firstly, we create a new list that will contain str(digits):
        new_list = []

        for row in digits:
            row = str(row)
            new_list.append(row)

        #  Secondly, we turn the new list into a string and later, turn this string into an integer:
        number = "".join(new_list)
        number = int(number)

        #  Sum this number and 1:
        new_number = number + 1

        #  Turn the new number into a string back:
        new_number = str(new_number)

        #  Create the final list that will contain the needed integers
        final_list = []
        for i in new_number:
            #  Don't forget to turn the str(i) into int(i) to have digits in the final list
            i = int(i)
            final_list.append(i)

        #  Return the final list and enjoy our lives ;)
        return final_list


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
numbers = [1,2,3]

variable = Solution()
print(variable.plusOne(digits=numbers))
