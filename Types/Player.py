class Player():
    CanDeclareBlitz = False
    Gfi = 0
    Id = 0
    CanBlock = False
    CanAct = False
    Cell = {
        "x": 0,
        "y": 0
    }
    CanHandOff = False
    TackleZone = False
    MovePoint = 0
    Data = {
        "LobbyId": '',
        "Ma": 0,
        "Name": '',
        "Ag": 0,
        "Level": 0,
        "Number": 0,
        "Experience": 0,
        "IdHead": 0,
        "Value": 0,
        "Av": 0,
        "St": 0,
        "ListSkills": '',
        "IdPlayerTypes": 0
    }
    CanPass = False

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    # getter and setter fns
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)