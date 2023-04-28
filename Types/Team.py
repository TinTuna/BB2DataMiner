class Team():
    KickOffTurn = 0
    HandOfferId = 0
    FoulAvailable = False
    PasserId = 0
    BlitzerId = 0
    Fame = 0
    InducementsTurn = 0
    ListInducements = ''
    TeamRerollAvailable = 0
    RerollNumber = 0
    ListPitchPlayers = []
    Data = {
        "LobbyId": '',
        "Value": 0,
        "Cheerleaders": 0,
        "TreasuryBeforeInducements": 0,
        "Name": '',
        "Popularity": 0,
        "Apothecary": False,
        "IdCheerleadersRace": 0,
        "TeamId": 0,
        "Sponsor": '',
        "IdRace": 0,
        "Treasury": 0,
        "Reroll": 0,
        "Logo": '',
        "CoachSlot": 0,
        "TeamColor": 0
    }
    ListMercenaries = []
    NbSupporters = 0
    Side = 0
    ApothecaryAvailable = False

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    # getter and setter fns
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)