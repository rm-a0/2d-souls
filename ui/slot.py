import pygame

from core.constants import SLOT_WIDTH, SLOT_HEIGHT, GREY, WHITE

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y, font): 
        super().__init__()
        self.image = pygame.Surface((SLOT_WIDTH, SLOT_HEIGHT))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.item = None
        self.font = font

    # Assign new item to the slot
    def switch_item(self, item):
        self.item = item

    # Update count of item stored in slot
    def update_count(self):
        self.image.fill(GREY)
        if self.item:
            if hasattr(self.item, "count"):
                count_txt = self.font.render(str(self.item.count), True, WHITE)
                self.image.blit(count_txt, (self.rect.width - 15, self.rect.height - 25))
