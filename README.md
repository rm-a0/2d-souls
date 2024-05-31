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
- `/objs/boss.py` - refined object controlled by FSM

Every complex object (enemy, boss, ...) is designed using simple FSM with hierarchical states (every state has substates and different conditional branches). 

### Enemies
- **Simple Enemy** `/objs/enemy.py`:
    ![enemy-fsm](
https://viewer.diagrams.net/index.html?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=enemy-fsm.drawio#R7VnbctowEP0aHsNYErbJI%2BGSdEIzTEhT8qixha3WtogQt359ZZCxfImTkoBJpk9Iq7UlHZ2zuxYN1A3X1xzP%2FO%2FMJUEDGu66gXoNCAG8NORPbNkoi2XbO4vHqatsqWFM%2FxBlVA96C%2BqSecZRMBYIOssaHRZFxBEZG%2BacrbJuUxZkZ51hjxQMYwcHRetP6gp%2FZ22bRmq%2FIdTzk5mBoUZCnDgrw9zHLltpJtRvoC5nTOxa4bpLghi9BJfdc4MXRvcL4yQSb3lgAh38cP9oDYYQoKFzc2cYdxdIrU1skg0TV%2B5fdRkXPvNYhIN%2Bar3ibBG5JH6rIXupz5CxmTQCafxFhNiow8QLwaTJF2GgRuWC%2BWaint92nuJO00y6vbU%2B2NuoXnHHCoQ5W3BHrR%2F%2FDgf2gPQmcPR8%2Bwx%2BjKejx4uEOZh7RFT4wZ1fjIE2gcLzmrCQyPVIB04CLOgyyxGsqObt%2FdLTkA11IOWHU7XqJQ4WaqZvvWG%2FcGLZ81j5VJDxDG%2FxWElVZrF%2FEcMl4YKsK3edjCpCK0nvCb5K9QFayuZr2kg08x6cSkncqoXEayomWlujsOylDI47G53OJyU%2BLBK%2FFEJwVsSHBeI3oBXI9V%2B5dCmbXtzs3nTG%2FcQup9GGapfIXhNnoxGrTo2kunjSZVGtEXAqjZhv1Mh5JQezoJHOw0One1s7962z4775Pz%2B8EvdfLYzMurhftWqN%2BzIZ3F%2FXXxq1oHlm3LdrjfsHcT%2Bl%2B5M%2B9uHcL6mNqsrwM%2BF%2BsTYaP%2Fy4q535CGWjvlU38dvnU%2FCAtxK%2FZdo69UHTgK%2Bwf9sbEU4laIQfoxQ6jSS2j3Y4xxvNYcZoJObam0exQas0LrOcQ%2B3cDUjOv%2F0ud2iDHCl3600put%2F4OzKbUZD3nATT5lwsokacTCwcxuJVnznJZZPGcqlXkSUlDqgXybYj6RBz5CpWNXVw0FEDIXXdLf%2FLwkRWEx8RKawsrvs9a6GiXRIp0LEiBQAFEE8aKuwDPo6MJqwvS57m6%2BigkNBCuQKsWuLIqnI%2FksRhvXSDB6UmO0M3cDS6lXyQnObC6jC65WIZAtV8M1Gl%2F5EI1yrPKY4fg%2FxFskrLNEuRrS%2BrFC9o4iUVwZ41XTL9Iqdg5uKpWfch2IVDcOlc6Gir62MDGJ8RcGDmitQS2tsnRfzyXxD%2FfIDnq9cjAi676b%2FDu2SQ%2FsmO%2Bn8B#%7B%22pageId%22%3A%22XxzA5qAW1PiLPIhqlTAl%22%7D
)

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
- [ ] Enemy doesnt deal damage when player is inside him
