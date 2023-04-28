class RulesEventBoardAction():
    PlayerId = -1
    RequestType = -1
    ActionType = -1
    Order = {
        'CellTo': {
            'cell': {
                'x': -1,
                'y': -1
            }
        },
        'CellFrom': {
            'x': -1,
            'y': -1
        },
    }
    Results = [{
        'BoardActionResult': {
            'Requirement': -1,
            'ListModifiers': '',
            'IsOrderCompleted': -1,
            'RollType': -1,
            'CoachChoices': {
                'ConcernedTeam': -1,
                'ListCells': [{
                    'cell': {
                        'x': -1,
                        'y': -1
                    }
                }],
                'ListDices': '',
                'ListSkills': '',
            }
        }
    }]

    def __init__(self, opts) -> None:
        for key in opts:
            self.__setitem__(key, opts[key])

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
