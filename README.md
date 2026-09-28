# Dramora's Idle Upgrade Tree

## Game Description

Dramora's Idle Upgrade Tree is an idle game built as a native Python desktop app (tkinter). It is in active development and has many planned features.

## Core Features

1. Node based upgrade tree
2. Idle stat gain
3. Many upgrades across different tiers
4. Tier based progression
5. Achievement system
6. Secrets hidden throughout the game that give strong boosts to upgrade tree, stats, tiers, or upgrades.

## Current Version

0.0.01-Pre-Alpha

## Requirements

- Python 3 (use the project virtual environment at `.venv`)
- tkinter (included with standard Windows Python builds)

No extra packages are required for the current Pre-Alpha build.

## How to Run

From the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe .\run_game.py
```

Or as a module (with `src` on `PYTHONPATH`):

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m dramora_idle
```

The app opens the main menu (Start Game, Load Game, Settings, Quit). Logs are written to `logs/latest.log`.
