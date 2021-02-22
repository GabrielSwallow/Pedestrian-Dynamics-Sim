from Agent import Agent
from node import Node 
from Track import Track
from Propagate import track_time, propagate

agent1 = Agent(speed = 10)
Node1 = Node(max_capacity = 5)
Node2 = Node(max_capacity = 5)
track = Track(distance = 10, max_capacity = 5, Node1 = Node1, Node2 = Node2)

agents = [agent1]
tracks = [track]

propagate(agents, tracks)