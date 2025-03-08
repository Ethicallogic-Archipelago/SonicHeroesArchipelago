from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, OptionGroup, PerGameCommonOptions, DeathLink


class Goal(Choice):
    """
    Determines the goal of the seed

    Metal Overlord: Beat Metal Overlord
    """
    display_name = "Goal"
    option_metal_overlord = 0
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




class SkipMetalMadness(DefaultOnToggle):
    """
    Skips Metal Madness when selecting it from level select and goes directly to Metal Overlord (final boss)
    """
    display_name = "Skip Metal Madness"



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


class RequiredRank(Choice):
    """
    Determines what minimum Rank is required to send a check for a mission
    """
    display_name = "Required Rank"
    option_e = 0
    option_d = 1
    option_c = 2
    option_b = 3
    option_a = 4
    default = 0


class AlwaysHaveBonusKey(Toggle):
    """
    The number emblem-locked gates which lock sets of levels. This is capped to 3 for only 1 story.
    """
    display_name = "Always Have Bonus Key for Emerald Stages"



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


class RingLink(Toggle):
    """
    Ring Link
    """
    display_name = "Ring Link Enabled"


class ModernRingLoss(Toggle):
    """
    Only lose up to 20 Rings when hit instead of all
    """
    display_name = "Modern Ring Loss Enabled"



sonic_heroes_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        GoalUnlockCondition,
        SkipMetalMadness,
        RequiredEmblemsPercent,
        RequiredRank,
        AlwaysHaveBonusKey
    ]),
    OptionGroup("Level Gates", [
        NumberOfLevelGates,
    ]),
    OptionGroup("Story Options", [
        SonicStory,
        DarkStory,
        RoseStory,
        ChaotixStory,
    ]),
    OptionGroup("Ring Options", [
        RingLink,
        ModernRingLoss,
    ]),
    OptionGroup("DeathLink", [
        DeathLink
    ]),
]


sonic_heroes_option_names_list = [
    "goal",
    "goal_unlock_condition",
    "skip_metal_madness",
    "required_emblems_percent",
    "required_rank",
    "always_have_bonus_key",
    "number_level_gates",
    "sonic_story",
    "dark_story",
    "rose_story",
    "chaotix_story",
    "ring_link",
    "modern_ring_loss",
    "death_link"
]



@dataclass
class SonicHeroesOptions(PerGameCommonOptions):
    goal: Goal
    goal_unlock_condition: GoalUnlockCondition
    skip_metal_madness: SkipMetalMadness
    required_emblems_percent: RequiredEmblemsPercent
    required_rank: RequiredRank
    always_have_bonus_key: AlwaysHaveBonusKey

    number_level_gates: NumberOfLevelGates

    sonic_story: SonicStory
    dark_story: DarkStory
    rose_story: RoseStory
    chaotix_story: ChaotixStory

    ring_link: RingLink
    modern_ring_loss: ModernRingLoss

    death_link: DeathLink
