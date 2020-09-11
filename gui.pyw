import PySimpleGUI as sg

layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse()],
    [sg.Output(size =(80,20))]


]

windows = sg.Window('Advanced Research',layout)

while True:
    event, values = windows.read()

    if event in (None,'Exit','Cansel'):
        break

