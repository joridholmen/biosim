import unittest
from  biosim.Simulation import biosim

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
'''

if __name__ == '__main__':
    unittest.main()

def test_init_pop():
    b = biosim(init_pop=None)
    b.add_pop()
    assert len(b.init_pop) == 50

def











