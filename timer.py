import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class Pomodoro:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Temporizador Pomodoro')
        self.root.tk.call('wm','iconphoto', self.root._w, PhotoImage(file = 'icon_pomodoro.png'))

        self.s = ttk.Style()
        self.s.configure('TNotebook.Tab', font=('Ubuntu', 16))
        self.s.configure('TButton', font=('Ubuntu', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill = 'both', pady = 10, expand = True)
        
        self.tab1 = ttk.Frame(self.tabs, width = 600, height = 100)
        self.tab2 = ttk.Frame(self.tabs, width = 600, height = 100)
        self.tab3 = ttk.Frame(self.tabs, width = 600, height = 100)

        self.tempor_pomodoro_funcao = ttk.Label(self.tab1, text = '25:00', font = ('Ubuntu', 48))
        self.tempor_pomodoro_funcao.pack(pady = 20)

        self.pausa_curta_funcao = ttk.Label(self.tab2, text = '05:00', font = ('Ubuntu', 48))
        self.pausa_curta_funcao.pack(pady = 20)

        self.pausa_longa_funcao = ttk.Label(self.tab3, text = '15:00', font = ('Ubuntu', 48))
        self.pausa_longa_funcao.pack(pady = 20)

        self.tabs.add(self.tab1, text = 'Pomodoro')
        self.tabs.add(self.tab2, text = 'Pausa curta')
        self.tabs.add(self.tab3, text = 'Pausa longa')


        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady = 10)

        self.inicia_botao = ttk.Button(self.grid_layout, text = 'Começar', command = self.inicia_temporizador_thread())
        self.inicia_botao.grid(row = 0, column = 0)

        self.pula_botao = ttk.Button(self.grid_layout, text = 'Pular', command = self.pula_relogio())
        self.pula_botao.grid(row = 0, column = 1)

        self.reset_botao = ttk.Button(self.grid_layout, text = 'Reiniciar', command = self.reset_relogio())
        self.reset_botao.grid(row = 0, column = 2)

        self.contador_pomodoro = ttk.Label(self.grid_layout, text = 'Pomodoros: 0', font = ('Ubuntu', 16))
        self.contador_pomodoro.grid(row = 1, column = 0, columnspan = 3, pady = 10)

        self.pomodoros = 0
        self.pulado = False
        self.parado = False
        self.executando = False


        self.root.mainloop()

    def inicia_temporizador_thread(self):
        if not executando:
            thread = threading.Thread(target = self.inicia_temporizador)
            thread.start()
            self.executando = True

    def inicia_temporizador(self):
        self.parado = False
        self.pulado = False
        relogio_id = self.tabs.index(self.tabs.select()) + 1

        if relogio_id == 1:
            full_segundos = 60 * 25            
            while full_segundos > 0 and not self.parado:
                minutos, segundos = divmod(full_segundos, 60)
                self.tempor_pomodoro_funcao.config(text =f'{minutos:02d}:{segundos:02d}') ####
                self.root.update()
                time.sleep(1)
                full_segundos -= 1
            if not self.parado or self.pulado:
                self.pomodoros += 1
                self.contador_pomodoro.config(text=f'Pomodoros: {self.pomodoros}')
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.inicia_temporizador()
        elif relogio_id == 2:
            full_segundos = 60 * 5
            while full_segundos > 0 and not self.parado:
                minutos, segundos = divmod(full_segundos, 60)
                self.pausa_curta_funcao.config(text =f'{minutos:02d}:{segundos:02d}') #####
                self.root.update()
                time.sleep(1)
                full_segundos -= 1
            if not self.parado or self.pulado:
                self.tabs.select(0)
                self.inicia_temporizador()
        elif relogio_id == 3:
            full_segundos = 60 * 15
            while full_segundos > 0 and not self.parado:
                minutos, segundos = divmod(full_segundos, 60)
                self.pausa_longa_funcao.config(text =f'{minutos:02d}:{segundos:02d}') #####
                self.root.update()
                time.sleep(1)
                full_segundos -= 1
            if not self.parado or self.pulado:
                self.tabs.select(0)
                self.inicia_temporizador()
        else:
            print('ID do temporizador desconhecido')



    def reset_relogio(self):
        self.parado = True
        self.pulado = False
        self.pomodoros = 0

        self.tempor_pomodoro_funcao.config(text = '25:00')
        self.pausa_curta_funcao.config(text = '05:00')
        self.pausa_longa_funcao.config(text = '15:00')
        self.contador_pomodoro.config(text = 'Pomodoros: 0')
        self.executando = False

    def pula_relogio(self):
        aba_atual = self.tabs.index(self.tabs.select())
        if aba_atual == 0:
            self.tempor_pomodoro_funcao.config(text = '25:00')
        elif aba_atual == 1:
            self.pausa_curta_funcao.config(text = '05:00')
        elif aba_atual == 2:
            self.pausa_longa_funcao.config(text = '15:00')


Pomodoro()
