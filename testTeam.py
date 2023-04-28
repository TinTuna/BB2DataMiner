import Types.Player as Player
import Types.Team as Team
import xml.etree.ElementTree as ET

# load XML from ReplayStubs
# parse XML into a list of players 


tree = ET.parse('ReplayStubs/0b69d36b97d781814b46d138e61de3cb_2023-02-26_12_43_03')

# LPPAll = tree.findall('.//ListPitchPlayers')

# print each players name
# for player in players:
#     print(player.Data["Name"])
# print(len(players))

def getPlayersFromLPP(LPP):
    ids = []
    players = []

    for playerStates in LPP.findall('.//PlayerState'):
        # check if this player is already in the list
        if playerStates.find('.//Id').text in ids:
            continue
        

    return players

teams = []

rSteps = tree.findall('.//ReplayStep')
s1 = rSteps[0].findall('.//TeamState')
for teamStates in s1:
    teamInitOpts = {}
    for team in teamStates:
        if team.tag == "Data":
            teamInitOpts[team.tag] = {}
            for data in team:
                teamInitOpts[team.tag][data.tag] = data.text
        else:
            teamInitOpts[team.tag] = team.text
    # add players to team
    teamInitOpts['ListPitchPlayers'] = getPlayersFromLPP(teamStates)

    teams.append(Team.Team(teamInitOpts))
