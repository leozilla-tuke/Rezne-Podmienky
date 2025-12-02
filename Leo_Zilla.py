import PySimpleGUI as sg

layout = [
    [sg.Text("Rovnica (1 = posuv, 2 = trieska fz):"), sg.Input(key="eq", size=(5,1))],
    [sg.Text("Otáčky (n):"), sg.Input(key="n", size=(8,1))],
    [sg.Text("Počet zubov (z):"), sg.Input(key="z", size=(8,1))],
    [sg.Text("fz (pre rovnicu 1):"), sg.Input(key="fz", size=(8,1))],
    [sg.Text("Posuv mm/min (pre rovnicu 2):"), sg.Input(key="vf", size=(8,1))],
    [sg.Button("Vypočítať")],
    [sg.Text("", key="result")]
]

window = sg.Window("Rezné podmienky", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    try:
        eq = values["eq"]
        n = float(values["n"])
        z = float(values["z"])

        if eq == "1":
            fz = float(values["fz"])
            result = n * z * fz
            window["result"].update(f"Posuv: {result:.2f} mm/min")

        elif eq == "2":
            vf = float(values["vf"])
            result = vf / (n * z)
            window["result"].update(f"Trieska fz: {result:.4f} mm/zub")

        else:
            window["result"].update("Vyber 1 alebo 2.")

    except:
        window["result"].update("Chyba: Zadaj platné čísla!")

window.close()
