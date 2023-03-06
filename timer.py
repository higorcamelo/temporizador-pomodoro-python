import datetime
import PySimpleGUI as sg
from plyer import notification


class Pomodoro:
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text('Relógio Pomodoro', font=('Helvetica', 15)), sg.Push()],
            [sg.Push(), sg.Text('0:00:00', font=('Helvetica', 20), key = '-TEMPO-'), sg.Push()],
            [sg.Button('Iniciar'), sg.Button('Pausar'), sg.Button('Reiniciar')]
        ]
        self.window =  sg.Window('Relógio Pomodoro', layout)

    def att_tempo(self,tempo):
        self.window['-TEMPO-'].update(tempo)

    def timer_pomodoro(self):
        tempo_trab = 25
        tempo_desc = 5

        while True:
            for i in range(tempo_trab * 1, 0, -1):
                self.att_tempo(str(datetime.timedelta(seconds=i)))
                event, values = self.window.read(timeout = 1000)
                if event == 'Reiniciar' or event == sg.WIN_CLOSED:
                    self.window.close()
                    return
                elif event == 'Pausar':
                    event, values = self.window.read()
                    while event != 'Iniciar':
                        event, values = self.window.read()
            self.nofitication.notify(
                title = 'Pomodoro',
                message = 'Hora de descansar!',
                app_icon = None,
                timeout = 10
            )
            for i in range(tempo_desc * 1, 0, -1):
                self.att_tempo(str(datetime.timedelta(seconds=i)))
                event, values = self.window.read(timeout = 1000)
                if event == 'Reiniciar' or event == sg.WIN_CLOSED:
                    self.window.close()
                    return
                elif event == 'Pausar':
                    event, values = self.window.read()
                    while event != 'Iniciar':
                        event, values = self.window.read()
            sg.popup('Trabalha')


    def iniciar(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event == 'Iniciar':
                self.timer_pomodoro()
            elif self.event == sg.WIN_CLOSED:
                break

tela = Pomodoro()
tela.iniciar()



