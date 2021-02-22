class Agent():

    def __init__(self, speed, initial_node):
        self.speed = speed
        self.node = initial_node
        self.exit = False
        self.element = "Node"
        self.timer=0
        self.currenttrack = None
        
    def exit(self):
        self.exit = True