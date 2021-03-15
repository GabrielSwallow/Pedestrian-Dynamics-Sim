"""Defines and runs simulation."""
from Propagate import propagate
from gui import *
import random

outside = Node(name="outside", max_capacity=100, pos=[30, 10])
reception_entrance = Node(name="outside", max_capacity=100, pos=[29, 10])
dalby_court_doorway = Node(name="outside", max_capacity=100, pos=[24, 12])
dalby_court_doorway_outside = Node(name="outside", max_capacity=100,
                                   pos=[23, 12])
upper_ramp = Node(name="outside", max_capacity=100, pos=[15, 10])
lower_ramp = Node(name="outside", max_capacity=100, pos=[5, 6])
queens_tower = Node(name="outside", max_capacity=100, is_end=True, pos=[0, 0])

main_entrance_doors = Track(max_capacity=3, node1=outside,
                            node2=reception_entrance, weight=6,
                            name="Main Entrance Doorway")
entrance = Track(max_capacity=50, node1=reception_entrance,
                 node2=dalby_court_doorway, weight=7,
                 name="Entrance to Dalby Court")
dalby_court_doors = Track(max_capacity=3, node1=dalby_court_doorway,
                          node2=dalby_court_doorway_outside, weight=8,
                          name="Dalby Court Doors")
dalby_court = Track(max_capacity=70, node1=dalby_court_doorway_outside,
                    node2=upper_ramp, weight=9, name="Dalby Court")
ramp = Track(max_capacity=30, node1=upper_ramp, node2=lower_ramp, weight=10,
             name="Ramp")
ramp_to_tower = Track(max_capacity=70, node1=lower_ramp, node2=queens_tower,
                      weight=11, name="Ramp To Tower")

tracks = [main_entrance_doors, entrance, dalby_court_doors, dalby_court, ramp,
          ramp_to_tower]
agentspeeds = []
for i in range(1, 101):
    agentspeeds.append(random.random()*2+3)
agents = []
for speed in agentspeeds:
    agents.append(Agent(speed, initial_node=outside))

print(propagate(agents, tracks, dt=0.1, animate=True))
