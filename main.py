#!/usr/bin/env python3
import pygame
import sys

from core.const import *                    # Constant variables
from core.settings import *                 # Settings

from utils.calc import *                    # Import utilities for calculating

from objs.obj_factory import ObjFactory     # Object factory class
from objs.player import Player              # Player class
from objs.enemy import Enemy                # Enemy class
from objs.consumable import Flask           # Flask class
from objs.weapon import Weapon              # Weapon class

from ui.ui_factory import UiFactory         # Ui factory class
from ui.bars import Bar                     # Bar classes
from ui.icons import Icon                   # Icon class
from ui.slots import Slot                   # Slot class

from levels.level import Level               # Level class

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
        pygame.display.set_caption('dev/2d-souls')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 26)

        self.init_player()
        self.init_player_ui()
        self.init_boss()
        self.init_boss_ui()
        #self.init_level(0, 0)
        self.append_sprites()

    def init_player(self):
        self.player = ObjFactory.create_player()
        self.player.equip_weapon(ObjFactory.create_weapon())
        self.hp_flask = ObjFactory.create_hp_flask(5)
        self.mana_flask = ObjFactory.create_mana_flask(2)

    def init_player_ui(self):
        self.ico = UiFactory.create_main_icon() 
        self.p_hp_bar = UiFactory.create_player_hp_bar(self.player)
        self.p_mana_bar = UiFactory.create_player_mana_bar(self.player)
        self.p_stamina_bar = UiFactory.create_player_stamina_bar(self.player)
        self.slot_1 = UiFactory.create_slot_1(self.font)
        self.slot_1.switch_item(self.hp_flask)
        self.slot_1.update_count()
        self.slot_2 = UiFactory.create_slot_2(self.font)
        self.slot_2.switch_item(self.mana_flask)
        self.slot_2.update_count()

    def init_boss(self):
        self.boss = ObjFactory.create_enemy()
        self.boss.equip_weapon(ObjFactory.create_weapon())

    def init_boss_ui(self):
        self.boss_hp_bar = UiFactory.create_boss_hp_bar(self.boss)

    def init_level(self, x, y):
        self.level = Level(x, y, "levels/data")
        self.level.load_level()

    def append_sprites(self):
        self.sprites = pygame.sprite.Group(self.player, self.boss, self.player.weapon, self.boss.weapon, self.ico, self.p_hp_bar, self.p_mana_bar, self.p_stamina_bar, self.boss_hp_bar, self.slot_1, self.slot_2)


    def game_loop(self):
        running = True 
        while running:
            # Handle keyboard input
            handle_input(self.player, self.boss, self.slot_1, self.slot_2)
            # Calculate distance
            dist = calc_dist(self.player.rect.center, self.boss.rect.center)
            direction = calc_dir(self.player.rect.x, self.boss.rect.x)
            # Handle player
            self.player.apply_gravity()
            self.player.refill_stamina(1)
            self.player.update()
            # Handle enemy
            self.boss.update(dist)
            self.boss.perform_action(direction, self.player)
            # Update ui
            if self.player.hp > 0:
                self.p_hp_bar.update(self.player.hp)
                self.p_mana_bar.update(self.player.mana)
                self.p_stamina_bar.update(self.player.stamina)
            else:
                print("You lost")
                break
            if self.boss.hp > 0: 
                self.boss_hp_bar.update(self.boss.hp)
            else:
                print("You won")
                break
            # Clear and draw new frame
            self.screen.fill(BLACK)
            self.sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# Main 
def main():
    game = Game()
    game.game_loop()

if __name__ == "__main__":
    main()
