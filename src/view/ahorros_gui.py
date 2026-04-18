from kivy.app import App

from kivy.unix.label import Label
from kivy.unix.button import Button
from kivy.unix.boxlayout import BoxLayout
from kivy.unix.textinput import TextInput
from kivy.unix.gridlayout import GridLayout 

class AhorrosGUI(App):
    def build(self):
        self.layout = GridLayout(cols=2, padding=10, spacing=10)

        self.label = Label(text='Ingrese el monto a ahorrar:')
        self.layout.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        self.layout.add_widget(self.text_input)

        self.button = Button(text='Calcular Ahorros')
        self.button.bind(on_press=self.calcular_ahorros)
        self.layout.add_widget(self.button)

        return self.layout

    def calcular_ahorros(self, instance):
        monto = float(self.text_input.text)
        ahorros = monto * 0.1 
        self.label.text = f'Ahorros calculados: {ahorros}'
