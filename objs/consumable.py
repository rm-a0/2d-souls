import pygame
from constants import *

class Flask(pygame.sprite.Sprite):
    def __init__(self, flask_type, qty, rfl_amt): 
        super().__init__()
        self.flask_type =flask_type 
        self.max_qty = qty
        self.qty = qty
        self.rfl_amt = rfl_amt

    # Refills player stat by certain amount and decrements quantity 
    def refill_stat(self, player):
        if self.qty > 0:
            self.qty -= 1
            stat = getattr(player, self.flask_type, 0)
            max_stat = getattr(player, f'max_{self.flask_type}', stat)
            if self.rfl_amt + stat > max_stat:
                setattr(player, self.flask_type, max_stat)
            else:
                setattr(player, self.flask_type, stat + self.rfl_amt)

    # Increments flask quantity
    def refill_flask(self):
        if self.qty < self.max_qty:
            self.qty += 1

    # Increases refill amount by given amount
    def inc_refill_amount(self, amt):
        self.rfl_amt += amt