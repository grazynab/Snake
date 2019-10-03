from enum import Enum
# dla Python >3.6, dla wersji 2.7 from aenum import Enum

class GameState(Enum):
    IN_PROGRESS = 1
    OVER = 2