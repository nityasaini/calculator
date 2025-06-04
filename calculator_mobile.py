from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.utils import get_color_from_hex

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10
        
        # Display
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=50,
            background_color=get_color_from_hex('#FFFFFF'),
            foreground_color=get_color_from_hex('#000000'),
            size_hint=(1, 0.2)
        )
        self.add_widget(self.display)
        
        # Button grid
        button_grid = GridLayout(cols=4, spacing=5)
        
        # Button data: text, background color
        buttons = [
            ('7', '#E0E0E0'), ('8', '#E0E0E0'), ('9', '#E0E0E0'), ('÷', '#FFB74D'),
            ('4', '#E0E0E0'), ('5', '#E0E0E0'), ('6', '#E0E0E0'), ('×', '#FFB74D'),
            ('1', '#E0E0E0'), ('2', '#E0E0E0'), ('3', '#E0E0E0'), ('-', '#FFB74D'),
            ('0', '#E0E0E0'), ('.', '#E0E0E0'), ('=', '#4CAF50'), ('+', '#FFB74D'),
            ('C', '#EF5350'), ('±', '#9575CD'), ('%', '#9575CD'), ('⌫', '#9575CD')
        ]
        
        for text, color in buttons:
            btn = Button(
                text=text,
                background_color=get_color_from_hex(color),
                background_normal='',
                font_size=30,
                color=get_color_from_hex('#000000') if color == '#E0E0E0' else get_color_from_hex('#FFFFFF')
            )
            btn.bind(on_press=self.on_button_press)
            button_grid.add_widget(btn)
        
        self.add_widget(button_grid)
        
        self.current = ''
        self.last_was_operator = False
        self.last_button = None

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
            self.current = ''
        
        elif button_text == '⌫':
            self.display.text = self.display.text[:-1]
            self.current = self.display.text
        
        elif button_text == '±':
            if current and current[0] == '-':
                self.display.text = current[1:]
            else:
                self.display.text = '-' + current
        
        elif button_text == '%':
            if current:
                self.display.text = str(float(current) / 100)
        
        elif button_text == '=':
            try:
                result = eval(self.current.replace('×', '*').replace('÷', '/'))
                self.display.text = str(result)
                self.current = str(result)
            except:
                self.display.text = 'Error'
                self.current = ''
        
        else:
            if current == '0' or current == 'Error':
                self.display.text = ''
                
            if button_text in '+-×÷':
                if self.last_was_operator:
                    self.display.text = self.display.text[:-1] + button_text
                else:
                    self.display.text += button_text
                self.last_was_operator = True
            else:
                self.display.text += button_text
                self.last_was_operator = False
            
            self.current = self.display.text

class CalculatorApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#F5F5F5')
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run() 