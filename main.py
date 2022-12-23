from pathlib import Path  # core python module
import pandas as pd
import PySimpleGUI as sg

def convert_to_csv(excel_file_path, output_folder):
    df = pd.read_excel(excel_file_path)
    filename = Path(excel_file_path).stem
    outputfile = Path(output_folder) / f"{filename}.csv"
    df.to_csv(outputfile, index=False)
    sg.popup_no_titlebar("Done! :)")
layout = [
    [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("Output File:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert To CSV")],
]
window = sg.Window("Excel 2 CSV Converter", layout)
while True:
    event, values = window.read()
    #print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert To CSV":
        convert_to_csv(
            excel_file_path=values["-IN-"],
            output_folder=values["-OUT-"],
        )
window.close()