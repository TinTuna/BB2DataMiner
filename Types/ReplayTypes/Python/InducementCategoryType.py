from enum import Enum

class InducementCategoryType(Enum):
    IrrelevantMinus6 = -6 # Don't know what this is either, but seems like it is a GUI thing as well. Leaning towards ignoring the negative values, really
    IrrelevantMinus5 = -5 # Don't know what this is either, but seems like it is a GUI thing as well. Leaning towards ignoring the negative values, really
    MercenarySave = -2 # Not entirely sure what this is, but seems like it's a GUI thing. Used for Bomber Dribblesnot in S28 finals, and he was never on the field
    BloodweiserBabe = 1 # 0-2
    Bribe = 2 # 0-3
    ExtraTeamTraining = 3 # 0-4
    HalflingMasterChef = 4 # 0-1
    WanderingApothecary = 5 # 0-2 Cyanide collates Igor and WanderingApo? No, this is wandering, Igor is separate
    Mercenary = 6 # Unlimited
    StarPlayer = 7 # 0-2
    Wizard = 8 # 0-1
    Igor = 9
    Journeyman = 10
    