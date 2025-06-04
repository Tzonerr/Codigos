import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Piscando")
        self.geometry("250x330")
        self.resizable(False, False)

        self.expression = ""

        self.display = ttk.Entry(self, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = ttk.Button(self, text=text, command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def blink(self, button):
        original = button.cget('style')
        style = ttk.Style()
        blink_style = 'Blink.TButton'
        style.configure(blink_style, background='yellow')
        button.config(style=blink_style)
        self.after(150, lambda: button.config(style=original))

    def on_click(self, char):
        button = self.focus_get()
        if isinstance(button, ttk.Button):
            self.blink(button)
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Erro"
        else:
            self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
