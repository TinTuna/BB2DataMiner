from enum import Enum

class DiceModifierType(Enum):
    BloodweiserBabe = 0
    # ?? = 1
    Stunty = 2
    TackleZone = 3
    AccuratePass = 4
    PickUp = 5
    QuickPass = 6
    ShortPass = 7
    LongPass = 8
    LongBomb = 9
    HandOff = 10
    Assist = 11
    DefenderAssist = 12
    DefenderBaseContactNoAssist = 13
    AttemptingAnInterception = 14
    VerySunny = 15
    PouringRain = 16
    Blizzard = 17
    ReallyStupidHelp = 18
    WildAnimalBlock = 19
    # ?? = 20
    BloodweiserBabes = 21 # Seems to be both 0 and 21 in different games. No clue as to why
    FireballMightyBlow = 22
    ThrowTeamMate = 23
    ShadowingOwnMA = 24
    ShadowingShadowingMA = 25
    TentaclesDodgerSt = 26
    TentaclesPlayerST = 27
    SkillModifier = 28 # Lots of skills use this. Horns, Two Heads, Mighty Blow, Stunty, Prehensile Tail, Accurate, Strong Arm, Disturbing Presence, Very Long Legs, Dirty Player, Kick, Diving Tackle, Diving Catch, Chainsaw, and that list is probably not even exhaustive
    MightyBlowInjury = 29
    Astrogranite = 30
    Grass = 31
    NigglingInjury = 32
    JumpUp = 33