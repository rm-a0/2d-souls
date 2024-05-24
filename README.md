# Overview

2D minigame inspired by Dark Souls, Sekiro and Hollow Knight in Metroidvania style. \

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
> [!NOTE]
> You may run into relative import beyond toplevel package. \
> To fix this either change your PYTHONPATH (not recommended). \
> Linux
> ```
> export PYTHONPATH=’path/to/directory’
> ```
> Windows
> ```
> SET PYTHONPATH=’path/to/directory’
> ```
> Or you can add this into the files.
> ```python
> import sys
> sys.path.insert(0, '/path/to/module/directory')
> ```

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

# Bugs and Issues

- [ ] Jumping feels clunky and non responsive in some scenarios
# Goals

- [ ] Positioning and movement relative to screen size
- [ ] Create basic interface (bars, item slots, icons)
- [ ] Create classes and methods for game objects
- [ ] Create simple AI for enemies
- [ ] Create refined AI for bosses
- [ ] Create rebinding menu

### TODO Checklist

- [ ] Dummy surface
- [ ] Tilemap
- [ ] Physics
- [ ] Player object and methods
