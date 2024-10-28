import Functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText()
add_button = sg.Button("Add")

window = sg.Window("My todo App", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()