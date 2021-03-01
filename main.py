from Agent import Agent
from Node import Node
from Propagate import propagate
from Track import Track

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

track1 = Track(distance=10, max_capacity=5, Node1=Node1, Node2=Node2, weight=1)
track2 = Track(distance=10, max_capacity=1, Node1=Node2, Node2=Node3, weight=2)

agents = [agent1, agent2, agent8, agent7, agent5, agent6, agent4, agent3]
tracks = [track1, track2]

print(propagate(agents, tracks, dt=0.1))
