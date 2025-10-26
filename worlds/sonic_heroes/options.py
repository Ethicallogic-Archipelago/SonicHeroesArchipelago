

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld



from dataclasses import dataclass
from Options import *
from .constants import *



class GoalUnlockCondition(Choice):
    """

    """
    internal_name = "goal_unlock_condition"
    display_name = "Goal Unlock Condition"
    option_level_completions = 0
    option_emerald_hunt = 1
    option_level_completions_and_emeralds = 2
    #option_all_abilities = 3
    default = 0


class GoalLevelCompletions(Range):
    """
    How Many Level Completions are needed per Story to unlock Metal Madness?
    This Requires Level Completion Goal Unlock Condition.
    Each Story will require at least this many completed levels.
    Required Rank will also affect this.
    """
    internal_name = "goal_level_completions"
    display_name = "Goal Level Completions"
    range_start = 0
    range_end = 14
    default = 7


class AbilityUnlocks(Choice):
    """

    """
    internal_name = "ability_unlocks"
    display_name = "Ability Unlocks"
    option_all_regions_separate = 0
    option_entire_story = 1
    default = 0



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
    default = 1

class SonicStoryStartingCharacter(Choice):
    """
    Which Character should be unlocked for Sonic Story from the Start?
    """
    internal_name = "sonic_story_starting_character"
    display_name = "Sonic Story Starting Character"
    option_sonic = 0
    option_tails = 1
    option_knuckles = 2
    default = "random"


class SonicKeySanity(Choice):
    """
    Getting a bonus key sends a check.
    This is separate per team enabled
    Only 1 Set makes it only 1 set of keys to collect (for the team)
    Set For Each Act has one set of keys for each Act enabled (requires both Acts enabled to have both sets)
    """
    internal_name = "sonic_key_sanity"
    display_name = "Sonic Key Sanity"
    option_disabled = 0
    option_Only1Set = 1
    option_SetForEachAct = 2
    default = 1


class SonicCheckpointSanity(Choice):
    """
    """
    internal_name = "sonic_checkpoint_sanity"
    display_name = "Sonic Checkpoint Sanity"
    option_disabled = 0
    option_Only1SetNormal = 1
    option_OnlySuperHard = 2
    option_SetForEachAct = 3
    default = 1


class RemoveCasinoParkVIPTableLaserGate(DefaultOnToggle):
    """

    """
    internal_name = "remove_casino_park_vip_table_laser_gate"
    display_name = "Remove Casino Park VIP Table Laser Gate"





class SecretLocations(Toggle):
    """

    """
    internal_name = "secret_locations"
    display_name = "Secret/OOB Locations"




sonic_heroes_option_groups = \
    [
        OptionGroup("Goal",
            [
                GoalUnlockCondition,
                GoalLevelCompletions,
                AbilityUnlocks,
            ]),


        OptionGroup("Stories",
            [
                SonicStory,
                SonicStoryStartingCharacter,
                SecretLocations,
            ]),

        OptionGroup("Sanity",
            [
                SonicKeySanity,
                SonicCheckpointSanity
            ]),
        OptionGroup("QOL",
            [
                RemoveCasinoParkVIPTableLaserGate,
            ]),
        OptionGroup("DeathLink",
            [
                DeathLink
            ]),
]


@dataclass
class SonicHeroesOptions(PerGameCommonOptions):

    goal_unlock_condition: GoalUnlockCondition
    goal_level_completions: GoalLevelCompletions
    ability_unlocks: AbilityUnlocks

    sonic_story: SonicStory
    sonic_story_starting_character: SonicStoryStartingCharacter
    sonic_key_sanity: SonicKeySanity
    sonic_checkpoint_sanity: SonicCheckpointSanity
    secret_locations: SecretLocations
    remove_casino_park_vip_table_laser_gate: RemoveCasinoParkVIPTableLaserGate

    death_link: DeathLink



def check_invalid_options(world: SonicHeroesWorld):

    if world.options.sonic_story.value == 0:
        if world.fuzzer:
            valid_values = [1, 2, 3]
            world.random.shuffle(valid_values)
            world.options.sonic_story.value = valid_values[0]
            print(f"Sonic Story Set to: {world.options.sonic_story.value}")

        else:
            raise OptionError(f"SONIC STORY MUST BE ENABLED")

    if world.options.sonic_key_sanity.value == 0:
        if world.fuzzer:
            valid_values = [1, 2]
            world.random.shuffle(valid_values)
            world.options.sonic_key_sanity.value = valid_values[0]
            print(f"Key Sanity Set to {world.options.sonic_key_sanity.value}")
        else:
            raise OptionError(f"SONIC KEYSANITY MUST BE ENABLED")

    if world.options.sonic_checkpoint_sanity.value == 0 or world.options.sonic_checkpoint_sanity.value == 2:
        if world.fuzzer:
            valid_values = [1, 3]
            world.random.shuffle(valid_values)
            world.options.sonic_checkpoint_sanity.value = valid_values[0]
            print(f"Checkpoint Sanity Set to {world.options.sonic_checkpoint_sanity.value}")
        else:
            raise OptionError(f"SONIC CHECKPOINTSANITY OPTION ERROR")


    if world.options.secret_locations.value:
        raise OptionError(f"SECRET LOCATIONS MUST BE DISABLED")






