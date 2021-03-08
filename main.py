"""Defines and runs simulation."""
from Propagate import propagate
from gui import *

tracks, agents = guis()

print(propagate(agents, tracks, dt=0.1))
