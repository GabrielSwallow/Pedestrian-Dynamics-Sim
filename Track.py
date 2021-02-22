class Track():

    def __init__(self, distance, max_capacity):
        self.travellers = 0
        self.distance = distance
        self.max_capacity = max_capacity
        self.full = False

    def update_full(self):
        if self.travellers == self.max_capacity:
            self.full = False
        elif 0 <= self.travellers < self.max_capacity:
            self.full = True
        else:
            raise Exception("negative number of travellers - spooky")
    
    def add_if_if_can(self, agent):
        self.update_full
        
        if self.full == True:
            self.travellers += 1
        else:
            return False
    
    def remove(self, agent):
        self.update_full
        self.travellers-=1
        if self.travellers < 0:
            raise Exception("negative number of travellers - spooky")
        self.update_full