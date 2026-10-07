import tkinter as tk
from tkinter import messagebox
import webbrowser


class Dialer:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Dialer")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#111111")

        self.number = tk.StringVar()

        # Display
        display = tk.Entry(
            root,
            textvariable=self.number,
            font=("Arial", 26),
            justify="center",
            bg="#2b2b2b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        display.pack(padx=20, pady=25, ipady=12, fill="x")

        # Keypad
        keypad = tk.Frame(root, bg="#111111")
        keypad.pack()

        buttons = [
            ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("*", 3, 0), ("0", 3, 1), ("#", 3, 2),
        ]

        for text, row, col in buttons:
            button = tk.Button(
                keypad,
                text=text,
                font=("Arial", 20),
                width=5,
                height=2,
                bg="#333333",
                fg="white",
                activebackground="#555555",
                activeforeground="white",
                relief="flat",
                command=lambda x=text: self.add_number(x)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

        # Bottom buttons
        bottom = tk.Frame(root, bg="#111111")
        bottom.pack(pady=15)

        tk.Button(
            bottom,
            text="⌫",
            font=("Arial", 18),
            width=6,
            height=2,
            bg="#ef4444",
            fg="white",
            relief="flat",
            command=self.delete_number
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            bottom,
            text="📞",
            font=("Arial", 18),
            width=6,
            height=2,
            bg="#22c55e",
            fg="white",
            relief="flat",
            command=self.call_number
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            bottom,
            text="Clear",
            font=("Arial", 12),
            width=6,
            height=2,
            bg="#555555",
            fg="white",
            relief="flat",
            command=self.clear_number
        ).grid(row=0, column=2, padx=5)

    def add_number(self, value):
        self.number.set(self.number.get() + value)

    def delete_number(self):
        self.number.set(self.number.get()[:-1])

    def clear_number(self):
        self.number.set("")

    def call_number(self):
        phone = self.number.get()

        if not phone:
            messagebox.showwarning("Dialer", "Please enter a phone number.")
            return

        # Opens the system's tel: handler, if available
        webbrowser.open("tel:" + phone)


root = tk.Tk()
app = Dialer(root)
root.mainloop()
