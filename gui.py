import PySimpleGUI as sg

from Agent import Agent
from Node import Node
from Track import Track


def initial_gui():
    sg.theme("LightBlue")
    layout = [[sg.Text("Number of Nodes"),
               sg.Slider(range=(2, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [sg.Text("Number of Tracks"),
               sg.Slider(range=(1, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [sg.Text("Number of Agents"),
               sg.Slider(range=(1, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    window = sg.Window('Best Pedestrian Dynamics Model Simulator Ever', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        window.close()
        return values


def node_gui(number_of_nodes):
    sg.theme("LightBlue")
    layout = []
    for i in range(number_of_nodes):
        node_options_list = [
            [sg.Text("Max Capacity"), sg.Slider(range=(1, 10), default_value=5,
                                                orientation="horizontal",
                                                font=('Helvetica', 12))],
            [sg.Text("Is this the final node")],
            [sg.Radio('No', "Node" + str(i), default=True),
             sg.Radio('Yes', "Node" + str(i))],
            [sg.Text("Node Name:"), sg.InputText('')],
            [sg.Text("Node Position"),
             sg.Spin([i for i in range(1, 11)],
                     initial_value=1),
             sg.Text('X position'),
             sg.Spin([i for i in range(1, 11)],
                     initial_value=1),
             sg.Text('Y Position')]]
        layout.append([sg.Frame("Node " + str(i) + " Attributes:",
                                node_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([sg.Button('Ok'), sg.Button('Cancel')])

    window = sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        window.close()
        return values


def track_gui(number_of_nodes, number_of_tracks):
    sg.theme("LightBlue")
    layout = []
    for i in range(number_of_tracks):
        track_options_list = [
            [sg.Text("Distance"), sg.Slider(range=(1, 10), default_value=5,
                                            orientation="horizontal",
                                            font=('Helvetica', 12))],
            [sg.Text("Max Capacity"), sg.Slider(range=(1, 10), default_value=5,
                                                orientation="horizontal",
                                                font=('Helvetica', 12))],
            [sg.Text("Connects node:"),
             sg.Spin(
                 [i for i in range(0, number_of_nodes)],
                 initial_value=0),
             sg.Text('to node:'),
             sg.Spin(
                 [i for i in range(0, number_of_nodes)],
                 initial_value=0),
             sg.Text('')],
            [sg.Text("Weight"), sg.Slider(range=(1, 10), default_value=5,
                                          orientation="horizontal",
                                          font=('Helvetica', 12))],
            [sg.Text("Track Name:"), sg.InputText('')]]
        layout.append([sg.Frame("Track " + str(i) + " Attributes:",
                                track_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([sg.Button('Ok'), sg.Button('Cancel')])

    window = sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        window.close()
        return values


def agent_gui(number_of_nodes, number_of_agents):
    sg.theme("LightBlue")
    layout = []
    for i in range(number_of_agents):
        agent_options_list = [
            [sg.Text("speed"), sg.Slider(range=(1, 10), default_value=5,
                                         orientation="horizontal",
                                         font=('Helvetica', 12))],
            [sg.Text("Initial Node"),
             sg.Slider(range=(0, number_of_nodes - 1), default_value=0,
                       orientation="horizontal",
                       font=('Helvetica', 12))]]
        layout.append([sg.Frame("Agent " + str(i) + " Attributes:",
                                agent_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([sg.Button('Ok'), sg.Button('Cancel')])

    window = sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        window.close()
        return values


def guis():
    values = initial_gui()
    number_of_nodes = int(values[0])
    number_of_tracks = int(values[1])
    number_of_agents = int(values[2])

    nodes = node_gui(number_of_nodes)
    tracks = track_gui(number_of_nodes, number_of_tracks)
    agents = agent_gui(number_of_nodes, number_of_agents)

    node_dict = dict()
    for i in range(number_of_nodes):
        node = Node(max_capacity=int(nodes[6 * i]), is_end=nodes[6 * i + 2],
                    name=nodes[6 * i + 3],
                    pos=[nodes[6 * i + 4], nodes[6 * i + 5]])
        node_dict["Node" + str(i)] = node

    tracks_list = []
    number_of_track_attributes = 6
    for i in range(number_of_tracks):
        track = Track(distance=int(tracks[number_of_track_attributes * i]),
                      max_capacity=int(
                          tracks[number_of_track_attributes * i + 1]),
                      node1=node_dict["Node" + str(int(
                          tracks[number_of_track_attributes * i + 2]))],
                      node2=node_dict["Node" + str(int(
                          tracks[number_of_track_attributes * i + 3]))],
                      weight=int(tracks[number_of_track_attributes * i + 4]),
                      name=tracks[number_of_track_attributes * i + 5])
        tracks_list.append(track)

    agent_list = []
    for i in range(number_of_agents):
        agent = Agent(speed=int(agents[2 * i]),
                      initial_node=node_dict[
                          "Node" + str(int(agents[2 * i + 1]))])
        agent_list.append(agent)
    return tracks_list, agent_list
