import os
from random import randint

import pygame
from gameobjects.vector2 import Vector2

from game.entities import Hero
from settings import game_settings


def draw_background_with_tiled_map(game_screen, game_map):
    # draw map data on screen
    for layer in game_map.visible_layers:
        for x, y, gid, in layer:
            tile = game_map.get_tile_image_by_gid(gid)
            if not tile:
                continue

            game_screen.blit(
                tile,
                (x * game_map.tilewidth,
                 y * game_map.tileheight)
            )


def load_alpha_image(resource_img):
    path = os.path.join(
        game_settings.base_dir,
        'img/{}'.format(resource_img),
    )

    return pygame.image.load(path)


green_hero_img = load_alpha_image('green_hero.png')
red_hero_img = load_alpha_image('red_hero.png')


def get_left_random_location():
    x, y = game_settings.left_home_location
    randX, randY = randint(x, x + 80), randint(80, game_settings.screen_height - 40)
    return Vector2(randX, randY)


def get_right_random_location():
    x, y = game_settings.right_home_location
    randX, randY = randint(x - 80, x), randint(80, game_settings.screen_height - 40)
    return Vector2(randX, randY)


def create_hero(world, hero_type):
    if hero_type == 'green':
        location = get_left_random_location()
        image = green_hero_img
    elif hero_type == 'red':
        location = get_right_random_location()
        image = red_hero_img
    else:
        raise KeyError("error type")

    hero = Hero(world, image, None, hero_type)
    hero.location = location
    world.add_entity(hero)
    return hero


def has_close_entities(world, item):
    entities = world.entities
    for entity in entities.values():
        item_location = entity.location
        if item.id != entity.id and item_location.get_distance_to(item.location) < 30:
            return True

    return False


def initial_heroes(world):
    green_hero_nums = game_settings.default_hero_num
    for _ in range(green_hero_nums):
        item = create_hero(world, 'green')
        while has_close_entities(world, item):
            item.location = get_left_random_location()

    red_hero_nums = game_settings.default_hero_num
    for _ in range(red_hero_nums):
        item = create_hero(world, 'red')
        while has_close_entities(world, item):
            item.location = get_right_random_location()