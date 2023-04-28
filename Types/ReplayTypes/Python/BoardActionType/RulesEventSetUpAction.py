class RulesEventSetUpAction():
    PlayerPosition = {
        "y": -1,
        "x": -1
    }
    NewPosition = {
        "y": -1,
        "x": -1
    }
    ValidAction = -1
    SetUpState = {
        "ScrimmageValid": -1,
        "BotWideZoneValid": -1,
        "PlayersNumberValid": -1,
        "TopWideZoneValid": -1,
        "ValidSetup": -1
    }

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
