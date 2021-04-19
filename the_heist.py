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
