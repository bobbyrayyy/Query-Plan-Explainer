# from __future__ import annotations
import PySimpleGUI as sg
import os.path
import io

import annotations

sg.theme('DarkTeal12')

# This function is for the user to enter the db password
def databasepw():
    dbpassword = input("Please enter your password to access PostGreSQL: ")
    annotations.setpassword(dbpassword)

# Function displays GUI, this is called by project.py
def display():
    layout = [
        [
            # [sg.Image('logo.png', size=(50,50))],
            [sg.Text('Please enter your SQL query\n', font=('Helvetica', 20))],
            [sg.Text('SELECT Statement', font=('Helvetica', 14), size =(25, 1)), sg.InputText(key='-SELECT-', font=('Helvetica', 14))],
            [sg.Text('FROM Statement', font=('Helvetica', 14), size =(25, 1)), sg.InputText(key='-FROM-', font=('Helvetica', 14))],
            [sg.Text('WHERE Statement', font=('Helvetica', 14), size =(25, 1)), sg.InputText(key='-WHERE-', font=('Helvetica', 14))],
            [sg.Text('')],
            [sg.Button("Send", font=('Helvetica', 14), button_color=('Black', 'LightBlue')), sg.Button("Close", font=('Helvetica', 14), button_color=('Black', 'LightBlue'))],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text(font=('Helvetica', 14), key='-DISPLAY_MSG-')],
            [sg.Text(size=(50, 2), font=('Helvetica', 18), justification='left', key='-DISPLAY_SELECT-')],
            [sg.Text(size=(50, 2), font=('Helvetica', 18), justification='left', key='-DISPLAY_FROM-')],
            [sg.Text(size=(50, 2), font=('Helvetica', 18), justification='left', key='-DISPLAY_WHERE-')],
            [sg.Text(size=(100, 20), font=('Helvetica', 14), justification='left', key='-RESULTS-')],
            [sg.Text('')],
            [sg.Text(size=(100, 100), font=('Helvetica', 14), justification='left', key='-OUTPUT-')]
        ]
    ]

    window = sg.Window("Query Plan Explainer", layout, size=(800, 800))

    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Send":
            select_text = values['-SELECT-']
            from_text = values['-FROM-']
            where_text = values['-WHERE-']

            # THIS IS FOR DEVELOPMENT PURPOSES
            select_text = 'SELECT AVG(ps_supplycost)' 
            from_text = 'FROM partsupp P, supplier S'
            where_text = 'WHERE P.ps_suppkey = S.s_suppkey'
            # THIS IS FOR DEVELOPMENT PURPOSES

            window['-DISPLAY_MSG-'].update('The query to explain is: ')
            window['-DISPLAY_SELECT-'].update(select_text)
            window['-DISPLAY_FROM-'].update(from_text)
            window['-DISPLAY_WHERE-'].update(where_text)
            print(select_text, from_text, where_text)
            
            # This is the part to call annotation.py with the parameters of the user input SQL text
            # And get back the return values from annotations.py
            # raw_data, output = annotations.explain(select_text, from_text, where_text)
            raw_data, output = annotations.testexplain(select_text, from_text, where_text)

            # Use returned values to label the frontend
            window['-RESULTS-'].update(raw_data)
            window['-OUTPUT-'].update(str(output))
        elif event == "Close":
            break
        
    
    
    window.close()
