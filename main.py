import PySimpleGUI as sg


def logical_gates(and1, and2, or1, or2, Not, buffer, nand1, nand2, nor1, nor2, xor1, xor2, xnor1, xnor2):
    """
    A method for process of input gates and generate appropriate output of gates
    :param and1:
    :param and2:
    :param or1:
    :param or2:
    :param Not:
    :param buffer:
    :param nand1:
    :param nand2:
    :param nor1:
    :param nor2:
    :param xor1:
    :param xor2:
    :param xnor1:
    :param xnor2:
    :return:
    """
    # And
    if bool(and1) and bool(and2):
        window["-OFF1-"].update("gates/on.png")
    else:
        window["-OFF1-"].update("gates/off.png")

    # Or
    if bool(or1) or bool(or2):
        window["-OFF2-"].update("gates/on.png")
    else:
        window["-OFF2-"].update("gates/off.png")

    # not
    if not bool(Not):
        window["-OFF3-"].update("gates/on.png")
    else:
        window["-OFF3-"].update("gates/off.png")

    # Buffer
    if bool(buffer):
        window["-OFF4-"].update("gates/on.png")
    else:
        window["-OFF4-"].update("gates/off.png")

    # Nand
    if not (bool(nand1) and bool(nand2)):
        window["-OFF5-"].update("gates/on.png")
    else:
        window["-OFF5-"].update("gates/off.png")

    # Nor
    if not (bool(nor1) or bool(nor2)):
        window["-OFF6-"].update("gates/on.png")
    else:
        window["-OFF6-"].update("gates/off.png")

    # Xor
    if bool(xor1) ^ bool(xor2):
        window["-OFF7-"].update("gates/on.png")
    else:
        window["-OFF7-"].update("gates/off.png")

    # Xnor
    if not (bool(xnor1) ^ bool(xnor2)):
        window["-OFF8-"].update("gates/on.png")
    else:
        window["-OFF8-"].update("gates/off.png")


sg.theme("LightBlue7")

first_layout = [
    [sg.Text("Welcome to\nGates Tutorial Application\n(GTA)", font="Calibre 30", text_color="red", expand_x=True,
             justification="center")],
    [sg.Text("Click tabs to start", font="Caliber 25", text_color="blue", expand_x=True, justification="center")],
    [sg.Image("gates/start.png", expand_x=True)],
    [sg.Text("By AliLaser", font="Calibre 15", text_color="black", expand_x=True, justification="center")]
]

# And gate
and_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-ANDBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-ANDBTN2-", size=(4, 30), pad=(0, 5))]
])

and_layout = [
    [
        sg.Column([
            [
                and_btn,
                sg.Image("gates/and.png", expand_x=True, expand_y=True, key="-ANDGATE-", pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF1-", expand_x=True, expand_y=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/and_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="Center", pad=(100, 0))
    ]
]

# Or gate
or_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-ORBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-ORBTN2-", size=(4, 30), pad=(0, 5))]
])

or_layout = [
    [sg.Column([
        [
            or_btn,
            sg.Image("gates/or.png", key="-OR-", expand_x=True, expand_y=True, pad=(0, 50)),
            sg.Image("gates/off.png", key="-OFF2-", expand_x=True, expand_y=True, pad=(0, 50))
        ]
    ], justification="center")],
    [sg.Column([
        [
            sg.Image("gates/or_table.png", expand_x=True, expand_y=True)
        ]
    ], justification="center", pad=(100, 0))]
]

# Not gate
not_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-NOTBTN-", size=(4, 30), pad=(0, 50))]
])

not_layout = [
    [
        sg.Column([
            [
                not_btn,
                sg.Image("gates/not.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF3-", expand_y=True, expand_x=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/not_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# Buffer gate
buffer_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-BUFFER-", size=(4, 30), pad=(0, 50))]
])

buffer_layout = [
    [
        sg.Column([
            [
                buffer_btn,
                sg.Image("gates/buffer.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF4-", expand_x=True, expand_y=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/buffer_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# Nand gate
nand_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-NANDBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-NANDBTN2-", size=(4, 30), pad=(0, 5))]
])

nand_layout = [
    [
        sg.Column([
            [
                nand_btn,
                sg.Image("gates/nand.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF5-", expand_x=True, expand_y=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/nand_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# Nor gate
nor_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-NORBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-NORBTN2-", size=(4, 30), pad=(0, 5))]
])

nor_layout = [
    [
        sg.Column([
            [
                nor_btn,
                sg.Image("gates/nor.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF6-", expand_y=True, expand_x=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/nor_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# Xor gate
xor_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-XORBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-XORBTN2-", size=(4, 30), pad=(0, 5))]
])
xor_layout = [
    [
        sg.Column([
            [
                xor_btn,
                sg.Image("gates/xor.png", expand_y=True, expand_x=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF7-", expand_x=True, expand_y=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/xor_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# Xnor gate

xnor_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-XNORBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-XNORBTN2-", size=(4, 30), pad=(0, 5))]
])

xnor_layout = [
    [
        sg.Column([
            [
                xnor_btn,
                sg.Image("gates/xnor.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF8-", expand_x=True, expand_y=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/xnor_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

# About
about_layout = [
    [sg.Text("֍ Ver", text_color="red", font="Calibre 15")],
    [sg.Text("1. Optimize the code", text_color="blue", font="Calibre 15")],
    [sg.Text("2. Covers the eight main logic gates", text_color="blue", font="Calibre 15")],
    [sg.Text("3. Improve the quality of images", text_color="blue", font="Calibre 15")],
    [sg.Text("4. Append start and about tabs", text_color="blue", font="Calibre 15")],
    [sg.Text("--------------------------------------------------------------------------------------------", text_color="black", font="Calibre 15")],
    [sg.Image("gates/instagram.png"), sg.Text("@alilaser1999", text_color="black", font="Calibre 15")],
    [sg.Image("gates/telegram.png"), sg.Text("@Ali_Laser1999", text_color="black", font="Calibre 15")],
    [sg.Image("gates/site.png"), sg.Text("Ali_Khoshkholgh.ir", text_color="black", font="Calibre 15")]
]


# Configuration
tab_group = [[
    sg.TabGroup([
        [
            sg.Tab("start", first_layout),
            sg.Tab("and", and_layout),
            sg.Tab("or", or_layout),
            sg.Tab("not", not_layout),
            sg.Tab("buffer", buffer_layout),
            sg.Tab("nand", nand_layout),
            sg.Tab("nor", nor_layout),
            sg.Tab("xor", xor_layout),
            sg.Tab("xnor", xnor_layout),
            sg.Tab("about", about_layout)
        ]
    ], font="Calibre 15", tab_location="top", tab_background_color="black", title_color="white",
        selected_background_color="yellow", selected_title_color="red")
]]

window = sg.Window("GTA", tab_group)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    logical_gates(values["-ANDBTN1-"],
                  values["-ANDBTN2-"],
                  values["-ORBTN1-"],
                  values["-ORBTN2-"],
                  values["-NOTBTN-"],
                  values["-BUFFER-"],
                  values["-NANDBTN1-"],
                  values["-NANDBTN2-"],
                  values["-NORBTN1-"],
                  values["-NORBTN2-"],
                  values["-XORBTN1-"],
                  values["-XORBTN2-"],
                  values["-XNORBTN1-"],
                  values["-XNORBTN2-"])

window.close()
