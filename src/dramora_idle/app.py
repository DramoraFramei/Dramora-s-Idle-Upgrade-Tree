"""Application entry: main window and main menu."""

from __future__ import annotations

import tkinter as tk

from dramora_idle.logging_system import logging
from dramora_idle.ui.main_menu import BG, MainMenu
from dramora_idle.version import __version__


class App(tk.Tk):
    """Root window for Dramora's Idle Upgrade Tree."""

    def __init__(self) -> None:
        super().__init__()
        self.title(f"Dramora's Idle Upgrade Tree — {__version__}")
        self.configure(bg=BG)
        self.geometry("800x600")
        self.minsize(480, 360)

        logging.init()
        logging.info(f"Application started (version {__version__})")

        menu = MainMenu(self, on_quit=self.destroy)
        menu.pack(expand=True, fill=tk.BOTH)

        self.bind("<Button-3>", lambda event: "break")


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
