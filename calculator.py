import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.minsize(350, 500)  # Minimum window size
        self.root.configure(bg="#f0f0f0")
        
        # Center window on screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"400x600+{x}+{y}")
        
        # Set icon if available
        icon_paths = ["icon.ico", "icon.png", "icon.svg"]
        for icon_path in icon_paths:
            if os.path.exists(icon_path):
                try:
                    self.root.iconbitmap(icon_path) if icon_path.endswith('.ico') else self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
                    break
                except:
                    continue
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12))
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.current_expression = ""
        self.last_was_equals = False
        
        # Bind keyboard events and window close
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
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
            bg="#f0f0f0",
            wraplength=360  # Wrap long numbers
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
            
        # Button layout with colors
        button_data = [
            ('C', 0, 0, '#ff6b6b'), ('±', 0, 1, '#4dabf7'), ('%', 0, 2, '#4dabf7'), ('÷', 0, 3, '#4dabf7'),
            ('7', 1, 0, '#ffffff'), ('8', 1, 1, '#ffffff'), ('9', 1, 2, '#ffffff'), ('×', 1, 3, '#4dabf7'),
            ('4', 2, 0, '#ffffff'), ('5', 2, 1, '#ffffff'), ('6', 2, 2, '#ffffff'), ('-', 2, 3, '#4dabf7'),
            ('1', 3, 0, '#ffffff'), ('2', 3, 1, '#ffffff'), ('3', 3, 2, '#ffffff'), ('+', 3, 3, '#4dabf7'),
            ('0', 4, 0, '#ffffff', 2), ('.', 4, 2, '#ffffff'), ('=', 4, 3, '#51cf66')
        ]
        
        for button in button_data:
            text = button[0]
            row = button[1]
            col = button[2]
            color = button[3]
            colspan = button[4] if len(button) > 4 else 1
            
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=('Helvetica', 18),
                bg=color,
                fg="#000000" if color == '#ffffff' else "#ffffff",
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
            self.last_was_equals = False
        elif value == '=':
            try:
                # Replace operators with Python operators
                expr = self.current_expression.replace('×', '*').replace('÷', '/')
                # Check for division by zero
                if '/0' in expr.replace(' ', '') and not '/0.' in expr.replace(' ', ''):
                    raise ZeroDivisionError("Cannot divide by zero")
                result = eval(expr)
                # Format result to avoid long decimal numbers
                if isinstance(result, float):
                    if abs(result) > 1e10:  # Scientific notation for very large numbers
                        result = '{:.2e}'.format(result)
                    else:
                        result = '{:.8f}'.format(result).rstrip('0').rstrip('.')
                self.result_var.set(result)
                self.current_expression = str(result)
                self.last_was_equals = True
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.current_expression = "0"
                self.result_var.set("0")
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.current_expression = "0"
                self.result_var.set("0")
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
            # Start new expression if last operation was equals
            if self.last_was_equals and value.isdigit():
                self.current_expression = value
            else:
                # Handle initial zero
                if self.current_expression == "0" and value not in ['.', '+', '-', '×', '÷']:
                    self.current_expression = value
                else:
                    self.current_expression += value
            self.result_var.set(self.current_expression)
            self.last_was_equals = False

    def on_closing(self):
        """Handle window closing event"""
        self.root.quit()
        sys.exit(0)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = Calculator(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}\n\nPlease contact support.") 