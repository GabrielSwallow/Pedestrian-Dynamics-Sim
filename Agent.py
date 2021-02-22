class Agent():

    def __init__(self, speed, initial_node):
        self.speed = speed
        self.current_node = initial_node
        self.current_track = None
        self.exit = False
        self.element = "Node"
        self.timer=0

    def exit(self):
        self.exit = True