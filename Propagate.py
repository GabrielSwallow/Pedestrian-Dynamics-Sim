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
                ideal_track = agent.node.ideal_track()
                possible_to_move = ideal_track.add_if_can(agent)
                if possible_to_move:
                    agent.currenttrack = ideal_track
                else:
                    continue
            elif agent.element == "Track":
                if agent.timer >= track_time(agent, agent.currenttrack):
                    #move agent to node
                    agent.element = "Node"
                    agent.timer=0
                    agent.currenttrack = None
                else:
                    agent.timer += 1
                continue
                
                
        
        t += dt
    
    return t