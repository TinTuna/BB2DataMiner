﻿from enum import Enum

# Weather table from LRB6:
# 2 Sweltering Heat: It’s so hot and humid that some players collapse from heat exhaustion. Roll a D6 for each player on the pitch at the end of a drive. On a roll of 1 the player collapses and may not be set up for the next kick-off.
# 3 Very Sunny: A glorious day, but the blinding sunshine causes a -1 modifier on all passing rolls.
# 4-10 Nice: Perfect Blood Bowl weather.
# 11 Pouring Rain: It’s raining, making the ball slippery and difficult to hold. A -1 modifier applies to all catch, intercept, or pick-up rolls.
# 12 Blizzard: It’s cold and snowing! The ice on the pitch means that any player attempting to move an extra square (GFI) will slip and be Knocked Down on a roll of 1-2, while the snow means that only quick or short passes can be attempted.
	

class WeatherType(Enum):
    Disabled = 0
    SwelteringHeat = 2
    VerySunny = 3
    Nice4 = 4
    Nice5 = 5
    Nice6 = 6
    Nice7 = 7
    Nice8 = 8
    Nice9 = 9
    Nice10 = 10
    PouringRain = 11
    Blizzard = 12