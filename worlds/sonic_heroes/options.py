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


class ExtraEmblems(Range):
    """
    How many extra emblems to add to the itempool?
    This is capped to avoid too many items
    There are currently 12 emblems per Story per Mission Type Enabled (A or B or Both)
    If Sanity options are enabled with a high number of checks, the recommendation is to add extra emblems and reduce the Required Emblems Percent
    """
    display_name = "Extra Emblems"
    range_start = 0
    range_end = 900
    default = 0


class RequiredEmblemsPercent(Range):
    """
    What percent of the total emblems should be required to unlock the Final Goal? (rounded down)
    This also affects level gates (if enabled)
    This can be 0 which makes all level gates and the final boss have no emblem cost
    If Sanity options are enabled with a high number of checks, the recommendation is to add extra emblems and reduce the Required Emblems Percent
    """

    display_name = "Required Emblems Percent"
    range_start = 0
    range_end = 100
    default = 60

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

class DontLoseBonusKey(Toggle):
    """
    Keep the Bonus Key for the rest of the level once you collect it
    """
    display_name = "Dont lose the Bonus Key when dying or getting hit"

class NumberOfLevelGates(Range):
    """
    The number emblem-locked gates which lock sets of levels. This is capped to 3 for only 1 story.
    """
    display_name = "Number of Level Gates"
    range_start = 0
    range_end = 7
    default = 3

class EnableMissionA(DefaultOnToggle):
    """
    Should the First Mission for each Level be enabled?
    Dark and Rose Sanity only affect Mission B
    """
    display_name = "Enable Mission A"

class EnableMissionB(DefaultOnToggle):
    """
    Should the Second Mission for each Level be enabled?
    This will include any Sanity Options chosen as well
    """
    display_name = "Enable Mission B"

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

class DarkSanity(Toggle):
    """
    Dark Mission B Enemy (100 enemies objective) Sanity
    """
    display_name = "Dark Sanity Enabled"

class DarkSanityEnemyInterval(Choice):
    """
    How many enemies are needed for a sanity check?
    Requires Mission B to be enabled
    1 results in 1400 checks
    20 results in 70 checks
    """
    display_name = "Dark Sanity Enemy Interval"
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 10

class RoseStory(Toggle):
    """
    Should Rose Story Missions be enabled?
    """
    display_name = "Rose Story Enabled"

class RoseSanity(Toggle):
    """
    Rose Mission B Ring Sanity
    """
    display_name = "Rose Sanity Enabled"

class RoseSanityRingInterval(Choice):
    """
    How many rings are needed for a sanity check?
    Requires Mission B to be enabled
    1 results in 2800 checks
    20 results in 140 checks
    """
    display_name = "Rose Sanity Ring Interval"
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 10

class ChaotixStory(Toggle):
    """
    Should Chaotix Story Missions be enabled?
    """
    display_name = "Chaotix Story Enabled"

class ChaotixSanity(Toggle):
    """
    Chaotix Sanity
    """
    display_name = "Chaotix Sanity Enabled"

class ChaotixSanityRingInterval(Choice):
    """
    How many rings are needed for a sanity check for Casino Park?
    Mission A is 200 Rings and Mission B is 500.
    1 results in 1189 checks (if both missions are enabled)
    20 results in 524 checks (if both missions are enabled)
    """
    display_name = "Chaotix Sanity Ring Interval"
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 10

class RingLink(Toggle):
    """
    Ring Link
    """
    display_name = "Ring Link Enabled"

class RingLinkOverlord(Toggle):
    """
    Should Ring Link be enabled on Metal Overlord?
    This requires Ring Link to be enabled to have any effect
    """
    display_name = "Ring Link on Metal Overlord"

class ModernRingLoss(Toggle):
    """
    Only lose up to 20 Rings when hit instead of all
    """
    display_name = "Modern Ring Loss Enabled"

class TrapFill(Range):
    """
    Determines the percentage of the junk fill which is filled with traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class StealthTrapWeight(Range):
    """
    Determines the weight (not percent) for Stealth Trap.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Stealth Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class FreezeTrapWeight(Range):
    """
    Determines the weight (not percent) for Freeze Trap.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Freeze Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class NoSwapTrapWeight(Range):
    """
    Determines the weight (not percent) for No Swap Trap.
    Traps must be enabled for this to have any effect.
    """
    display_name = "No Swap Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class RingTrapWeight(Range):
    """
    Determines the weight (not percent) for Ring Trap.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Ring Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class CharmyTrapWeight(Range):
    """
    Determines the weight (not percent) for Charmy Trap.
    Traps must be enabled for this to have any effect.
    """
    display_name = "Charmy Trap Weight"
    range_start = 0
    range_end = 100
    default = 50


sonic_heroes_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        GoalUnlockCondition,
        SkipMetalMadness,
        ExtraEmblems,
        RequiredEmblemsPercent,
        RequiredRank,
        DontLoseBonusKey
    ]),
    OptionGroup("Level Gates", [
        NumberOfLevelGates,
    ]),
    OptionGroup("Story Options", [
        EnableMissionA,
        EnableMissionB,
        SonicStory,
        DarkStory,
        RoseStory,
        ChaotixStory,
    ]),
    OptionGroup("Sanity", [
        DarkSanity,
        DarkSanityEnemyInterval,
        RoseSanity,
        RoseSanityRingInterval,
        ChaotixSanity,
        ChaotixSanityRingInterval
    ]),
    OptionGroup("Ring Options", [
        RingLink,
        RingLinkOverlord,
        ModernRingLoss,
    ]),
    OptionGroup("Traps", [
        TrapFill,
        StealthTrapWeight,
        FreezeTrapWeight,
        NoSwapTrapWeight,
        RingTrapWeight,
        CharmyTrapWeight
    ]),
    OptionGroup("DeathLink", [
        DeathLink
    ]),
]



@dataclass
class SonicHeroesOptions(PerGameCommonOptions):
    goal: Goal
    goal_unlock_condition: GoalUnlockCondition
    skip_metal_madness: SkipMetalMadness
    extra_emblems: ExtraEmblems
    required_emblems_percent: RequiredEmblemsPercent
    required_rank: RequiredRank
    dont_lose_bonus_key: DontLoseBonusKey

    number_level_gates: NumberOfLevelGates

    enable_mission_a: EnableMissionA
    enable_mission_b: EnableMissionB
    sonic_story: SonicStory
    dark_story: DarkStory
    dark_sanity: DarkSanity
    dark_sanity_enemy_interval: DarkSanityEnemyInterval
    rose_story: RoseStory
    rose_sanity: RoseSanity
    rose_sanity_ring_interval: RoseSanityRingInterval
    chaotix_story: ChaotixStory
    chaotix_sanity: ChaotixSanity
    chaotix_sanity_ring_interval: ChaotixSanityRingInterval

    ring_link: RingLink
    ring_link_overlord: RingLinkOverlord
    modern_ring_loss: ModernRingLoss

    trap_fill: TrapFill
    stealth_trap_weight: StealthTrapWeight
    freeze_trap_weight: FreezeTrapWeight
    no_swap_trap_weight: NoSwapTrapWeight
    ring_trap_weight: RingTrapWeight
    charmy_trap_weight: CharmyTrapWeight

    death_link: DeathLink
