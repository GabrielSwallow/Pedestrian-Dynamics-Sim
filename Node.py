class Node():

    def __init__(self, max_capacity, is_end, pos):
        self.max_capacity = max_capacity
        self.full = False
        self.edges_dict = dict()
        self.end = is_end
        self.pos = pos
        if len(self.pos) != 2:
            raise Exception("pos must be a 2D position")

    def add_edge(self, track):
        self.edges_dict[track] = track.weight

    def ideal_track(self):
        return max(self.edges_dict, key=self.edges_dict.get)

# class Node_Pair():
#
#    def __init__(self, max_capacityN1, max_capacityT1, max_capacityN2, distance):
