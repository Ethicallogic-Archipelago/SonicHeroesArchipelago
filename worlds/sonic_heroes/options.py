from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    Determines the goal of the seed

    Metal Madness: Beat Metal Madness
    """
    display_name = "Goal"
    option_metal_madness = 0
    default = 0


class GoalUnlockCondition(Choice):
    """
    Determines how the Goal level is unlocked

    Normal: Requires all 7 Chaos Emeralds plus the number of Emblems chosen

    Emblems Only: Only requires the chosen number of Emblems

    Emeralds Only: Only requires the 7 Chaos Emeralds with no Emblem requirements. Level Gates will still require Emblems to proceed
    """
    display_name = "Goal Unlock Condition"
    option_normal = 0
    option_emblems_only = 1
    option_emeralds_only = 2
    default = 0


class RequiredEmblemsPercent(Range):
    """
    What percent of the total emblems should be required to unlock the Final Goal? (rounded down)
    This also affects level gates (if enabled)
    There are currently 25 emblems per story
    The minimum value is 1 per gate and 1 additional for the final boss (unless there are 0 level gates)
    """

    display_name = "Required Emblems Percent"
    range_start = 0
    range_end = 100
    default = 80


class NumberOfLevelGates(Range):
    """
    The number emblem-locked gates which lock sets of levels. This is capped to 3 for only 1 story.
    """
    display_name = "Number of Level Gates"
    range_start = 0
    range_end = 5
    default = 3


class SonicStory(DefaultOnToggle):
    """
    Should Sonic Story Missions be enabled?
    """
    display_name = "Sonic Story Enabled"


class DarkStory(Toggle):
    """
    Should Dark Story Missions be enabled?
    """
    display_name = "Dark Story Enabled"


class RoseStory(Toggle):
    """
    Should Rose Story Missions be enabled?
    """
    display_name = "Rose Story Enabled"


class ChaotixStory(Toggle):
    """
    Should Chaotix Story Missions be enabled?
    """
    display_name = "Chaotix Story Enabled"


sonic_heroes_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        GoalUnlockCondition,
        RequiredEmblemsPercent,
    ]),
    OptionGroup("Level Gates", [
        NumberOfLevelGates,
    ]),
    OptionGroup("Story Options", [
        SonicStory,
        DarkStory,
        RoseStory,
        ChaotixStory,
    ])
]






@dataclass
class SonicHeroesOptions(PerGameCommonOptions):
    goal: Goal
    goal_unlock_condition: GoalUnlockCondition
    required_emblems_percent: RequiredEmblemsPercent

    number_level_gates: NumberOfLevelGates

    sonic_story: SonicStory
    dark_story: DarkStory
    rose_story: RoseStory
    chaotix_story: ChaotixStory
