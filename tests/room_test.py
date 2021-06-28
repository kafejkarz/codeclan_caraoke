import unittest

from classes.room import *
from classes.guest import *


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("room1")
        
        self.room = Room('room1')
        self.room.capacity = 2
        self.Arek = Guest('Arek Rucki', 100)
        self.Sara = Guest('Sara', 100)

   
    
    def test_should_be_able_to_checkin_to_room(self):
        self.room.check_in("Arek Rucki")
    
    def test_should_be_able_to_checkout_from_room(self):
        self.room.check_out('Arek Rucki')

    def test_should_be_able_to_add_song_to_room(self):
        self.room.add_song('song1')

    def test_more_guests_trying_to_check_in_than_there_is_free_space(self):
        self.room.capacity = 2
        self.assertTrue(self.room.check_in('guest 1'))
        self.assertTrue(self.room.check_in('guest 2'))
        self.assertFalse(self.room.check_in('guest 3'))
        self.assertEqual(2, len(self.room.guests))

    





        





 

    