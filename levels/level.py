import json
import os

from core.const import *

class Level:
    def __init__(self, x, y, base_path):
        self.name = f"lvl_{x}_{y}"
        self.x = x 
        self.y = y
        self.tilemap = []
        self.enemies = []
        self.bosses = []
        self.objects = []
        self.base_path = base_path

    def load_level(self):
        filepath = os.path.join(self.base.path, self.level_name)
        self.tilemap = self.load_tilemap(os.path.join(filepath, 'tilemap.txt'))
        self.enemies = self.load_json(os.path.join(filepath, 'enemies.json'))
        self.bosses = self.load_json(os.path.join(filepath, 'bosses.json'))
        self.objects = self.load_json(os.path.join(filepath, 'objects.json'))

    def load_tilemap(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return [list(line.strip()) for line in f]
        return []

    def load_json(self, path):
        if not path or not os.path.exists(path):
            return []
        with open(path, 'r') as f:
            data = json.load(f)
        return self.decode_json(data)

    def decode_json(self, data):
        return
