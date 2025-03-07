import pygame
import os
from const import *

# Custom Event
ITEM_PICKUP_EVENT = pygame.event.custom_type()

class Object(pygame.sprite.Sprite):

    def __init__(self, name, position, groups, player, collision_sprites, progression=None):

        super().__init__(groups)
        self.object = True

        self.object_name = name
        self.position = position
        self.groups = groups
        self.collision_sprites = collision_sprites
        self.player = player

        self.sprites = []

        self.load_images()

        # Sprites
        self.image = self.sprites[0]
        self.rect = self.image.get_frect(topleft=position)

        self.progression = progression

    def load_images(self):

        folder_path = os.path.join('assets', 'sprites', 'map', 'objects', self.object_name)

        file_count = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])

        for i in range(file_count):

            file_path = os.path.join('assets', 'sprites', 'map', 'objects', self.object_name, f'{i}.png')

            if file_path:

                self.sprites.append(pygame.image.load(file_path).convert_alpha())

    def interact(self):

        pass


class Chest(Object):

    def __init__(self, position, groups, player, item, collision_sprites, progression=None):

        super().__init__('chest', position, groups, player, collision_sprites, progression)

        self.image = pygame.transform.scale(self.image, CHEST_SIZE)  # const.py
        self.rect = self.image.get_frect(topleft=self.position)

        self.opened = False
        self.inventory = [item]
        self.open_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds','object', 'chest', 'open','0.wav'))

    def interact(self):

        if not self.opened:

            self.opened = True
            self.image = self.sprites[1]
            self.image = pygame.transform.scale(self.image, CHEST_SIZE)
            self.rect = self.image.get_frect(topleft=self.position)

            picked_item = self.inventory[0]
            self.player.inventory.append(picked_item)
            self.open_sound.play()

            pygame.event.post(pygame.event.Event(ITEM_PICKUP_EVENT, {"message": f"Picked up {picked_item.name}!"}))

            if self.progression:

                for sprite in self.progression:

                    sprite.kill()