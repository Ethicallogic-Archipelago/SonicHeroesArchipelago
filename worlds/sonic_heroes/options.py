from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld



from dataclasses import dataclass
from Options import *
from .constants import *


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
    default = 0


class SonicCheckpointSanity(Choice):
    """
    """
    internal_name = "sonic_checkpoint_sanity"
    display_name = "Sonic Checkpoint Sanity"
    option_disabled = 0
    option_Only1SetNormal = 1
    option_OnlySuperHard = 2
    option_SetForEachAct = 3
    default = 0







class SecretLocations(Toggle):
    """

    """
    internal_name = "secret_locations"
    display_name = "Secret/OOB Locations"




sonic_heroes_option_groups = \
    [
    OptionGroup("Stories",
                [
                    SonicStory,
                    SecretLocations,
                ]),

    OptionGroup("Sanity",
                [
                    SonicKeySanity,
                    SonicCheckpointSanity
                ]),
    OptionGroup("DeathLink",
                [
                    DeathLink
                ]),
]


@dataclass
class SonicHeroesOptions(PerGameCommonOptions):

    sonic_story: SonicStory
    sonic_key_sanity: SonicKeySanity
    sonic_checkpoint_sanity: SonicCheckpointSanity
    secret_locations: SecretLocations

    death_link: DeathLink



def check_invalid_options(world: SonicHeroesWorld):

    if world.options.sonic_story.value == 0:
        raise OptionError(f"SONIC STORY MUST BE ENABLED")

    if world.options.sonic_key_sanity.value == 0:
        raise OptionError(f"SONIC KEYSANITY MUST BE ENABLED")

    if world.options.sonic_checkpoint_sanity.value == 0 or world.options.sonic_checkpoint_sanity.value == 2:
        raise OptionError(f"SONIC CHECKPOINTSANITY OPTION ERROR")






