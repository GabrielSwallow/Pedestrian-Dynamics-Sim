class Track():

    def __init__(self, distance, max_capacity, Node1, Node2, weight):
        self.travellers = 0
        self.distance = distance
        self.max_capacity = max_capacity
        self.full = False
        self.weight = weight
        self.start_node = Node1
        self.end_node = Node2

        Node1.add_edge(self)
        Node2.add_edge(self)

    def __repr__(self):
        return self, "\n", "distance:", self.distance, "\n", "Max Capacity:", self.max_capacity, "\n", "Start Node:", self.start_node, "\n", "End Node:", self.end_node, "\n", "Weight", self.weight

    def update_full(self):
        if self.travellers == self.max_capacity:
            self.full = True
        elif 0 <= self.travellers < self.max_capacity:
            self.full = False
        else:
            raise Exception("negative number of travellers - spooky")

    def add_if_can(self, agent):
        self.update_full()

        if not self.full:
            self.travellers += 1
            agent.element = "Track"
            agent.current_track = self
            self.update_full()
            return
        else:
            return

    def remove(self, agent):
        self.update_full
        self.travellers -= 1
        agent.elemt = "Node"
        self.update_full
