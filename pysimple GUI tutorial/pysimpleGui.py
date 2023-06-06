import PySimpleGUI as sg

sg.theme('lightyellow')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Hello')],
            [sg.Text('What is  your name ')], 
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print('Your Name', values[0])

window.close()