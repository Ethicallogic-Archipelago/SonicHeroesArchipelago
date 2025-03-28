import typing
import string
from typing import ClassVar, TextIO
import math
import dataclasses

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .names import *
from .options import *
from .items import *
from .locations import *
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
    options_dataclass = SonicHeroesOptions
    options: SonicHeroesOptions

    item_name_to_id: ClassVar[dict[str, int]] = {item.itemName: item.code for item in itemList}  # noqa: F405
    location_name_to_id: ClassVar[dict[str, int]] = {v.name: k for k, v in location_dict.items()}  # noqa: F405

    topology_present = False


    def __init__(self, multiworld, player):

        self.default_emblem_pool_size: int = 12
        """
        Number of emblems for only one story and only one mission (A or B)
        """
        self.emblem_pool_size = 12
        """
        Number of emblems in the itempool
        """
        self.gate_emblem_costs = []
        """
        List of emblem costs for each gate boss
        """
        self.shuffleable_level_list: list[int] = []
        """
        List of levels that gets shuffled. Used by the client as well.
        """
        self.shuffleable_boss_list: list[int] = []
        """
        List of bosses/extras that gets shuffled. Used by the client as well.
        """
        self.story_list: list[str] = []
        """
        List of enabled Stories in order: ["Sonic", "Dark", "Rose", "Chaotix"]
        """
        self.required_emblems: int = 0
        """
        Number of required emblems for the final boss (can be 0)
        """
        self.gate_cost: int = 0
        """
        Cost for a gate boss (multiplied by the gate)
        As this is rounded down, the final boss can be different
        """
        self.gate_level_counts = []
        """
        Number of levels per gate: [4, 4, 3, 3]
        """
        self.placed_emeralds = []
        """
        List to ensure emeralds are only placed once
        """
        self.emerald_mission_numbers = [2, 4, 6, 8, 10, 12, 14]
        """
        List of Mission Numbers that contain an emerald bonus stage
        """
        self.spoiler_string = ""
        """
        String for printing to the spoiler log
        """

        super().__init__(multiworld, player)


    def generate_early(self) -> None:

        if (self.options.sonic_story.value):
            self.story_list.append(sonic_heroes_story_names[0])

        if (self.options.dark_story.value):
            self.story_list.append(sonic_heroes_story_names[1])

        if (self.options.rose_story.value):
            self.story_list.append(sonic_heroes_story_names[2])

        if (self.options.chaotix_story.value):
            self.story_list.append(sonic_heroes_story_names[3])

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

        #extra emblem math here
        max_allowed_emblems = self.default_emblem_pool_size

        max_allowed_emblems *= len(self.story_list)

        if self.options.goal_unlock_condition.value == 1:
            max_allowed_emblems += 7


        #sanity
        if self.options.enable_mission_a.value:
            if "Chaotix" in self.story_list:
                if self.options.chaotix_sanity.value:
                    #do chaotix sanity
                    max_allowed_emblems += 223 + int(200 / self.options.chaotix_sanity_ring_interval.value)

        if self.options.enable_mission_b.value:
            #dark
            if "Dark" in self.story_list:
                if self.options.dark_sanity.value:
                    max_allowed_emblems += int(1400 / self.options.dark_sanity_enemy_interval.value)

            #Rose
            if "Rose" in self.story_list:
                if self.options.rose_sanity.value:
                    max_allowed_emblems += int(2800 / self.options.rose_sanity_ring_interval.value)

            #Chaotix
            if "Chaotix" in self.story_list:
                if self.options.chaotix_sanity:
                    max_allowed_emblems += 266 + int(500 / self.options.chaotix_sanity_ring_interval.value)


        self.emblem_pool_size = min(self.options.extra_emblems.value + self.default_emblem_pool_size * len(self.story_list), max_allowed_emblems)

        self.spoiler_string += f"THE EMBLEM POOL SIZE IS {self.emblem_pool_size}\n"

        self.required_emblems = math.floor(self.emblem_pool_size * self.options.required_emblems_percent.value / 100)

        if self.options.number_level_gates.value > 3 and len(self.story_list) == 1:
            self.options.number_level_gates.value = 3

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



    def create_item(self, name: str) -> SonicHeroesItem:

        if name in junk_weights.keys():
            return SonicHeroesItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

        return SonicHeroesItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)


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


    def fill_slot_data(self):
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

        #Truncate here to remove unneeded values
        templist = templist[0:self.options.number_level_gates.value]

        templist.append("B23")

        self.shuffleable_boss_list = templist

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




    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]):
        new_hint_data = {}
        for k, v in location_dict.items():
            try:
                location = self.multiworld.get_location(v.name, self.player)
            except KeyError:
                continue

            
            if v.gate == 0:
                new_hint_data[location.address] = f"Gate {v.gate}: Available from Start"

            elif v.gate > 0:
                if v.region in sonic_heroes_extra_names.values():
                    new_hint_data[location.address] = f"Gate {v.gate} Boss: Requires {self.gate_emblem_costs[v.gate]} Emblems and {sonic_heroes_extra_names[self.shuffleable_boss_list[v.gate]]}"
                else:
                    new_hint_data[location.address] = f"Gate {v.gate}: Requires {self.gate_emblem_costs[v.gate - 1]} Emblems and {sonic_heroes_extra_names[self.shuffleable_boss_list[v.gate - 1]]}"

            else:
                self.spoiler_string += f"This check does not exist {location}: {location.address}\n"
                new_hint_data[location.address] = f"Gate {v.gate}: (Does not exist)"

        hint_data[self.player] = new_hint_data