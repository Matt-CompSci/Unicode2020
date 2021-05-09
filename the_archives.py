class Solution:

    def get_check_digit(self, input):
        # Check valid format
        import re
        regex = re.compile("\\d-\\d{2}-\\d{6}-[a-zA-Z]")

        if (regex.match(input)):
            numberIndexes = [0, 2, 3, 5, 6, 7, 8, 9, 10]
            sum = 0

            for idx, index in enumerate(numberIndexes):
                sum += int(input[index]) * (idx + 1)
            return sum % 11
        else:
            return -1

import unittest

class SolutionTests(unittest.TestCase):

    # Given test
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("0-19-852663-x"), 6)

    # Gibberish
    def test2(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("How many cats have you eaten today?"), -1)

    # Negative number
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("-1-19-852663-x"), -1)

    # Different length in first section
    def test4(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("01-19-852663-x"), -1)

    # Different length in second section
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("0-195-852663-x"), 6)

    # Different length in third section
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("0-19-5852663-x"), -1)

    # Different variable name as check digit
    def test6(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("0-19-852663-y"), 6)

    # Another valid example
    def test7(self):
        solution = Solution()
        self.assertEqual(solution.get_check_digit("5-29-284872-x"), 7)

# You are working as a researcher in the Archives, a vast collection of knowledge stored physically and encoded digitally with signifier codes.
# 
# The signifier codes are represented in the format 0-00-000000-0.
# 
# You have been approached by a detective. She needs to prove the innocence of her client, who is sentenced to death on April 26th.
# 
# The client claims to have been framed and that there is a note hidden in a book stored within the Archives that proves it.
# 
# Finding the book should be easy - Each code is ten digits long and the last number (known as a check digit) is used to verify the identity of the document.
# 
# There is a problem however:
# 
# Someone has been covering their tracks. Someone has changed the check digit on every document in this section of the Archives.
# 
# Luckily, being an experienced researcher, you know that the check digit is determined by taking the sum of each digit multiplied by its integer weight (1-9 in ascending order) modulo 11.
# 
# For example, to calculate the check digit (x) for 0-19-852663-x you would use the equation ((0*1)+(1*2)+(9*3)+(8*4)+(5*5)+(2*6)+(6*7)+(6*8)+(3*9)) % 11.
# 
# You can simply write a method to determine the check digit when provided with a representation of the signifier code, e.g. 0-19-852663-x, where x represents the check digit.
# 
# If the input is not in a valid format return -1.
# 
# You can use this method to find any document in this section of the Archives, and so you can find the book!
# 
# Hurry though, the the life of the detective's client depends on you.
