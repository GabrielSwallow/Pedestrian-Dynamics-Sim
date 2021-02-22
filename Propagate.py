def track_time(agent, track):
    time = track.distance/agent.speed
    return time

def propagate(agents, tracks, dt=0.01):
    t=0

    leftover = agents

    while len(leftover)>0:
        #propagate each agent through one time step

        for agent in leftover:
            if agent.exit:
                leftover.remove(agent)
            elif agent.element == "Node":
                #choose a track and try and join it 
                ideal_track = agent.current_node.ideal_track()
                ideal_track.add_if_can(agent)
            elif agent.element == "Track":
                if agent.timer >= track_time(agent, agent.current_track):
                    #move agent to node
                    agent.element = "Node"
                    agent.timer=0
                    agent.current_track = None
                else:
                    agent.timer += dt
            raise Exception("oops! agent status wasn't found")
        
        t += dt
    
    return t