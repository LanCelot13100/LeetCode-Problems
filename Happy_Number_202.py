
#  Here is the solution of the 202. Happy Number LeetCode problem
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        false_counter = 0
        while True:
            counter = 0
            for row1 in list(str(n)):
                row1 = int(row1)
                counter += row1 ** 2

            false_counter += 1
            n = counter
            print(n)
            if n == 1:
                return True

            elif false_counter == 31:
                return False



#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
integer = 7

variable = Solution()
print(variable.isHappy(n=integer))

