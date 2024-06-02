# Overview
2D minigame inspired by Dark Souls, Sekiro and Hollow Knight in Metroidvania style.

# Table of Contents
- [Description](#description)
- [Installation](#how-to-install-and-run)
- [Usage](#how-to-use)
- [Updates](#updates-and-features)
- [Bugs](#bugs-and-issues)

# Description
## File Structure
```
├── main.py             - executable script             
│
├── build/              - components necessary for building parts of a game
│   ├── level.py        - level class
│   ├── levels/         - txt files with tilempas
│   └── tiles/          - different types of tiles
│
├── core/               - core game components
│   ├── constants.py    - constants
│   ├── game.py         - main game module
│   └── settings.py     - keyboard input and other settings
│
├── objects/            - in-game objects 
│   ├── entities/       - in-game entities
│   │   ├── entity.py   - superclass for all entities
│   │   ├── player.py   - player class
│   │   ├── bosses/     - different types of in-game bosses
│   │   └── enemies/    - different types of in-game enemies
│   ├── items/          - different types of in-game items
│   └── weapons/        - different types of in-game weapons
│
├── ui/                 - user interface
└── utils/              - basic utilities (for math)
```

Every complex object (enemy, boss, ...) is designed using simple FSM with hierarchical states (every state has substates and different conditional branches). 

### Example
- **Simple (default) Enemy** `/objects/entities/enemies/enemy.py`:
    ![enemy-fsm](https://northeurope1-mediap.svc.ms/transform/thumbnail?provider=spo&farmid=190566&inputFormat=jpg&cs=MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDQ4MTcxMGE0fFNQTw&docid=https%3A%2F%2Fmy.microsoftpersonalcontent.com%2F_api%2Fv2.0%2Fdrives%2Fb!1B81ZReNdkaB3FfFGFCybX_88nOjrTdKtVprYFhHxTr53iKIDrU7Qa9ZgXIn2sxE%2Fitems%2F0156LPDBTP2HTOLUM46BDZGYQ4XOCUSTO4%3Ftempauth%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDAwMDMwMDAwMGFlOWEyNjdAbGl2ZS5jb20iLCJlbmRwb2ludHVybCI6Im42YU9YdkNsMUp0bWk4azZnRDhIRzhnZDAycldzQVpaem56eGlBRGlveUE9IiwiZW5kcG9pbnR1cmxMZW5ndGgiOiIxNjQiLCJleHAiOiIxNzE3MTU2ODAwIiwiaXBhZGRyIjoiMTc4LjE0My40NC4yMzkiLCJpc2xvb3BiYWNrIjoiVHJ1ZSIsImlzcyI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMCIsIm5iZiI6IjE3MTcxMzUyMDAiLCJwdWlkIjoiMDAwMzAwMDAwQUU5QTI2NyIsInNjcCI6ImFsbHNpdGVzLmZ1bGxjb250cm9sIiwic2lkIjoiMzg3NDI3MjQxNjI4MzYxMzcyMCIsInNpdGVpZCI6Ik5qVXpOVEZtWkRRdE9HUXhOeTAwTmpjMkxUZ3haR010TlRkak5URTROVEJpTWpaayIsInRpZCI6IjkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsInR0IjoiMiIsInVwbiI6Im1pY2hhbHJlcGNpazlAZ21haWwuY29tIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiJ9.DR60SOsT4hUMi6NSpIna5zrE4joXUrrUm_evp--3sUs%26version%3DPublished&cb=63852736446&encodeFailures=1&width=1920&height=876)

# How to Install and Run
Download or clone this repository
```
git clone https://github.com/rm-a0/2d-souls
```
Install pygame
```
sudo apt install pygame
```
Run using
```
./main.py
```

# How to use
> [!NOTE]
> Rebinding is not implemented yet
> You can rebind keys manually in main.py

### List of Keybinds
| Keys                      | Actions                                       |
|---------------------------|-----------------------------------------------|
| `A`                       | Move left (backward)                          |
| `D`                       | Move right (forward)                          |
| `[Space]`                 | Jump                                          |
| `[L-Shift]`               | Dash                                          |
| `[L-MButton]`             | Attack                                        |
| `[R-MButton]`             | Deflect                                       |
| `E`                       | Use Slot 1 (Heal)                             |
| `Q`                       | Use Slot 2 (Refill mana)                      |

# Updates and Features
- [x] Created classes and methods for game objects
- [x] Created user interface
- [x] Added simple AI for enemies
- [x] Refactored, cleaned up and modularized code
- [x] Finished file organization and structure
- [x] Tilemap
- [ ] Updated physics

# Bugs and Issues
- [x] Jumping feels clunky and non responsive in some scenarios
- [x] When enemy is defeated coordinates still exist and bar updating crashes
- [ ] Enemy spawns relative to tile size (refine algorithm)
- [ ] Redundant tile array in level object
- [x] UI upddating doesnt work
- [ ] Enemy weapon isnt displayed
- [ ] Enemy doesnt deal damage when player is inside him
