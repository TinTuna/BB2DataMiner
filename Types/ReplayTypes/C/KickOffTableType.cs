using System.ComponentModel;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	enum KickOffTableType
	{
		[Label( "UNKNOWN" )] Unknown = 0, // Probably a bug, since this isn't a 2D6 result
		[Description( "The fans exact gruesome revenge on the referee for some of the dubious decisions he has made, either during this match or in the past. His replacement is so intimidated that he can be more easily persuaded to look the other way. Each team receives 1 additional Bribe to use during this game." )]
		[Label( "Get the Ref" )] GetTheRef = 2,
		[Description( "The trash talk between two opposing players explodes and rapidly degenerates, involving the rest of the players.If the receiving team’s turn marker is on turn 7 for the half, both teams move their turn marker back one space as the referee resets the clock back to before the fight started.If the receiving team has not yet taken a turn this half the referee lets the clock run on during the fight and both teams’ turn markers are moved forward one space. Otherwise roll a D6.On a 1 - 3, both teams’ turn markers are moved forward one space. On a 4 - 6, both team’s turn markers are moved back one space." )]
		[Label( "Riot" )] Riot = 3,
		[Description( "The kicking team’s coach may reorganize his players – in other words he can set them up again into another legal defence. The receiving team must remain in the set - up chosen by their coach." )]
		[Label( "Perfect Defence" )] PerfectDefence = 4,
		[Description( "The ball is kicked very high, allowing a player on the receiving team time to move into the perfect position to catch it. Any one player on the receiving team who is not in an opposing player’s tackle zone may be moved into the square where the ball will land no matter what their MA may be, as long as the square is unoccupied." )]
		[Label( "High Kick" )] HighKick = 5,
		[Description( "Each coach rolls a D3 and adds their team’s FAME and the number of cheerleaders on their team to the score. The team with the highest score is inspired by their fans' cheering and gets an extra re-roll this half. If both teams have the same score, then both teams get a re-roll." )]
		[Label( "Cheering Fans" )] CheeringFans = 6,
		[Description( "Make a new roll on the Weather table. Apply the new Weather roll. If the new Weather roll was a ‘Nice’ result, then a gentle gust of wind makes the ball scatter one extra square in a random direction before landing." )]
		[Label( "Changing Weather" )] ChangingWeather = 7,
		[Description( "Each coach rolls a D3 and adds their FAME and the number of assistant coaches on their team to the score. The team with the highest total gets an extra team re-roll this half thanks to the brilliant instruction provided by the coaching staff. In case of a tie both teams get an extra team re-roll." )]
		[Label( "Brilliant Coaching" )] BrilliantCoaching = 8,
		[Description( "The offence start their drive a fraction before the defence is ready, catching the kicking team flat-footed. All of the players on the receiving team are allowed to move one square. This is a free move and may be made into any adjacent empty square, ignoring tackle zones. It may be used to enter the opposing half of the pitch." )]
		[Label( "Quick Snap!" )] QuickSnap = 9,
		[Description( "The defence start their drive a fraction before the offence is ready, catching the receiving team flat-footed.The kicking team receives a free ‘bonus’ turn: however, players that are in an enemy tackle zone at the beginning of this free turn may not perform an Action. The kicking team may use team re-rolls during a Blitz. If any player suffers a turnover then the bonus turn ends immediately." )]
		[Label( "Blitz!" )] Blitz = 10,
		[Description( "An enraged fan hurls a large rock at one of the players on the opposing team. Each coach rolls a D6 and adds their FAME to the roll. The fans of the team that rolls higher are the ones that threw the rock. In the case of a tie a rock is thrown at each team! Decide randomly which player in the other team was hit (only players on the pitch are eligible) and roll for the effects of the injury straight away. No Armour roll is required." )]
		[Label( "Throw a Rock" )] ThrowARock = 11,
		[Description( "Both coaches roll a D6 for each opposing player on the pitch and add their FAME to the roll. If a roll is 6 or more after modification then the player is Stunned (players with the Ball & Chain skill are KO'd). A roll of 1 before adding FAME will always have no effect." )]
		[Label( "Pitch Invasion" )] PitchInvasion = 12,
	}
}
