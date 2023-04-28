using System.ComponentModel;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	enum InducementCategoryType
	{
		IrrelevantMinus6 = -6, // Don't know what this is either, but seems like it is a GUI thing as well. Leaning towards ignoring the negative values, really
		IrrelevantMinus5 = -5, // Don't know what this is either, but seems like it is a GUI thing as well. Leaning towards ignoring the negative values, really
		MercenarySave = -2, // Not entirely sure what this is, but seems like it's a GUI thing. Used for Bomber Dribblesnot in S28 finals, and he was never on the field
		[Label( "Bloodweiser Babes" )] BloodweiserBabe = 1, // 0-2
		Bribe = 2, // 0-3
		[Label( "Extra Team Training" )] ExtraTeamTraining = 3, // 0-4
		[Label( "Halfling Master Chef" )] HalflingMasterChef = 4, // 0-1
		[Label( "Wandering Apothecary" )] WanderingApothecary = 5, // 0-2 Cyanide collates Igor and WanderingApo? No, this is wandering, Igor is separate
		Mercenary = 6, // Unlimited
		[Label( "Star Player" )] StarPlayer = 7, // 0-2
		Wizard = 8, // 0-1
		Igor = 9,
		Journeyman = 10,
	}
}
