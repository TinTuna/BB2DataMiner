using System.ComponentModel;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	public enum DiceModifierType
	{
		[Label( "Bloodweiser Babes" )] BloodweiserBabe = 0,
		Stunty = 2,
		[Label( "Tackle Zone" )] TackleZone = 3,
		[Label( "Accurate Pass" )] AccuratePass = 4,
		PickUp = 5,
		[Label( "Quick Pass" )] QuickPass = 6,
		[Label( "Short Pass" )] ShortPass = 7,
		[Label( "Long Pass" )] LongPass = 8,
		[Label( "Long Bomb" )] LongBomb = 9,
		[Label( "Hand-off" )] HandOff = 10,
		Assist = 11,
		DefenderAssist = 12,
		DefenderBaseContactNoAssist = 13,
		AttemptingAnInterception = 14,
		[Label( "Very Sunny" )] VerySunny = 15,
		[Label( "Pouring Rain" )] PouringRain = 16,
		Blizzard = 17,
		ReallyStupidHelp = 18,
		WildAnimalBlock = 19,
		[Label( "Bloodweiser Babes" )] BloodweiserBabes = 21, // Seems to be both 0 and 21 in different games. No clue as to why
		FireballMightyBlow = 22,
		ThrowTeamMate = 23,
		ShadowingOwnMA = 24,
		ShadowingShadowingMA = 25,
		TentaclesDodgerSt = 26,
		TentaclesPlayerST = 27,
		[Label( "Mighty Blow/Dirty Player/Chainsaw")] SkillModifier = 28, // Lots of skills use this. Horns, Two Heads, Mighty Blow, Stunty, Prehensile Tail, Accurate, Strong Arm, Disturbing Presence, Very Long Legs, Dirty Player, Kick, Diving Tackle, Diving Catch, Chainsaw, and that list is probably not even exhaustive
		[Label( "Mighty Blow")] MightyBlowInjury = 29, // Definitely MB +1 for injury roll with mighty blow as well, pushed into crowd, but no skill id. But see example in Champion Ladder X: Please dont run away vs Golden Green. 
		Astrogranite = 30, // This was +1 to armour break on a gfri with no other players nearby, Brick Far'th was doing the GFI'ing
		Grass = 31, // Not 100% sure, but it was -1 to armour break on a gfi with no particular skills nearby
		[Label( "Niggling Injury")] NigglingInjury = 32,
		[Label( "Jump Up" )] JumpUp = 33,
	}
}
