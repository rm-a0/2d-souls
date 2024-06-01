import pygame
import sys

from core.constants import *                    # Constant variables
from core.settings import *                 # Settings

from utils.calc import *                    # Import utilities for calculating

from objects.items.item_factory import ItemFactory
from objects.weapons.weapon_factory import WeaponFactory
from objects.entities.player import Player              # Player class
from objects.entities.enemies.enemy import Enemy                # Enemy class
from objects.items.consumable import Flask           # Flask class
from objects.weapons.weapon import Weapon              # Weapon class

from ui.ui_factory import UiFactory         # Ui factory class
from ui.bar import Bar                     # Bar classes
from ui.icon import Icon                   # Icon class
from ui.slot import Slot                   # Slot class

from build.level import Level              # Level class

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
        pygame.display.set_caption('dev/2d-souls')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 26)
        self.sprites = pygame.sprite.Group

        self.init_player()
        self.init_player_ui()
        self.init_level(0, 0)
        self.init_sprites()
        self.append_sprites()

    def init_player(self):
        self.player = Player(100, GROUND, PLAYER_WIDTH, PLAYER_HEIGHT, GREEN, PLAYER_MAX_HP, PLAYER_SPEED, PLAYER_MAX_MANA, PLAYER_MAX_STAMINA, JUMP_SPEED)
        self.player.equip_weapon(WeaponFactory.create_default_weapon())
        self.hp_flask = ItemFactory.create_hp_flask(5)
        self.mana_flask = ItemFactory.create_mana_flask(2)

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

    def init_level(self, x, y):
        self.level = Level(x, y)
        self.level.load_level()

    def init_sprites(self):
        self.sprites = pygame.sprite.Group(self.player, self.player.weapon, self.ico, self.p_hp_bar, self.p_mana_bar, self.p_stamina_bar, self.slot_1, self.slot_2)

    def append_sprites(self):
        for enemy in self.level.enemies:
            self.sprites.add(enemy)
        for boss in self.level.bosses:
            self.sprites.add(boss)

    def render_frame(self):
        self.screen.fill(BLACK)
        self.level.tiles.draw(self.screen)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def handle_player(self):
        self.player.apply_gravity()
        self.player.refill_stamina(1)
        self.player.update()

    def handle_enemies(self):
        for enemy in self.level.enemies:
            enemy.update(calc_dist(self.player.rect.center, enemy.rect.center))
            enemy.perform_action(calc_dir(self.player.rect.x, enemy.rect.x), self.player)
        for boss in self.level.bosses:
            boss.update(calc_dist(self.player.rect.center, boss.rect.center))
            boss.perform_action(calc_dir(self.player.rect.x, boss.rect.x), self.player)

    # Main game loop
    def game_loop(self):
        running = True 
        while running:
            # Process keyboard input
            handle_input(self.player, self.level.enemies[0], self.slot_1, self.slot_2)

            self.handle_player()
            self.handle_enemies()

            # Update frame
            self.render_frame()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
