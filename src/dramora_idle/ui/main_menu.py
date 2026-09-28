"""Main menu window matching the former HTML/CSS main menu."""

from __future__ import annotations

import tkinter as tk
from typing import Callable

from dramora_idle.logging_system import logging
from dramora_idle.version import __version__

BG = "#000000"
TITLE_FG = "#00D0FF"
BUTTON_FG = "#ffffff"
BUTTON_HOVER = "#333333"
BUTTON_ACTIVE = "#555555"


class MainMenu(tk.Frame):
    """Centered main menu: Start Game, Load Game, Settings, Quit."""

    def __init__(self, master: tk.Misc, on_quit: Callable[[], None]) -> None:
        super().__init__(master, bg=BG)
        self._on_quit = on_quit
        self._build()

    def _build(self) -> None:
        title = tk.Label(
            self,
            text="Main Menu",
            font=("Segoe UI", 24, "bold"),
            fg=TITLE_FG,
            bg=BG,
        )
        title.pack(pady=(0, 32))

        for label, handler in (
            ("Start Game", self._start_game),
            ("Load Game", self._load_game),
            ("Settings", self._settings),
            ("Quit", self._quit),
        ):
            self._make_button(label, handler)

        version = tk.Label(
            self,
            text=__version__,
            font=("Segoe UI", 9),
            fg="#666666",
            bg=BG,
        )
        version.pack(side=tk.BOTTOM, pady=16)

    def _make_button(self, text: str, command: Callable[[], None]) -> tk.Button:
        button = tk.Button(
            self,
            text=text,
            font=("Segoe UI", 12, "bold"),
            fg=BUTTON_FG,
            bg=BG,
            activeforeground=BUTTON_FG,
            activebackground=BUTTON_ACTIVE,
            relief=tk.FLAT,
            bd=0,
            padx=32,
            pady=12,
            cursor="hand2",
            command=command,
        )
        button.pack(pady=8)

        def on_enter(_: tk.Event) -> None:
            button.configure(bg=BUTTON_HOVER)

        def on_leave(_: tk.Event) -> None:
            button.configure(bg=BG)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        return button

    def _start_game(self) -> None:
        logging.info("Start Game button clicked")

    def _load_game(self) -> None:
        logging.info("Load Game button clicked")

    def _settings(self) -> None:
        logging.info("Settings button clicked")

    def _quit(self) -> None:
        logging.info("Quit button clicked")
        self._on_quit()
