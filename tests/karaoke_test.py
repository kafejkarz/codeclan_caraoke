import unittest
from classes.karaoke import *

class TestKaraoke(unittest.TestCase):
   
    def setUp(self):
        self.karaoke = MJKaraoke(20)
        self.guest = Guest('Arek Rucki', 100)
   
    def test_should_be_able_to_create_room(self):
        self.karaoke.create_room('room1')
        self.assertEqual(1, len(self.karaoke.rooms))
        

    def test_should_be_able_to_create_song(self):
        self.karaoke.create_song('song')
        
    
    def test_karaoke_should_have_entry_fee(self):
        self.assertEqual(20, self.karaoke.entry_fee)
    

    def test_guest_can_pay_fee(self):
         self.karaoke.pay_entry_fee(self.guest)
         self.assertEqual(80, self.guest.wallet)
    
    
   

    

    

    
    
  


        
