from Agent import Agent
from Node import Node
from Propagate import propagate
from Track import Track
import plotparams

Node1 = Node(max_capacity=5, is_end=False, pos=[0,5])
Node2 = Node(max_capacity=5, is_end=True, pos=[5,5])
agent1 = Agent(speed=5, initial_node=Node1)
track = Track(distance=10, max_capacity=5, Node1=Node1, Node2=Node2, weight=1)

agents = [agent1]
tracks = [track]

propagate(agents, tracks)