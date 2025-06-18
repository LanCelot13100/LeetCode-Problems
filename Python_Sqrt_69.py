
#  Here is the solution of the  69. Sqrt(x) LeetCode problem (Python)
#  I was able to come up with my own way of solving that. Here it is:

class Solution(object):

    #  This function returns the square root of x rounded down to the nearest integer
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5) #  <- Solution


#  This block of code down below is needed to run the program in your IDE, but you don't actually need it when you check your answer on LeetCode
number = int(input("Enter some number: "))
variable = Solution()
print(variable.mySqrt(number))