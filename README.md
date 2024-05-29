# Overview
2D minigame inspired by Dark Souls, Sekiro and Hollow Knight in Metroidvania style.

# Table of Contents
- [Description](#description)
- [Installation](#how-to-install-and-run)
- [Usage](#how-to-use)
- [Updates](#updates-and-features)
- [Bugs](#bugs-and-issues)

# Description

Upon executing the script, a window with a resolution of 1336x768 is created, featuring a simple user interface and two game objects.

### User Interface
- **Player Stats**: Three bars tracking the player's health (HP), mana, and stamina.
- **Equipment Slots**: Two slots displaying the player's equipped items.
- **Enemy Health**: A health bar at the bottom showing the enemy's HP.

### Controls
- **Player (left object)**: Controlled via keyboard and mouse inputs.
- **Enemy (right object)**: Driven by a simple AI using a finite state machine (FSM) with multiple conditions.

## Enemies
In the `/objs` folder, there are two types of enemies:
- **Simple Enemy** `/objs/enemy.py`:
  - Features: Three states and one attack pattern. Predictable and easy to defeat.
  - ![enemy-fsm](fsm/enemy-fsm.jpg)

- **Boss Enemy** `/objs/boss.py`:
  - Features: Multiple states, various attack types, driven by random number generators, and a more complex FSM.
  - ![boss-fsm](fsm/boss-fsm.jpg)

This project serves as a foundation for developing and experimenting with game mechanics and AI behavior.

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
- [x] Basic interface (bars, item slots, icons)
- [x] Classes and methods for game objects
- [x] Weapon class and methods
- [x] More constants, erase magic numbers
- [x] Refined UI elements and classes
- [x] Slot tracking method
- [x] Attacks and deflects stop movement briefly
- [x] Added enemy AI prototype
- [x] Added simple AI for enemies
- [x] Windup for enemy attack
- [ ] Refined boss AI 
- [ ] Dummy surface
- [ ] Tilemap

# Bugs and Issues
- [x] Jumping feels clunky and non responsive in some scenarios
- [x] When enemy is defeated coordinates still exist and bar updating crashes
