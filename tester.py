import unittest
import main

class tester(unittest.TestCase):
    def test_SimpleOr(self):
        self.assertEqual(main.calcSystemProb('(1|2)',[5,3]),5+3-15)
    def test_SimpleFunctionOr(self):
        self.assertEqual(main.calcSystemProb('(1|2)',[6,2]),main.TonyOr(6,2))
    def test_compoundOr(self):
        self.assertEqual(main.calcSystemProb('(1|2|3)', [5, 3, 4]), main.TonyOr(main.TonyOr(5,3),4))
    def test_SimpleAnd(self):
        self.assertEqual(main.calcSystemProb('(1&2)',[5,3]),15)
    def test_SimpleFunctionAnd(self):
        self.assertEqual(main.calcSystemProb('(1&2)',[15,3]),15*3)
    def test_Hard(self):
        self.assertEqual(main.calcSystemProb('(1|2)&3', [5,3,62]),(5+3-15)*62)
    def test_LabHard(self):
        self.assertEqual(main.calcSystemProb('(1|2)',[6,2]),main.TonyOr(6,2))
    def test_Lab(self):
        self.assertEqual(round(main.calcSystemProb('((2&4)|1)&((3&8)|(6&7)|(5))',[.95]*8),6), .994652)

if __name__ == '__main__':
    unittest.main()