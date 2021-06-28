import unittest

from classes.room import *
from classes.guest import *
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.lets_rock = Song("lets rock", "Crazy guitars")
        self.november_rain = Song("november rain", "Guns N' Roses" )
        self.crazy_disco_song = Song("Crazy disco song", "Take the floor")
        self.dancing_queen = Song("Dancing queen", "Abba")