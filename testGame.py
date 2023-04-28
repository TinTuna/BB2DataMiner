import xml.etree.ElementTree as ET

# load XML from ReplayStubs
# parse XML into a list of players 

teamsLoaded = False
teams = {
    0: 'testesstestestes',
    1: 'Marauding Mashers'
}

# tree = ET.parse('ReplayStubs/0b69d36b97d781814b46d138e61de3cb_2023-02-26_12_43_03')
tree = ET.parse('ReplayStubs/1c43d98608e4cd7055d896f90c9b6bc1_2021-02-05_21_02_22')

steps = tree.getroot().findall('.//ReplayStep')

eventTpyes = set()

for step in steps:
    children = list(step)
    for child in children:
        eventTpyes.add(child.tag)
        match child.tag:
            case 'BoardState':
                if teamsLoaded:
                    pass
                else:
                    teamsLoaded = True
                    print('Teams loaded')
                    
                pass
            case 'GameInfos':
                # print(child.attrib)
                pass
            case 'RulesEventKickOffChoice':
                try: 
                    choosingTeam = child.find('ChosingTeam').text
                except:
                    choosingTeam = 0
                try:
                    kickoffTeam = child.find('KickOffTeam').text
                except:
                    kickoffTeam = 0
                if choosingTeam == kickoffTeam:
                    print(f'{teams[int(choosingTeam)]} won the toss and chose to kick off')
                else:
                    print(f'{teams[int(choosingTeam)]} won the toss and chose {teams[int(kickoffTeam)]} to kick off')
                pass
            case 'RulesEventBoardAction':
                # print(child.attrib)
                pass
            case 'RulesEventKickOffTable':
                # print(child.attrib)
                pass
            case 'RulesEventWaitingRequest':
                # print(child.attrib)
                pass
            case 'RulesEventInducementsInfos':
                # print(child.attrib)
                pass
            case 'RulesEventApplyInducements':
                # print(child.attrib)
                pass
            case 'RulesEventSpecialAction':
                # print(child.attrib)
                pass
            case 'RulesEventForcedDices':
                # print(child.attrib)
                pass
            case 'RulesEventGameFinished':
                # print(child.attrib)
                pass
            case 'RulesEventSetUpAction':
                # print(child.attrib)
                pass
            case 'RulesEventEndTurn':
                # print(child.attrib)
                pass
            case 'RulesEventSetUpConfiguration':
                # print(child.attrib)
                pass
            case 'RulesEventCoachChoice':
                # print(child.attrib)
                pass