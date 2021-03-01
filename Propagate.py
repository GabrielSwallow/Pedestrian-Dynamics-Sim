import os

import matplotlib.pyplot as plt
from celluloid import Camera
from matplotlib.animation import PillowWriter

directory = os.path.dirname(os.path.realpath(__file__))


def track_time(agent, track):
    time = track.distance / agent.speed
    return time


fig = plt.figure()
camera = Camera(fig)


def plot_frame(tracks):
    x, y = [], []
    for track in tracks:
        # x.append(track.start_node.pos[0])
        # x.append(track.end_node.pos[0])
        # y.append(track.start_node.pos[1])
        # y.append(track.end_node.pos[1])
        x = [track.start_node.pos[0], track.end_node.pos[0]]
        y = [track.start_node.pos[1], track.end_node.pos[1]]   
        plt.plot(x,y, "-o", linewidth = 5 + 5*track.travellers, color="b")
        plt.plot(x[0], y[0], "o", ms=5 + 10*track.travellers, color="b")
        plt.plot(x[1], y[1], "o", ms=5 + 10*track.travellers, color="b")



def propagate(agents, tracks, dt=0.01):
    #initial frame
    for i in range(30):
        plot_frame(tracks)
        camera.snap()

    end_node_counter = 0
    for track in tracks:
        if track.end_node.end:
            end_node_counter += 1

    if end_node_counter < 1:
        raise Exception("oops, no node has been defined as the end node")
    elif end_node_counter > 1:
        raise Exception("oops, too many nodes have been defined as the end node")

    t = 0
    count = 0

    leftover = agents

    while len(leftover) > 0:
        # propagate each agent through one time step
        for agent in leftover:
            if agent.exit:
                leftover.remove(agent)
                continue
            elif agent.element == 'Node':
                # choose a track and try and join it
                ideal_track = agent.current_node.ideal_track()
                ideal_track.add_if_can(agent)
                continue
            elif agent.element == 'Track':
                if agent.timer >= track_time(agent, agent.current_track):
                    # move agent to node
                    agent.element = "Node"
                    agent.current_track.travellers -= 1
                    agent.timer = 0
                    agent.current_node = agent.current_track.end_node
                    if agent.current_node.end:
                        agent.exit = True
                    agent.current_track = None
                    continue
                else:
                    agent.timer += dt
                    continue
            raise Exception("oops! agent status wasn't found", agent.element)
        if count % 5 == 0:
            plot_frame(tracks)
            camera.snap()
        print(t)
        
            
        t += dt
        count += 1
    #final frame
    for i in range(30):
        plot_frame(tracks)
        camera.snap()
        
    anim = camera.animate()
    pillow = PillowWriter(fps=45)
    filename = directory + "\\Animation.gif"
    anim.save(filename, writer=pillow)

    return t
