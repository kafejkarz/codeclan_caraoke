from classes.room import *
from classes.guest import *

class MJKaraoke:
    def __init__(self, fee):
        
    
        self.rooms = []
        self.entry_fee = fee

    def create_song(self, name):
        pass

    def create_room(self, name):
        self.rooms.append(Room(name))
    
    
    def pay_entry_fee(self, guest):
        guest.wallet -= self.entry_fee
