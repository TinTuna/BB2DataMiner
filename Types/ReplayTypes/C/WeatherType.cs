﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static BB2Replayer.Utils.Extensions;

namespace BB2Replayer.Replay.Types
{
	/* Weather table from LRB6:
	   2 Sweltering Heat: It’s so hot and humid that some players collapse from heat exhaustion. Roll a D6 for each player on the pitch at the end of a drive. On a roll of 1 the player collapses and may not be set up for the next kick-off.
	   3 Very Sunny: A glorious day, but the blinding sunshine causes a -1 modifier on all passing rolls.
	4-10 Nice: Perfect Blood Bowl weather.
	  11 Pouring Rain: It’s raining, making the ball slippery and difficult to hold. A -1 modifier applies to all catch, intercept, or pick-up rolls.
	  12 Blizzard: It’s cold and snowing! The ice on the pitch means that any player attempting to move an extra square (GFI) will slip and be Knocked Down on a roll of 1-2, while the snow means that only quick or short passes can be attempted.
	*/
	public enum WeatherType
	{
		[Label( "Disabled" )] Disabled = 0,
		[Label( "Sweltering Heat" )] SwelteringHeat = 2,
		[Label( "Very Sunny" )] VerySunny = 3,
		[Label( "Nice" )] Nice4 = 4,
		[Label( "Nice" )] Nice5 = 5,
		[Label( "Nice" )] Nice6 = 6,
		[Label( "Nice" )] Nice7 = 7,
		[Label( "Nice" )] Nice8 = 8,
		[Label( "Nice" )] Nice9 = 9,
		[Label( "Nice" )] Nice10 = 10,
		[Label( "Pouring Rain" )] PouringRain = 11,
		[Label( "Blizzard" )] Blizzard = 12
	}
}
