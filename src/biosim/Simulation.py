# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

from biosim.animals import herbivore
from biosim.Cell import lowland

import pandas
import matplotlib.pyplot as plt
import subprocess
import random
'''
<<<<<<< HEAD
=======

>>>>>>> origin/Simulation
'''
class biosim:

    def __init__(self, init_pop, seed = 10):  # mangler img og ymax

        #self.seed = random.seed(10)
        #self.init_pop = 2
        self.seed = random.seed(seed)
        if init_pop is None:
            self.init_pop = self.add_pop()



        self.init_pop = init_pop

    def add_pop(self):
        """
        Adds animal to the cell/island. These animals become the initial population
        """
        l = lowland()
        self.init_pop = l.adding_animals()

    #def feeding(self):
        """
            Herbivores eat yearly
            """

    #def procreation(self):
        """
            Animals mate maximum once per year
            """

    # def migration(self):

    def year_cycle(self):
        """
            simulates one year

        Runs through each of the 6 yearly seasons for all cells.
        - Step 1: Animals feed
        - Step 2: Animals procreate
        - Step 3: Animals migrate
        - Step 4: Animals age
        - Step 5: Animals lose weight
        - Step 6: Animals die
            """
        l = lowland()

        if self.y == 0:
            l.adding_animals()
        l.make_herbivores_eat() # Animals feed
        l.reset_appetite()      # Animals feed
        l.newborn_animals() #Animals procreate
        l.aging()           #Animals age
        l.make_animals_lose_weight() #Animals lose weight
        l.dead_animals_natural_cause() # Animals die
        #self.init_pop = l.counting_animals()
#=======
        l.make_herbivores_eat()  # Animals feed
        l.reset_appetite()
        l.newborn_animals()  # Animals procreate
        l.make_animals_age()  # Animals age
        l.make_animals_lose_weight()  # Animals lose weight
        l.dead_animals_natural_cause()  # Animals die
        l.counting_animals()
#>>>>>>> origin/Simulation

        self.y = n_year + 1  # counts how many years have passed for the simulation #tror denne er feil da, ville bare ha den med

    def year(self):
        """
            Counts how many years to use in simulation
            """
        # n_year =

    def num_animals(self):
        """
            Counts how many animals there are in the cell/island, for use in simulation
            """
        self.N_animals = lowland.counting_animals()

    def simulate(self):
        """
            function for simulating
            """
