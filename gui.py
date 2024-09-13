# gui.py - Handles the graphical user interface with Tkinter

import tkinter as tk
from services import FileCopyService

class ApplicationGUI:
    def __init__(self, root, config):
        self.root = root
        self.service = FileCopyService(config)
        self.setup_ui()

    def setup_ui(self):
        """Set up the basic UI components."""
        tk.Label(self.root, text="File Copy Tool").pack(pady=10)
        self.start_btn = tk.Button(self.root, text="Start Copy", command=self.start_copy)
        self.start_btn.pack(pady=5)

        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.pack(pady=10)

    def start_copy(self):
        """Start the copy service and log the process."""
        self.service.copy_files()
        self.log_message("Copy task started...")

    def log_message(self, message):
        """Log messages to the text box."""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
