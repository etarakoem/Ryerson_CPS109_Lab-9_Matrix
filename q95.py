#!/usr/bin/python3
import unittest
from matrices import *
from q94 import repeatedrow
# --------------------------------------------------------------q4.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------
def transpose(matrix) :
    '''
    Returns a matrix which is the transpose of the argument matrix.
    Assumes that the matrix is retangular
    '''
    try:
        n = len(matrix)
        m = len(matrix[0])
        trans = [[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                trans[i][j] = matrix[j][i]
        return trans
    except:
        return matrix

# --------------------------------------------------------------
# is there a repeated column?
# --------------------------------------------------------------
def repeatedrow(matrix) :
    '''
    Returns True if an only if at least one row is the same as another row
    False otherwise
    '''
    for i in range(len(matrix)-1):
     for j in range(i+1,len(matrix)):
      if matrix[i] == matrix[j]:
       return True
    return False

def repeatedcolumn(matrix) :
    '''
    Returns True if an only if at least one column is the same as another column
    False otherwise
    Use the transpose() method as a helper method, along with the 
    repeatedrow() method from q4.py
    '''
    temp = transpose(matrix)
    return repeatedrow(temp) # fill in the function
# ----------------------------------------------------------
# Show the matrices that we imported 
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
for matrix in [matrix1, matrix2, matrix3, matrix4, matrix5] :
    printmx(matrix)
    print('transpose:')
    printmx(transpose(matrix))

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(repeatedcolumn(matrix1), False)
 def test2(self):
  self.assertEqual(repeatedcolumn(matrix2), True)
 def test3(self):
  self.assertEqual(repeatedcolumn(matrix3), False)
 def test4(self):
  self.assertEqual(repeatedcolumn(matrix4), False)
 def test5(self):
  self.assertEqual(repeatedcolumn(matrix5), False)
if __name__ == '__main__':
 unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
