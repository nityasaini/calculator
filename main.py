import sys
import platform

def is_mobile():
    return platform.system() == 'Linux' and hasattr(sys, 'android_private')

if __name__ == '__main__':
    if is_mobile():
        from calculator_mobile import CalculatorApp
        CalculatorApp().run()
    else:
        import tkinter as tk
        from calculator import Calculator
        root = tk.Tk()
        app = Calculator(root)
        root.mainloop() 