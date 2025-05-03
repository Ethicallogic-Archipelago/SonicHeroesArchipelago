from . import SonicHeroesTestBase
from .. import options

class TestNormalEPriorityEmblem14SevenGatesSonicADarkAB(SonicHeroesTestBase):
    options = {
        options.EmblemPoolSize.internal_name: 14,
        options.NumberOfLevelGates.internal_name: 7,
        options.SonicStory.internal_name: options.SonicStory.option_mission_a_only,
        options.DarkStory.internal_name: options.DarkStory.option_both_missions_enabled
    }

class TestNormalEPriorityEmblem14ZeroGatesSonicADarkAB(SonicHeroesTestBase):
    options = {
        options.EmblemPoolSize.internal_name: 14,
        options.NumberOfLevelGates.internal_name: 0,
        options.SonicStory.internal_name: options.SonicStory.option_mission_a_only,
        options.DarkStory.internal_name: options.DarkStory.option_both_missions_enabled
    }