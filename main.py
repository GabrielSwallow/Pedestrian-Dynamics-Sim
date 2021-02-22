from Agent import Agent
from Node import Node 
from Track import Track
from Propagate import track_time, propagate

Node1 = Node(max_capacity = 5, is_end=False)
Node2 = Node(max_capacity = 5, is_end=True)
agent1 = Agent(speed = 10, initial_node=Node1)
track = Track(distance = 10, max_capacity = 5, Node1 = Node1, Node2 = Node2, weight=1)

agents = [agent1]
tracks = [track]

propagate(agents, tracks)