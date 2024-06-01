import pygame

from core.constants import JUMP

class Flask(pygame.sprite.Sprite):
    def __init__(self, flask_type, count, refill_amount): 
        super().__init__()
        self.flask_type = flask_type 
        self.max_count = count 
        self.count = count 
        self.refill_amount = refill_amount 

    # Refills player stat by certain amount and decrements quantity 
    def refill_stat(self, player):
        state = getattr(player, "state")
        if self.count > 0 and state != JUMP:
            self.count -= 1
            stat = getattr(player, self.flask_type)
            max_stat = getattr(player, f'max_{self.flask_type}', stat)
            if self.refill_amount + stat > max_stat:
                setattr(player, self.flask_type, max_stat)
            else:
                setattr(player, self.flask_type, stat + self.refill_amount)

    # Increments flask quantity
    def refill_flask(self):
        if self.count < self.max_count:
            self.count += 1

    # Increases refill amount by given amount
    def inc_refill_amount(self, amount):
        self.refill_amount += amount