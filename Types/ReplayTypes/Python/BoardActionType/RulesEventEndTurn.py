class RulesEventEndTurn():
    PlayingTeam = -1
    TouchdownScorer = -1
    ListTeamInfos = [{
    }]
    Turnover = -1
    NewDrive = -1

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)