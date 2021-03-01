import matplotlib.pyplot as plt 
from matplotlib.animation import PillowWriter
from celluloid import Camera
import os

directory = os.path.dirname(os.path.realpath(__file__))

def track_time(agent, track):
    time = track.distance / agent.speed
    return time

fig, axs = plt.figure()
camera = Camera(fig)

def frame(tracks):
    for track in tracks():
        plt.plot()
    plt.plot()


def propagate(agents, tracks, dt=0.01):
    t = 0

    leftover = agents

    while len(leftover) > 0:
        # propagate each agent through one time step
        for agent in leftover:
            if agent.exit:
                leftover.remove(agent)
            elif agent.element == "Node":
                # choose a track and try and join it
                ideal_track = agent.current_node.ideal_track()
                ideal_track.add_if_can(agent)
                continue
            elif agent.element == "Track":
                if agent.timer >= track_time(agent, agent.current_track):
                    # move agent to node
                    agent.element = "Node"
                    agent.timer = 0
                    agent.current_node = agent.current_track.end_node
                    if agent.current_node.is_end:
                        agent.exit = True
                    agent.current_track = None
                    continue
                else:
                    agent.timer += dt
                    continue
            raise Exception("oops! agent status wasn't found", agent.element)
        print(t)

        if t%10=0:
            #plot function
        t += dt

    return t

anim = camera.animate()
pillow = PillowWriter(fps=45)
filename = directory + "\\Animation.gif" 
anim.save(filename, writer=pillow)