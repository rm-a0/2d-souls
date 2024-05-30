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
- **Player Stats**: Three bars tracking the players hp, mana, and stamina.
- **Equipment Slots**: Two slots displaying players equipped items.
- **Enemy Health**: A health bar at the bottom showing the enemy's hp.

### Controls
- **Player (left object)**: Controlled via keyboard and mouse inputs.
- **Enemy (right object)**: Driven by a simple AI using a finite state machine (FSM) with multiple conditions.

## Game design
Every element (hp bar, item slot, player, ...) has its own class with different methods. Classes were designed to be reuseable and readable at the same time. \
The `/ui` directory consists of classes used for creating and maintaining user interface. 
- `/ui/bars.py` - bars tracking and displaying different stats
- `/ui/icons.py` - icons displaying items or status effects
- `/ui/slots.py` - slots displaying and tracking players equipped items

The `/objs` directory consists of classes representing game objects. 
- `/objs/player.py` - object controlled by keyboard and mouse
- `/objs/enemy.py` - object controlled by FSM
- `/objs/weapon.py` - object used for dealing damage
- `/objs/boss.py` - refined object controlled by FSM \
\
Every complex object (player, enemy, ...) is designed using simple FSM with hierarchical states (every state has substates and different conditional branches). 

### Player
  ![player-fsm](fsm/player-fsm.jpg)

### Enemies
- **Simple Enemy** `/objs/enemy.py`:
    ![enemy-fsm](fsm/enemy-fsm.jpg)

- **Boss Enemy** `/objs/boss.py`:
    ![boss-fsm](fsm/boss-fsm.jpg)

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
- [ ] Refactored, cleaned up and modularized code
- [ ] Refined boss AI 
- [ ] Dummy surface
- [ ] Tilemap

# Bugs and Issues
- [x] Jumping feels clunky and non responsive in some scenarios
- [x] When enemy is defeated coordinates still exist and bar updating crashes
- [ ] Code is ugly and messy
