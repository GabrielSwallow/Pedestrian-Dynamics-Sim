def track_time(agent, track):
    time = track.distance / agent.speed
    return time


def propagate(agents, tracks, dt=0.01):
    end_node_counter = 0
    for track in tracks:
        if track.end_node.end:
            end_node_counter += 1

    if end_node_counter < 1:
        raise Exception("oops, no node has been defined as the end node")
    elif end_node_counter > 1:
        raise Exception("oops, too many nodes have been defined as the end node")

    t = 0

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
        t += dt

    return t
