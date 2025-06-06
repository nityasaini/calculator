import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12))
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.current_expression = ""
        
        # Bind keyboard events to the main window
        self.root.bind('<KeyPress>', self.on_key_press)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(fill=tk.BOTH, padx=20, pady=20)
        
        self.result_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=('Helvetica', 40),
            anchor="e",
            bg="#f0f0f0"
        )
        self.result_label.pack(fill=tk.BOTH)
        
        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Configure grid
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            
        # Button layout
        button_data = [
            ('C', 0, 0), ('±', 0, 1), ('%', 0, 2), ('÷', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 2), ('.', 4, 2), ('=', 4, 3)
        ]
        
        for button in button_data:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = 2 if len(button) > 3 else 1
            
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=('Helvetica', 18),
                bg="#ffffff" if text.isdigit() or text == '.' else "#e0e0e0",
                fg="#000000",
                relief=tk.FLAT,
                padx=20,
                pady=20,
                command=lambda x=text: self.button_click(x)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def on_key_press(self, event):
        key = event.char
        keysym = event.keysym
        
        # Handle numeric keys and decimal point
        if key.isdigit() or key == '.':
            self.button_click(key)
            
        # Handle operators
        elif key in ['+', '-']:
            self.button_click(key)
        elif key == '*':
            self.button_click('×')
        elif key == '/':
            self.button_click('÷')
            
        # Handle special keys
        elif keysym == 'Return':
            self.button_click('=')
        elif keysym == 'Escape':
            self.button_click('C')
        elif keysym == 'BackSpace':
            if self.current_expression:
                self.current_expression = self.current_expression[:-1]
                if not self.current_expression:
                    self.current_expression = "0"
                self.result_var.set(self.current_expression)
    
    def button_click(self, value):
        if value == 'C':
            self.current_expression = "0"
            self.result_var.set("0")
        elif value == '=':
            try:
                # Replace operators with Python operators
                expr = self.current_expression.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                # Format result to avoid long decimal numbers
                if isinstance(result, float):
                    result = '{:.8f}'.format(result).rstrip('0').rstrip('.')
                self.result_var.set(result)
                self.current_expression = str(result)
            except:
                self.result_var.set("Error")
                self.current_expression = "0"
        elif value == '±':
            try:
                current = float(self.current_expression)
                self.current_expression = str(-current)
                self.result_var.set(self.current_expression)
            except:
                pass
        elif value == '%':
            try:
                current = float(self.current_expression)
                self.current_expression = str(current / 100)
                self.result_var.set(self.current_expression)
            except:
                pass
        else:
            # Handle initial zero
            if self.current_expression == "0" and value not in ['.', '+', '-', '×', '÷']:
                self.current_expression = value
            else:
                self.current_expression += value
            self.result_var.set(self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 