
  
class Room:
    def __init__(self, room_name):
         
         self.guests = [] # self.guests is a list to store guests 
         self.capacity = 0
       
        

    def check_in(self, guest):  # check_in function can add guests to the self.guests list 
        if len(self.guests) < self.capacity: # guests can be added if required criteria are met
            self.guests.append(guest)  
            return True
        else:
            return False

    def check_out(self, guest):
        pass

    def add_song(self, song_name):
        pass
        
        


    
        
        



