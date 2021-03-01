"""Defines and runs simulation."""
from Agent import Agent
from Node import Node
from Propagate import propagate
from Track import Track

Node_x = Node(max_capacity=5, is_end=False, name="Node_x", pos=[0, 0])
Node1 = Node(max_capacity=5, is_end=False, name="Node1", pos=[0, 5])
Node2 = Node(max_capacity=5, is_end=False, name="Node2", pos=[5, 5])
Node3 = Node(max_capacity=5, is_end=True, name="Node3", pos=[10, 5])

agent1 = Agent(speed=1, initial_node=Node1)
agent2 = Agent(speed=1, initial_node=Node1)
agent3 = Agent(speed=1, initial_node=Node1)
agent4 = Agent(speed=1, initial_node=Node1)
agent5 = Agent(speed=1, initial_node=Node3)
agent6 = Agent(speed=1, initial_node=Node1)
agent7 = Agent(speed=1, initial_node=Node1)
agent8 = Agent(speed=1, initial_node=Node1)

track1 = Track(10, 5, node1=Node1, node2=Node2, weight=1, name="track1")
track2 = Track(10, 1, node1=Node2, node2=Node3, weight=2, name="track2")
track3 = Track(10, 3, node1=Node_x, node2=Node2, weight=1, name="track3")

agents = [agent1, agent2, agent8, agent7, agent5, agent6, agent4, agent3]
tracks = [track1, track2, track3]

print(propagate(agents, tracks, dt=0.1))
