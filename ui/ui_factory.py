from core.constants import RED, BLUE, GREEN, SCREEN_HEIGHT, GROUND

from ui.icon import Icon
from ui.bar import Bar
from ui.slot import Slot

class UiFactory:
    @staticmethod
    def create_player_hp_bar(player):
        return Bar(
            120,
            20,
            player.hp,
            RED
        )

    @staticmethod
    def create_player_mana_bar(player):
        return Bar(
            120,
            50,
            player.mana,
            BLUE 
        )

    @staticmethod
    def create_player_stamina_bar(player):
        return Bar(
            120,
            80,
            player.stamina,
            GREEN 
        )

    @staticmethod
    def create_boss_hp_bar(boss):
        return Bar(
            200,
            SCREEN_HEIGHT - 50,
            boss.hp,
            RED
        )

    @staticmethod
    def create_slot_1(font):
        return Slot(
            20,
            GROUND + 20,
            font 
        )

    @staticmethod
    def create_slot_2(font):
        return Slot(
            80,
            GROUND + 20,
            font 
        )

    @staticmethod
    def create_main_icon():
        return Icon(
            20,
            20
        )
