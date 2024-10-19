import PySimpleGUI as sg
window = sg.Window(title="Profile",
                   layout=[
                       [sg.Text("NPM    : 2210010553")],
                       [sg.Text("Nama   : Ayu Atut Khofifah")],
                       [sg.Text("Kelas  : 5B NonReg Banjarmasin")],
                       [sg.Text("Matkul : Pemrograman Visual 3")],
                   ],
                   size=(400,200),
                   )
window()
window.close()