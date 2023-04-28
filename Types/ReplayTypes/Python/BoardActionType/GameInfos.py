class GameInfos():
    AnswerClock = -1
    TurnClockDuration = -1
    CoachesInfos = [{
        'CoachInfos': {
            'Slot': -1,
            'Login': '',
            'UserId': ''
        }
    }]
    Id = ''
    LevelCabalVision = -1
    LocalCoachSlot = -1
    State = -1
    Stadium = ''
    BallType = ''
    TurnClock = -1
    NameStadium = ''
    LevelStadium = -1
    RowLeague = {
        'Edition': -1,
        'IdOwner': -1,
        'LeagueType': -1,
        'Logo': '',
        'Id': {
            'Value': ''
        },
        'Solo': -1,
        'Phase': -1,
        'Name': '',
        'Created': '',
        'NbRegisteredTeams': -1
    }
    Mode = -1
    RowCompetition = {
        'IdPreviousEdition': {
            'Value': '',
        },
        'IdOwner': -1,
        'Id': {
            'Value': ''
        },
        'CloneOnNextLeagueEdition': -1,
        'LeaguePhase': -1,
        'IdLeague': {
            'Value': ''
        },
        'PrematchEvents': -1,
        'Flags': -1,
        'IdCompetitionTypes': -1,
        'NbRounds': -1,
        'NbTeamsMax': -1,
        'CompetitionStatus': -1,
        'CurrentRound': -1,
        'Name': '',
        'LeagueEdition': -1,
        'NbRegisteredTeams': -1,
        'TurnDuration': -1,
    }

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
