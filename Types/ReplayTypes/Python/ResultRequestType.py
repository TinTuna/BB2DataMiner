from enum import Enum

# 0 - Outcome / decision
# 1 - Opposing player choosing dice? This is if opponent chooses block dice when you block with less strength) Also, opposing player choosing whether to pile on (re-roll) for injury. Seems to be consistent for choosing re-roll or not
# 2 - Active player choosing dice (no further RR options)
# 3 - Choose player to take some action? I.e. shadowing, but also touchback? Choose multiple block target? Also, choose direction in push. So it is choosing a _cell_ perhaps. Also, follow-up
# 4 - Skill used to deny other use of somesuch? Fend/Tackle. Maybe those that can't be optional?
# 5 - Active player choose dice or Re-Roll
# 6 - Choose secondary target for stab... very specific

class ResultRequestType(Enum):
    Outcome = 0
    ChooseWhetherToReroll = 1
    ChooseDiceNoRR = 2
    ChooseCell = 3
    UseSkill = 4
    ChooseDiceOrRR = 5
    ChooseCell2 = 6 # Secondary target for multiple block stab is the only case I've seen