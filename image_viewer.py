import PySimpleGUI as sg
import os.path


# LAYOUT , WILL BE 2 COLMNS USING VSEPARATOR() AND BROWSABLE AND DISPLAYABLE CONTENT
file_list_column = [
      [
        sg.Text("Image Folder"),
        # IN is input parameter
        sg.In(size = (25,1), enable_events = True , key ="-FOLDER-"),
        sg.FolderBrowse(),

      ],
      [
        sg.Listbox(
            values = [], enable_events = True , size = (40,20),
            key = "-FILE LIST-"
        )
      ],
]

image_viewer_column = [
    [sg.Text("Choose an image from list on the left:")],
    [sg.Text(size=(40,1), key = "-TOUT-")],
    [sg.Image(key= "-IMAGE-")],
]

layout = [
    [
    sg.Column(file_list_column),
    sg.VSeparator(),
    sg.Column(image_viewer_column),

    ]
]

# WINDOW DEFINITION
window = sg.Window("Image Viewer", layout)

# EVENT LOOP TO READ THE WINDOW AND INTERACT WITH IT
while True:
    event , values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
      break

    if event == "-FOLDER-" :
        folder = values["-FOLDER-"]
        try:
            # get list of files in the FOLDER
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png",".gif"))
        ]
        window["-FILE LIST-"].update(fnames)

    if event == "-FILE LIST-":
        try:
            filename = os.path.join(values["-FOLDER-"],values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename = filename)
        except:
            pass

# ENDING THE PROGRAM TO CLOSE THE WINDOW 
window.close()
