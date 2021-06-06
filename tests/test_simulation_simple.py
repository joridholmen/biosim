import unittest
from  biosim.Simulation import biosim
from biosim.Cell import lowland

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
'''

if __name__ == '__main__':
    unittest.main()

def test_init_pop():
    'Check if add_pop works'
    b = biosim(init_pop=None)
    b.add_pop()
    assert len(b.init_pop) == 50

def test_year_cycle():
    'Check if add_pop works in test_year_cycle'
    b = biosim(init_pop=None)
    assert len(b.year_cycle()) == 50
    #assert len(l.nyliste) == 50
   #assert len(b.eat) == 50


def test_fodder_eaten():
    'Check if make_herbivores eat works in year_cycle'
    l = lowland()
    b = biosim(init_pop=None)
    b.year_cycle()
    l.herbivores_pop = b.dyn
    #l.make_herbivores_eat()
    assert l.af == 800 - 50 * 10

#def test_year:












