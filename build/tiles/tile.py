import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, texture_path=None):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        if texture_path:
            try:
                texture = pygame.image.load(texture_path).convert_alpha()
                texture = pygame.transform.scale(texture, (width, height))
                self.image.blit(texture, (0, 0))
            except pygame.error as e:
                print(f"Error loading texture {texture_path}: {e}")
                self.image.fill(color)
        else:
            self.image.fill(color)

