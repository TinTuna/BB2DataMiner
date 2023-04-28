using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	public enum RollStatusType
	{
		[Label( "Final result" )] Final = 0,
		[Label( "Re-rolled with Team RR" )] TeamReRolled = 1,
		[Label( "Not re-rolled" )] NotReRolled = 2,
		[Label( "Re-rolled with skill" )] ReRolledWithSkill = 3, // Pick-Up ball auto-rerolled with Sure Hands in S29 Wonderworlders v Crocs
		[Label( "Re-rolled with skill" )] ReRolledWithSkill2 = 4, // Dodge auto-rerolled with Dodge in S29 Wonderworlders v Crocs
		[Label( "Not re-rolled with skill" )] NotReRolledWithSkill = 5
	}
}
