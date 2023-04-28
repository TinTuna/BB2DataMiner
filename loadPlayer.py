from xml.etree.ElementTree import Element
import Types.Player as Player

def loadPlayer(player: Element):
    # Find all the initial player states
    playerInitOpts = {}
    for playerDetail in player.iter():
        # Itterate over each player state and add it to the playerInitOpts
        if playerDetail.tag == "PlayerState":
            continue
        elif playerDetail.tag == "Cell":
            playerInitOpts[playerDetail.tag] = {
                "x": playerDetail.find('x').text,
                "y": playerDetail.find('y').text
            }
        elif playerDetail.tag == "Data":
            playerInitOpts[playerDetail.tag] = {
                "LobbyId": playerDetail.find('LobbyId').text if playerDetail.find('LobbyId') else '',
                "Ma": playerDetail.find('Ma').text if playerDetail.find('Ma') else '',
                "Name": playerDetail.find('Name').text if playerDetail.find('Name') else '',
                "Ag": playerDetail.find('Ag').text if playerDetail.find('Ag') else '',
                "Number": playerDetail.find('Number').text if playerDetail.find('Number') else '',
                "IdHead": playerDetail.find('IdHead').text if playerDetail.find('IdHead') else '',
                "Value": playerDetail.find('Value').text if playerDetail.find('Value') else '',
                "Av": playerDetail.find('Av').text if playerDetail.find('Av') else '',
                "St": playerDetail.find('St').text if playerDetail.find('St') else '',
                "ListSkills": playerDetail.find('ListSkills').text if playerDetail.find('ListSkills') else '',
                "IdPlayerTypes": playerDetail.find('IdPlayerTypes').text if playerDetail.find('IdPlayerTypes') else ''
            }
        else:
            playerInitOpts[playerDetail.tag] = playerDetail.text

    return Player.Player(playerInitOpts)