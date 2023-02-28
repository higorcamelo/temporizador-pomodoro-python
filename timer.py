import time
import threading
import PySimpleGUI as sg
import winsound

class Pomodoro:
    def __init__(self):
        layout = [
            [sg.Push(),sg.Text('Relógio Pomodoro'), sg.Push()],
            [sg.Push(), sg.Text('00:00'), sg.Push()],
            [sg.Button('Iniciar'), sg.Button('Pular'), sg.Button('Reiniciar')]
        ]
        self.criarJanela =  sg.Window('Relógio Pomodoro', layout)

    def iniciar(self):
        while True:
            self.event, self.values = self.criarJanela.read()
            if self.event == sg.WIN_CLOSED:
                break

tela = Pomodoro()
tela.iniciar()



