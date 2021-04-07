from pathlib import Path


home = Path.home()
assets: Path = Path(__file__).parent / 'assets'

MAIN_MUSIC = assets / 'Sappheiros - Lights.mp3'
DEFAULT_VOLUME = .25
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Fishy"
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5