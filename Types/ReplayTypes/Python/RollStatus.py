from enum import Enum

class RollStatusType(Enum):
    Final = 0,
    TeamReRolled = 1,
    NotReRolled = 2,
    ReRolledWithSkill = 3, # Pick-Up ball auto-rerolled with Sure Hands in S29 Wonderworlders v Crocs
    ReRolledWithSkill2 = 4, # Dodge auto-rerolled with Dodge in S29 Wonderworlders v Crocs
    NotReRolledWithSkill = 5