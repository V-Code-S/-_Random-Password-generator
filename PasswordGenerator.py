import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator By - VIRUPAKSHI")
        self.root.geometry("400x300")

        # Variables
        self.length_var = tk.IntVar()
        self.include_upper_var = tk.BooleanVar()
        self.include_numbers_var = tk.BooleanVar()
        self.include_symbols_var = tk.BooleanVar()
        self.password_var = tk.StringVar()

        # Default values
        self.length_var.set(12)
        self.include_upper_var.set(True)
        self.include_numbers_var.set(True)
        self.include_symbols_var.set(True)

        # UI Components
        self.create_widgets()

    def generate_password(self):
        length = self.length_var.get()
        include_upper = self.include_upper_var.get()
        include_numbers = self.include_numbers_var.get()
        include_symbols = self.include_symbols_var.get()

        characters = string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        try:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def copy_to_clipboard(self):
        generated_password = self.password_var.get()
        pyperclip.copy(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

    def create_widgets(self):
        # Labels
        ttk.Label(self.root, text="Password Length:").pack(pady=10)
        ttk.Label(self.root, text="Include:").pack(pady=5)

        # Entry for password length
        length_entry = ttk.Entry(self.root, textvariable=self.length_var)
        length_entry.pack(pady=5)

        # Checkboxes for character types
        ttk.Checkbutton(self.root, text="Uppercase Letters", variable=self.include_upper_var).pack(pady=5)
        ttk.Checkbutton(self.root, text="Numbers", variable=self.include_numbers_var).pack(pady=5)
        ttk.Checkbutton(self.root, text="Symbols", variable=self.include_symbols_var).pack(pady=5)

        # Button to generate password
        ttk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Display generated password
        ttk.Entry(self.root, textvariable=self.password_var, state='readonly').pack(pady=10)

        # Buttons for clipboard integration and exit
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        ttk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
