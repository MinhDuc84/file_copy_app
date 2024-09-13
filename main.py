# main.py - Application entry point

import tkinter as tk
from gui import ApplicationGUI
from config import AppConfig

def main():
    """Main entry point for the application."""
    config = AppConfig.load()
    root = tk.Tk()
    root.title("Advanced Copy Tool")
    app_gui = ApplicationGUI(root, config)
    root.mainloop()

if __name__ == "__main__":
    main()
