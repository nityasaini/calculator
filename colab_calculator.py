from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

# Define the UI style
Builder.load_string('''
<CalculatorLayout>:
    orientation: 'vertical'
    padding: '10dp'
    spacing: '10dp'
    canvas.before:
        Color:
            rgba: 245/255, 247/255, 250/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    TextInput:
        id: display
        font_size: '32sp'
        multiline: False
        readonly: True
        halign: 'right'
        background_color: 1, 1, 1, 1
        foreground_color: 0.17, 0.24, 0.31, 1
        size_hint_y: 0.2
        text: '0'
        
    GridLayout:
        cols: 4
        spacing: '10dp'
        size_hint_y: 0.8
        
        Button:
            text: 'C'
            on_press: root.clear()
            background_color: get_color_from_hex('#e0e0e0')
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '±'
            on_press: root.toggle_sign()
            background_color: get_color_from_hex('#e0e0e0')
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '%'
            on_press: root.percentage()
            background_color: get_color_from_hex('#e0e0e0')
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '÷'
            on_press: root.add_operator('/')
            background_color: get_color_from_hex('#4facfe')
            color: 1, 1, 1, 1
            
        Button:
            text: '7'
            on_press: root.add_number(7)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '8'
            on_press: root.add_number(8)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '9'
            on_press: root.add_number(9)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '×'
            on_press: root.add_operator('*')
            background_color: get_color_from_hex('#4facfe')
            color: 1, 1, 1, 1
            
        Button:
            text: '4'
            on_press: root.add_number(4)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '5'
            on_press: root.add_number(5)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '6'
            on_press: root.add_number(6)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '-'
            on_press: root.add_operator('-')
            background_color: get_color_from_hex('#4facfe')
            color: 1, 1, 1, 1
            
        Button:
            text: '1'
            on_press: root.add_number(1)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '2'
            on_press: root.add_number(2)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '3'
            on_press: root.add_number(3)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '+'
            on_press: root.add_operator('+')
            background_color: get_color_from_hex('#4facfe')
            color: 1, 1, 1, 1
            
        Button:
            text: '0'
            on_press: root.add_number(0)
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
            size_hint_x: 2
        Button:
            text: '.'
            on_press: root.add_decimal()
            background_color: 1, 1, 1, 1
            color: get_color_from_hex('#2c3e50')
        Button:
            text: '='
            on_press: root.calculate()
            background_color: get_color_from_hex('#51cf66')
            color: 1, 1, 1, 1
''')

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_was_operator = False
        self.last_was_equals = False
    
    def add_number(self, number):
        display = self.ids.display
        if self.last_was_equals:
            display.text = str(number)
            self.last_was_equals = False
        elif display.text == '0':
            display.text = str(number)
        else:
            display.text += str(number)
        self.last_was_operator = False
    
    def add_operator(self, operator):
        if not self.last_was_operator:
            self.ids.display.text += operator
            self.last_was_operator = True
            self.last_was_equals = False
    
    def add_decimal(self):
        if '.' not in self.ids.display.text.split()[-1]:
            self.ids.display.text += '.'
    
    def clear(self):
        self.ids.display.text = '0'
        self.last_was_operator = False
        self.last_was_equals = False
    
    def toggle_sign(self):
        if self.ids.display.text != '0':
            if self.ids.display.text[0] == '-':
                self.ids.display.text = self.ids.display.text[1:]
            else:
                self.ids.display.text = '-' + self.ids.display.text
    
    def percentage(self):
        try:
            value = float(self.ids.display.text) / 100
            self.ids.display.text = str(value)
        except:
            self.ids.display.text = 'Error'
    
    def calculate(self):
        try:
            result = str(eval(self.ids.display.text))
            self.ids.display.text = result
            self.last_was_equals = True
        except:
            self.ids.display.text = 'Error'

class CalculatorApp(App):
    def build(self):
        self.title = 'Modern Calculator'
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run() 