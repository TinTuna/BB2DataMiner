from enum import Enum

class BlockDiceType(Enum):
    Skull = 0 # Attacker Down
    BD = 1 # Both Down
    Push = 2 # Pushed
    Stumble = 3 # Defender Stumbles
    Pow = 4 # Defender Down
    
class DiceType(Enum):
    D3 = 1
    # D6
    # D8
    # Block
    # D68