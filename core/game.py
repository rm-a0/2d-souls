import pygame
import sys

from core.constants import *                    # Constant variables
from core.settings import *                     # Settings

from utils.calc import *                        # Import utilities for calculating

from objects.items.item_factory import ItemFactory
from objects.weapons.weapon_factory import WeaponFactory
from objects.entities.player import Player
from objects.entities.enemies.enemy import Enemy
from objects.items.consumable import Flask
from objects.weapons.weapon import Weapon

from ui.ui_factory import UiFactory
from ui.bar import Bar
from ui.icon import Icon
from ui.slot import Slot

from build.level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
        pygame.display.set_caption('dev/2d-souls')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 26)
        self.main_sprites = pygame.sprite.Group()
        self.level_sprites = pygame.sprite.Group()
        # Map and levels
        self.row = 0
        self.col = 0
        self.map = [[None for _ in range(MAX_ROWS)] for _ in range(MAX_COLS)]
        self.level = None

        self.init_player()
        self.init_player_ui()
        self.init_main_sprites()
        # Create and load starting level
        self.switch_level()
        self.init_level_sprites()
 
    def init_player(self):
        self.player = Player(100, GROUND-200, PLAYER_WIDTH, PLAYER_HEIGHT, GREEN, PLAYER_MAX_HP, PLAYER_SPEED, PLAYER_MAX_MANA, PLAYER_MAX_STAMINA, JUMP_SPEED)
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

    def switch_level(self):
        if self.row >= MAX_ROWS or self.row < 0:
            print("Row level index out of range")
            pygame.quit()
            sys.exit()
        if self.col >= MAX_COLS or self.col < 0:
            print("Col level index out of range")
            pygame.quit()
            sys.exit()

        if self.map[self.row][self.col] == None:
            self.append_to_map(self.row, self.col)
        self.level = self.map[self.row][self.col] 

    def append_to_map(self, row, col):
        self.map[row][col] = Level(row, col)
        self.map[row][col].load_level()

    def init_main_sprites(self):
        self.main_sprites = pygame.sprite.Group(self.player, self.player.weapon, self.ico, self.p_hp_bar, self.p_mana_bar, self.p_stamina_bar, self.slot_1, self.slot_2)

    def init_level_sprites(self):
        self.level_sprites.empty()
        for enemy in self.level.enemies:
            self.level_sprites.add(enemy)
            self.level_sprites.add(enemy.weapon)
        for boss in self.level.bosses:
            self.level_sprites.add(boss)
            self.level_sprites.add(boss.weapon)

    def render_frame(self):
        self.screen.fill(BLACK)
        self.level.tiles.draw(self.screen)
        self.main_sprites.draw(self.screen)
        self.level_sprites.draw(self.screen)
        pygame.display.flip()

    def update_ui(self):
        self.p_hp_bar.update(self.player.hp)
        self.p_mana_bar.update(self.player.mana)
        self.p_stamina_bar.update(self.player.stamina)

    def handle_player(self):
        self.player.refill_stamina(1)
        self.player.update(self.level.tiles)

    def handle_enemies(self):
        for enemy in self.level.enemies:
            enemy.change_state(calc_dist(self.player.rect.center, enemy.rect.center))
            enemy.perform_action(calc_dir(self.player.rect.x, enemy.rect.x), self.player)
            enemy.update(self.level.tiles)
        for boss in self.level.bosses:
            boss.change_state(calc_dist(self.player.rect.center, boss.rect.center))
            boss.perform_action(calc_dir(self.player.rect.x, boss.rect.x), self.player)
            boss.update(self.level.tiles)

    def handle_level(self):
        if self.player.rect.x > SCREEN_WIDTH:
            self.col += 1
            self.player.rect.x = 0
            self.switch_level()
            self.init_level_sprites()
        elif self.player.rect.x < 0:
            self.col -= 1
            self.player.rect.x = SCREEN_WIDTH
            self.switch_level()
            self.init_level_sprites()
        elif self.player.rect.y > SCREEN_HEIGHT:
            self.row += 1
            self.player.rect.y = 0
            self.switch_level()
            self.init_level_sprites()
        elif self.player.rect.y < 0:
            self.row -= 1
            self.player.rect.y = SCREEN_HEIGHT
            self.switch_level()
            self.init_level_sprites()

    def check_game_end(self):
        if self.player.hp <= 0:
            print("You lost")
            pygame.quit()
            sys.exit()

    # Main game loop
    def game_loop(self):
        running = True 
        while running:
            # Check if player is alive
            self.check_game_end()

            # Handle level switching
            self.handle_level()

            # Process keyboard input
            handle_input(self.player, self.level, self.slot_1, self.slot_2)

            # Handle entities
            self.handle_player()
            self.handle_enemies()

            # Update frame
            self.update_ui()
            self.render_frame()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
