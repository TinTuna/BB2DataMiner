from enum import Enum

class BoardActionType(Enum):
    Move = 0
    Block = 1
    Blitz = 2
    Pass = 3
    HandOff = 4
    Foul = 5
    KnockDown = 6
    KickOff = 7
    Bounce = 8
    Catch = 9
    TouchDown = 10
    StunnedToProne = 11
    KORecovery = 12
    # ?? = 13
    PickUpBall = 14
    NegaTrait = 15 # Negative trait
    RightStuffLanding = 16
    AlwaysHungrySquirmFree = 17 # Squirm Free From Always Hungry
    Shadowing = 18
    Stab = 19
    # ?? = 20
    Leap = 21
    # ?? = 22
    BallAndChain = 23
    # ?? = 24
    Chainsaw = 25
    MultipleBlock = 26
    HypnoticGaze = 27
    # ?? = 28
    PassBlock = 29
    HalflingMasterChef = 30
    Fireball = 31
    FireballHit = 32
    LightningBolt = 33
    Referee = 34
    RightStuffLandingOnAnotherPlayer = 35
    # ?? = 36
    MovePlayerUnderBall = 37
    # ?? = 38
    DodgeFromDivingTackle = 39
    # ?? = 40
    MultipleBlockStab = 41
    ActivatePlayer = 42
    # ?? = 43
    # ?? = 44
    # ?? = 45
    NumberOfFans = 46
    Weather = 47
    SwelteringHeat = 48
    Feed = 49
    BombDirectHit = 50
    BombAdjacentHit = 51
    ThrowABomb = 52
    BombCatch = 53
    BombScatter = 54
    BombReThrow = 55