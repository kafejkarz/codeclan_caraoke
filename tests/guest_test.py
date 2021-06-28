import unittest

from classes.room import *
from classes.guest import *
from classes.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        
        self.sara = Guest("Sara", 100)
        self.Arek = Guest('Arek Rucki', 100)

    
