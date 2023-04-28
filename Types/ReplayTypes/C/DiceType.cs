using System.ComponentModel;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	public enum BlockDiceType
	{
		Skull = 0, // Attacker Down
		BD = 1, // Both Down
		Push = 2, // Pushed
		Stumble = 3, // Defender Stumbles
		Pow = 4, // Defender Down
	}

	public enum DiceType
	{
		D3 = 1,
		D6,
		D8,
		Block,
		D68
	}
}
