WINDOW_W = 800
WINDOW_H = 600

TILE_SIZE = 32

## Entities ##

## Player ##
PLAYER_SIZE = 32, 32
PLAYER_HITBOX = -20, -20

# Player Attack
PLAYER_ATTACK_WIDTH = 32
PLAYER_ATTACK_HEIGHT = 35
PLAYER_ATTACK_COOLDOWN = 0.5 # 0.5 = 500ms
PLAYER_EQUIP_COOLDOWN = 0.1 # 0.5 = 500ms

# Player Health, Speed
PLAYER_HEALTH = 100
PLAYER_SPEED = 200

# Player Interactions
PLAYER_INTERACTION_DISTANCE = 30

# Player Inventory
PLAYER_INVENTORY_EQUIP_COOLDOWN = 200 # 200ms
PLAYER_INVENTORY_MOUSE_EQUIP_COOLDOWN = 200 # 200ms

# Slash
SLASH_SPEED = 20

## Enemies ##
ENEMY_LOS = (300, 300) # LOS dimensions (width, height)
ENEMY_DISTANCE_THRESHOLD = 40 # Minimum distance threshold

## Slimes ##
SLIME_SIZE = 32,25
SLIME_HITBOX = 0, 0
SLIME_ANIMATION_SPEED = 10

# Slime Health, Speed, Damage
SLIME_HEALTH = 200
SLIME_SPEED = 50
SLIME_DAMAGE = 5

# Water Slime Health, Speed, Damage
WATER_SLIME_HEALTH = 200
WATER_SLIME_SPEED = 50
WATER_SLIME_DAMAGE = 5

# Fire Slime Health, Speed, Damage
FIRE_SLIME_HEALTH = 200
FIRE_SLIME_SPEED = 50
FIRE_SLIME_DAMAGE = 5

# Earth Slime Health, Speed, Damage
EARTH_SLIME_HEALTH = 200
EARTH_SLIME_SPEED = 50
EARTH_SLIME_DAMAGE = 5

# Air Slime Health, Speed, Damage
AIR_SLIME_HEALTH = 200
AIR_SLIME_SPEED = 50
AIR_SLIME_DAMAGE = 5


## Objects ##
CHEST_SIZE = 32, 28