import unittest    
def classify_triangle(a,b,c):
    
    if a <= 0 or b <= 0 or c <= 0:
       return 'NotaTriangle' 
    elif a == b and b == c:
       return 'Equilateral'
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
      return 'Right'
    elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
      return 'Isoceles'
    else :
      return 'Scalene'   
def runClassifyTriangle(a, b, c):
   
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classify_triangle(a, b, c),sep="")
class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        self.assertEqual(classify_triangle(3, 4 ,5),'Right','3,4,5 is a Right triangle')    
        self.assertEqual(classify_triangle(5, 5, 4), 'Isoceles', '5, 5, 4 is a Isoceles triangle')
        self.assertEqual(classify_triangle(3, 7, 4), 'Scalene', '3, 7, 4 is a Scalene triangle')

    def testMyTestSet2(self): 
        self.assertEqual(classify_triangle(0,0,0),'NotaTriangle','should be a not a triangle')
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
        self.assertEqual(classify_triangle(3, 7,5),'Scalene','Should be Isoceles')
        self.assertNotEqual(classify_triangle(1,2,3),'Isoceles','Should be Equilateral')    

    
if __name__ == '__main__':
    runClassifyTriangle(11, 22, 33)
    runClassifyTriangle(11, 11, 11)
    runClassifyTriangle(2, 2, 4)
    runClassifyTriangle(500, 400, 300)
    runClassifyTriangle(3, 3, 5)
    runClassifyTriangle(-3,0, 0)

    unittest.main(exit=False)   