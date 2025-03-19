import typing
import string
from typing import ClassVar, Dict, List, Set, TextIO
import math
import dataclasses

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule

from .options import *
from .items import *
#SonicHeroesItem, item_name_to_id, create_items, junk_weights
from .locations import *
#SonicHeroesLocation, location_name_to_id, sonic_mission_locs, sonic_boss_locs, dark_mission_locs,
#dark_boss_locs, rose_mission_locs, rose_boss_locs, chaotix_mission_locs, chaotix_boss_locs, emerald_locs
from .regions import *


class SonicHeroesWeb(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Sonic Heroes randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["EthicalLogic"]
    )

    tutorials = [setup_en]
    option_groups = sonic_heroes_option_groups


class SonicHeroesWorld(World):

    game: str = "Sonic Heroes"
    web = SonicHeroesWeb()
    options: SonicHeroesOptions
    options_dataclass = SonicHeroesOptions

    item_name_to_id: ClassVar[Dict[str, int]] = {item.itemName: item.code for item in itemList}
    location_name_to_id: ClassVar[Dict[str, int]] = full_location_dict

    topology_present = True


    def __init__(self, multiworld, player):

        self.disabled_locations: Set[str] = set() #currently not used

        self.default_emblem_pool_size: int = 12 #for only one story

        self.gate_emblem_costs = []

        self.shuffleable_level_list: List[int] = []
        self.shuffleable_boss_list: List[int] = []

        self.story_list: List[str] = []

        #self.emblem_cost_victory: int = 0
        self.required_emblems: int = 0

        self.gate_cost: int = 0

        self.gate_level_counts = []

        self.placed_emeralds = []

        self.emerald_mission_numbers = [2, 4, 6, 8, 10, 12, 14]

        self.spoiler_string = ""


        super().__init__(multiworld, player)


    def generate_early(self) -> None:

        if (self.options.sonic_story.value):

            self.story_list.append("Sonic")

        if (self.options.dark_story.value):

            self.story_list.append("Dark")

        if (self.options.rose_story.value):

            self.story_list.append("Rose")

        if (self.options.chaotix_story.value):

            self.story_list.append("Chaotix")


        if (len(self.story_list) < 1 or len(self.story_list) > 4):
            raise OptionError("[ERROR] Number of stories enabled is invalid.")

        if (not(self.options.enable_mission_a.value or self.options.enable_mission_b.value)):
            raise OptionError("[ERROR] Either Mission A or Mission B must be enabled")

        if (self.options.stealth_trap_weight.value == 0 and
        self.options.freeze_trap_weight.value == 0 and
        self.options.no_swap_trap_weight.value == 0 and
        self.options.ring_trap_weight.value == 0 and
        self.options.charmy_trap_weight.value == 0):
            raise OptionError("[ERROR] The Trap Weights must not all be zero")

        if (self.options.enable_mission_a.value and self.options.enable_mission_b.value):
            self.default_emblem_pool_size *= 2

        self.required_emblems = math.floor(self.default_emblem_pool_size * len(self.story_list) *
        self.options.required_emblems_percent.value / 100)


        if self.options.number_level_gates.value > 3 and len(self.story_list) == 1:
            self.options.number_level_gates.value = 3

        if self.options.number_level_gates.value == 0:
            self.gate_cost = 0

        else:
            self.gate_cost = math.floor(self.required_emblems / (self.options.number_level_gates.value + 1))


        for i in range(self.options.number_level_gates.value):
            self.gate_emblem_costs.append((i + 1) * self.gate_cost)

        self.gate_emblem_costs.append(self.required_emblems)


        for i in range(len(self.story_list)):
            for ii in range(14):
                self.shuffleable_level_list.append(14 * i + ii)

        for ii in range(7):
            self.shuffleable_boss_list.append(ii)


        self.random.shuffle(self.shuffleable_level_list)
        self.random.shuffle(self.shuffleable_boss_list)

        generate_locations(self)


    def create_regions(self):

        create_regions(self)

        victory_item = SonicHeroesItem("Victory", ItemClassification.progression, None, self.player)

        self.get_location("Metal Overlord").place_locked_item(victory_item)

        for i in range(self.options.number_level_gates.value):

            boss_gate_item = SonicHeroesItem(f"Boss Gate Item {i + 1}", ItemClassification.progression,
            None, self.player)    #0x93930009 + i + 1

            self.get_location(f"Boss Gate {i + 1}").place_locked_item(boss_gate_item)

        connect_entrances(self)



    def create_item(self, item: str) -> SonicHeroesItem:

        if item in junk_weights.keys():
            return SonicHeroesItem(item, ItemClassification.filler, self.item_name_to_id[item], self.player)


        return SonicHeroesItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)


    def create_items(self):

        create_items(self)


    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


    #only 0.6.0 here
    #def connect_entrances(self):

        #connect_entrances(self)

        #from Utils import visualize_regions
        #visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")



    def write_spoiler_header(self, spoiler_handle: TextIO):

        self.spoiler_string += f"\nGate Costs is: {str(self.gate_emblem_costs)}\n"

        spoiler_handle.write(self.spoiler_string)



    def fill_slot_data(self) -> id:
        #s2-s15 sonic (Inclusive)
        #d2-d15 dark
        #r2-r15 rose
        #c2-c15 chaotix
        #b16-b22 bosses 23 is Madness
        templist = []
        for number in self.shuffleable_level_list:
            story = self.story_list[math.floor(number / 14)]
            templist.append(f'{story[:1].upper()}{(number % 14) + 2}')

        self.shuffleable_level_list = templist

        templist = []
        for number in self.shuffleable_boss_list:
            templist.append(f'B{number + 16}')

        self.shuffleable_boss_list = templist

        self.shuffleable_boss_list[self.options.number_level_gates.value] = "B23"

        #Truncate here to remove unneeded values
        self.shuffleable_boss_list = self.shuffleable_boss_list[0:self.options.number_level_gates.value + 1]

        return {
            "ModVersion": 100,

            "Goal": self.options.goal.value,
            "GoalUnlockCondition": self.options.goal_unlock_condition.value,
            "SkipMetalMadness": self.options.skip_metal_madness.value,
            "RequiredRank": self.options.required_rank.value,
            "DontLoseBonusKey": self.options.dont_lose_bonus_key.value,
            "EnableMissionA": self.options.enable_mission_a.value,
            "EnableMissionB": self.options.enable_mission_b.value,
            "SonicStory": self.options.sonic_story.value,
            "DarkStory": self.options.dark_story.value,
            "DarkSanity": self.options.dark_sanity.value,
            "DarkSanityEnemyInterval": self.options.dark_sanity_enemy_interval.value,
            "RoseStory": self.options.rose_story.value,
            "RoseSanity": self.options.rose_sanity.value,
            "RoseSanityRingInterval": self.options.rose_sanity_ring_interval.value,
            "ChaotixStory": self.options.chaotix_story.value,
            "ChaotixSanity": self.options.chaotix_sanity.value,
            "ChaotixSanityRingInterval": self.options.chaotix_sanity_ring_interval.value,
            "RingLink": self.options.ring_link.value,
            "RingLinkOverlord": self.options.ring_link_overlord.value,
            "ModernRingLoss": self.options.modern_ring_loss.value,
            "DeathLink": self.options.death_link.value,

            "GateEmblemCosts": self.gate_emblem_costs,
            "ShuffledLevels": self.shuffleable_level_list,
            "ShuffledBosses": self.shuffleable_boss_list,
            "GateLevelCounts": self.gate_level_counts,
        }