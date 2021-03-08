import PySimpleGUI as sg


def initialGUI():
    sg.theme("LightBlue")
    layout = [[sg.Text("Number of Nodes"),
               sg.Slider(range=(1, 10), default_value=5,
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


def nodeGUI(number_of_nodes):
    sg.theme("LightBlue")
    number_of_nodes = int(number_of_nodes)
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


def trackGUI(number_of_nodes, number_of_tracks):
    sg.theme("LightBlue")
    number_of_tracks = int(number_of_tracks)
    number_of_nodes = int(number_of_nodes)
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
                 initial_value=1),
             sg.Text('to node:'),
             sg.Spin(
                 [i for i in range(0, number_of_nodes)],
                 initial_value=1),
             sg.Text('')], [sg.Text("Track Name:"), sg.InputText('')]]
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


def agentGUI(number_of_nodes, number_of_agents):
    sg.theme("LightBlue")
    number_of_agents = int(number_of_agents)
    number_of_nodes = int(number_of_nodes)
    layout = []
    for i in range(number_of_agents):
        agent_options_list = [
            [sg.Text("speed"), sg.Slider(range=(1, 10), default_value=5,
                                         orientation="horizontal",
                                         font=('Helvetica', 12))],
            [sg.Text("Initial Node"),
             sg.Slider(range=(1, number_of_nodes), default_value=5,
                       orientation="horizontal",
                       font=('Helvetica', 12))]]
        layout.append([sg.Frame("Track " + str(i) + " Attributes:",
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
    values = initialGUI()
    number_of_nodes = values[0]
    number_of_tracks = values[1]
    number_of_agents = values[2]

    nodes = nodeGUI(number_of_nodes)
    tracks = trackGUI(number_of_nodes, number_of_tracks)
    agents = agentGUI(number_of_nodes, number_of_agents)

    return nodes, tracks, agents
