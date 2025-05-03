from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, OptionGroup, PerGameCommonOptions, DeathLink


class Goal(Choice):
    """
    Determines the goal of the seed

    Metal Overlord: Beat Metal Overlord
    """
    internal_name = "goal"
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
    internal_name = "goal_unlock_condition"
    display_name = "Goal Unlock Condition"
    option_normal = 0
    option_emblems_only = 1
    option_emeralds_only = 2
    default = 0



class EmeraldStageLocationType(Choice):
    """
    Which Location type should the Emeralds be?
    Priority is recommended as it gives a reason to do them
    Excluded requires enough space in the itempool to generate
    """
    internal_name = "emerald_stage_location_type"
    display_name = "Emerald Stage Location Type"
    option_priority = 0
    option_normal = 1
    option_excluded = 2
    default = 0


class SkipMetalMadness(DefaultOnToggle):
    """
    Skips Metal Madness when selecting it from level select and goes directly to Metal Overlord (final boss)
    """
    internal_name = "skip_metal_madness"
    display_name = "Skip Metal Madness"


class EmblemPoolSize(Range):
    """
    How many Emblems should be added to the itempool?
    This is per Mission Act enabled (A and B) and Story
    """
    internal_name = "emblem_pool_size"
    display_name = "Emblem Pool Size"
    range_start = 0
    range_end = 14
    default = 12


class ExtraEmblems(Range):
    """
    How many extra emblems to add to the itempool?
    These allow for easier unlocking of gates as they are NOT used calculate emblem costs
    This is capped at available spots in the location pool
    Very high values can allow for very fast gate and goal unlocks with sanity enabled
    """
    internal_name = "extra_emblems"
    display_name = "Extra Emblems"
    range_start = 0
    range_end = 900
    default = 0


class RequiredEmblemsPercent(Range):
    """
    What percent of the Emblem pool size emblems should be required to unlock the Final Goal? (rounded down)
    This also affects level gates (if enabled)
    This can be 0 which makes all level gates and the final boss have no emblem cost
    """
    internal_name = "required_emblems_percent"
    display_name = "Required Emblems Percent"
    range_start = 0
    range_end = 100
    default = 100

class RequiredRank(Choice):
    """
    Determines what minimum Rank is required to send a check for a mission
    """
    internal_name = "required_rank"
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
    internal_name = "dont_lose_bonus_key"
    display_name = "Dont lose the Bonus Key when dying or getting hit"

class NumberOfLevelGates(Range):
    """
    The number emblem-locked gates which lock sets of levels.
    """
    internal_name = "number_of_level_gates"
    display_name = "Number of Level Gates"
    range_start = 0
    range_end = 7
    default = 3

class SonicStory(Choice):
    """
    Should Sonic Story Missions be enabled?
    """
    internal_name = "sonic_story"
    display_name = "Sonic Story"
    option_disabled = 0
    option_mission_a_only = 1
    option_mission_b_only = 2
    option_both_missions_enabled = 3
    default = 0


class DarkStory(Choice):
    """
    Should Dark Story Missions be enabled?
    Mission B will allow for Dark Enemy Sanity
    """
    internal_name = "dark_story"
    display_name = "Dark Story"
    option_disabled = 0
    option_mission_a_only = 1
    option_mission_b_only = 2
    option_both_missions_enabled = 3
    default = 0

class DarkSanity(Choice):
    """
    How many enemies are needed for a sanity check?
    Requires Mission B to be enabled
    1 results in 1400 checks
    20 results in 70 checks
    """
    internal_name = "dark_sanity"
    display_name = "Dark Sanity"
    option_disabled = 0
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 0

class RoseStory(Choice):
    """
    Should Rose Story Missions be enabled?
    Mission B will allow for Rose Ring Sanity
    """
    internal_name = "rose_story"
    display_name = "Rose Story"
    option_disabled = 0
    option_mission_a_only = 1
    option_mission_b_only = 2
    option_both_missions_enabled = 3
    default = 1

class RoseSanity(Choice):
    """
    How many rings are needed for a sanity check?
    Requires Mission B to be enabled
    Each
    1 results in 2800 checks
    20 results in 140 checks
    """
    internal_name = "rose_sanity"
    display_name = "Rose Sanity"
    option_disabled = 0
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 0

class ChaotixStory(Choice):
    """
    Should Chaotix Story Missions be enabled?
    Either Mission Act, or both, will allow for Chaotix Sanity
    """
    internal_name = "chaotix_story"
    display_name = "Chaotix Story"
    option_disabled = 0
    option_mission_a_only = 1
    option_mission_b_only = 2
    option_both_missions_enabled = 3
    default = 0

class ChaotixSanity(Choice):
    """
    Should Chaotix Sanity be enabled, and if so, how many rings are needed for a check on Casino Park?
    Mission A only Check Count: 223 + 200 / value (if enabled)
    Mission B only Check Count: 266 + 500 / value (if enabled)
    Both Missions Check Count: 489 + 700 / value (if enabled)
    """
    internal_name = "chaotix_sanity"
    display_name = "Chaotix Sanity"
    option_disabled = 0
    option_1 = 1
    option_5 = 5
    option_10 = 10
    option_20 = 20
    default = 0


class SanityExcludedPercent(Range):
    """
    How much percent of sanity checks should be excluded (only have filler/trap items)?
    This helps with large amounts of sanity checks having all of the progressive items in a sync.
    """
    internal_name = "sanity_excluded_percent"
    display_name = "Sanity Excluded Percent"
    range_start = 0
    range_end = 100
    default = 80



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
        EmeraldStageLocationType,
        SkipMetalMadness,
        EmblemPoolSize,
        ExtraEmblems,
        RequiredEmblemsPercent,
        RequiredRank,
        DontLoseBonusKey
    ]),
    OptionGroup("Level Gates", [
        NumberOfLevelGates,
    ]),
    OptionGroup("Story Options", [
        SonicStory,
        DarkStory,
        RoseStory,
        ChaotixStory
    ]),
    OptionGroup("Sanity", [
        DarkSanity,
        RoseSanity,
        ChaotixSanity,
        SanityExcludedPercent
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
    emerald_stage_location_type: EmeraldStageLocationType
    skip_metal_madness: SkipMetalMadness
    emblem_pool_size: EmblemPoolSize
    extra_emblems: ExtraEmblems
    required_emblems_percent: RequiredEmblemsPercent
    required_rank: RequiredRank
    dont_lose_bonus_key: DontLoseBonusKey

    number_level_gates: NumberOfLevelGates

    sonic_story: SonicStory
    dark_story: DarkStory
    dark_sanity: DarkSanity
    rose_story: RoseStory
    rose_sanity: RoseSanity
    chaotix_story: ChaotixStory
    chaotix_sanity: ChaotixSanity
    sanity_excluded_percent: SanityExcludedPercent

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
