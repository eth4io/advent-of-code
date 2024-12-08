from enum import Enum

class Colour(Enum):
  GREEN = '92m'
  LIGHT_BLUE = '34m'
  ORANGE = '38;2;255;165;0m'
  PINK = '38;2;255;105;180m'
  RED = '91m'


def colourify(colour: Colour, text: str or int) -> str:
  return f'\033[{colour.value}{text}\033[0m'


