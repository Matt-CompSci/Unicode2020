class Solution:
    def calculate_capacity(self, heights):
        total_area = 0
        trough_left = -1
        trough_right = -1

        for idx, height in enumerate(heights):
            if idx != 0:
                if height < heights[idx - 1]:
                    if trough_left == -1:
                        trough_left = idx - 1
                elif height > heights[idx - 1]:
                    if idx == len(heights) - 1 or heights[idx + 1] <= height:
                        trough_right = idx
                        if trough_left != -1:
                            trough_height = min(heights[trough_left], heights[trough_right])
                            for column in range(trough_left + 1, trough_right):
                                total_area += trough_height - heights[column]
                            trough_left = -1

        return total_area

class UnitTests:
    def assertEqual(self, x, y):
        print("Output", x)
        print("Output Expected:", y)
        print("Success?", x == y)

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([1, 4, 2, 1, 1, 2, 5, 3, 4]), 11)
    
    def test2(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([1, 4, 2, 1, 1, 2, 5, 5, 3]), 10)
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([5, 4, 2, 1, 1, 2, 5, 3, 4]), 16)
    
    def test4(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([1, 6, 2, 1, 1, 2, 5, 5, 3]), 14)
    
    def test5(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([15, 2, 5, 2]), 3)
    
    def test6(self):
        solution = Solution()
        self.assertEqual(solution.calculate_capacity([1, 5]), 0)



asd = UnitTests()
asd.test1()
asd.test2()
asd.test3()
asd.test4()
asd.test5()
asd.test6()

# You have been hired as part of a specialist team for a heist.
# 
# They have found a vault built by the Inca civilisation and hidden deep beneath Machu Pichu in Peru.
# 
# The vault can only be opened by collecting 24 signet rings hidden around South America, which must be turned at the close of "Pachapucuy," the Month of Rain.
# 
# Each signet has a tiny and unique two dimensional crest: complete peaks from those crests form the teeth of the keys. All 24 must be found before the vault can be opened.
# 
# ...But your employer doesn't have time for that.
# 
# Which is where you come in.
# 
# The 2D signet crests can be represented by a set of instructions:
# 
# [1, 4, 2, 1, 1, 2, 5, 3, 4]
# 
# These instructions can be interpreted as a 2D object where the index of the array is the x position and the value represents the y 'height':
# 
# 
#       #  
#  #    # #
#  #    ###
#  ##  ####
# #########
# 
# From this 2D object you can calculate the volume required to shape quick setting resin to reproduce the teeth of the keys:
# 
# 
#       #  
#  #~~~~#~#
#  #~~~~###
#  ##~~####
# #########
# 
# The volume is the number of resin units the 2D object can hold. In this example it is 11 units.
# 
#     Note: the volume will only include complete troughs in the 2D object.
#     For example, the half formed trough on the left in the example above does not count.
#     Note also that the volume of the trough can only be calculated from the lowest lip.
#     For Example, the small trough on the right has one side two units high and another that is only one. With a width of one unit, it has a total possible volume of one unit.
# 
# You must write a program that takes a list of integers in the range of 1 to 255 and calculate the volume of resin needed to properly form the teeth of the keys. You may assume the list always contains at least one element.
# 
# This must be done with at least two days to spare before the end of the Month of Rain, so that your employer's other specialists have time to travel there and use the program.
# 
# Success will grant you the respect of the heisting community, not to mention your share of whatever lies in the vault.
# 
# If you do not provide the program before then however your employer will be... displeased.
