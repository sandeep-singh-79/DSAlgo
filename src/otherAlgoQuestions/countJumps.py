import unittest

def minJumpsRequired(x: int, y: int, d: int) -> int:
    if x < y and d > 0 and x > 0:
        jumpCount, currentDist = 1, (x+d)
		
        while currentDist < y:
            jumpCount += 1
            currentDist += d
		
        return jumpCount
    
    return 0

class tests(unittest.TestCase):
    def testJumpCountWhenEndIsNotMultipleOfStart(self):
        self.assertEqual(minJumpsRequired(10, 85, 30), 3)
    
    def testJumpCountWhenEndIsMultipleOfStart(self):
        self.assertEqual(minJumpsRequired(10, 100, 30), 3)
    
    def testJumpCountWhenEndIsSameAsStart(self):
        self.assertEqual(minJumpsRequired(10, 10, 30), 0)
    
    def testJumpCountWhenEndIsBeforeStart(self):
        self.assertEqual(minJumpsRequired(10, 5, 30), 0)
    
    def testJumpCountWhenStartIsNegative(self):
        self.assertEqual(minJumpsRequired(-10, 10, 30), 0)


if __name__ == "__main__":
    unittest.main()
