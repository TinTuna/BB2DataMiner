class RulesEventKickOffTable():
    

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)