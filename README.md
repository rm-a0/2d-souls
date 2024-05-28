# Overview
2D minigame inspired by Dark Souls, Sekiro and Hollow Knight in Metroidvania style.

# Table of Contents
- [Description](#description)
- [Installation](#how-to-install-and-run)
- [Usage](#how-to-use)
- [Updates](#updates-and-features)
- [Bugs](#bugs-and-issues)
- [License](#license)

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
| `E`                       | Heal (Will be switched to Use Slot 1)         |
| `Q`                       | Use Slot 2                                    |

# Updates and Features
- [x] Created basic interface (bars, item slots, icons)
- [x] Created classes and methods for game objects
- [ ] Create simple AI for enemies
- [ ] Create refined AI for bosses
- [ ] Create rebinding menu

### TODO
- [x] Weapon class and methods
- [x] Add more constants, erase magic numbers
- [x] Create ui elements and classes
- [ ] Make attack and deflect duration longer
- [x] Boss AI prototype
- [ ] Slot tracking method
- [ ] Dummy surface
- [ ] Tilemap

# Bugs and Issues
- [x] Jumping feels clunky and non responsive in some scenarios
- [x] When enemy is defeated coordinates still exist and bar updating crashes

# License
