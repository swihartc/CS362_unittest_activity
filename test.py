import unittest
from calculator import add
from calculator import sub
from calculator import mult
from calculator import div

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert add(3,1) == 4
        assert add(13.2,2.5) == 15.7
        assert add (3,-20) == -17

    def test_sub(self):
        assert sub(3,-1) == 4
        assert sub(-1,-1) == 0
        assert sub(3.5,2.5) == 1

    def test_mult(self):
        assert mult(3,12) == 36
        assert mult(0,300) == 0
        assert mult(2.5,3) == 7.5
        
    def test_div(self):
        assert div(10,0) == None
        assert div(4,2) == 2
        assert div(3,4) == 0.75

        pass

if __name__ == '__main__':
    unittest.main()