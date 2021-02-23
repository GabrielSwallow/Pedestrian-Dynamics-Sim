class Node():

    def __init__(self, max_capacity, is_end):
        self.max_capacity = max_capacity
        self.full = False
        self.edges_dict = dict()
        self.end = is_end

    def add_edge(self, track):
        self.edges_dict[track] = track.weight

    def ideal_track(self):
        return max(self.edges_dict, key=self.edges_dict.get)

# class Node_Pair():
#
#    def __init__(self, max_capacityN1, max_capacityT1, max_capacityN2, distance):
