import typing
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

    item_name_to_id: ClassVar[Dict[str, int]] = item_name_to_id
    location_name_to_id: ClassVar[Dict[str, int]] = location_name_to_id

    topology_present = True


    def __init__(self, multiworld, player):

        self.disabled_locations: Set[str] = set() #currently not used

        self.default_emblem_pool_size: int = 25 #for only one story

        self.gate_emblem_costs = []

        self.shuffleable_level_list: List[int] = []
        self.shuffleable_boss_list: List[int] = []

        self.story_list: List[str] = []

        #self.emblem_cost_victory: int = 0
        self.required_emblems: int = 0

        self.gate_cost: int = 0

        #locations for regions here
        self.goal = []
        self.gate_locs = []
        self.gate_boss_locs = []
        self.emerald_locs = emerald_locs

        self.team_locs = []
        self.boss_locs = []


        self.number_of_levels_in_gate = []

        self.emerald_mission_numbers = [2, 4, 6, 8, 10, 12, 14]


        super().__init__(multiworld, player)


    def generate_early(self) -> None:

        self.goal.append(goal_loc[0])

        if (self.options.sonic_story.value):

            self.story_list.append("Sonic")
            self.team_locs.append(sonic_mission_locs)
            self.boss_locs.append(sonic_boss_locs)


        if (self.options.dark_story.value):

            self.story_list.append("Dark")
            self.team_locs.append(dark_mission_locs)
            self.boss_locs.append(dark_boss_locs)


        if (self.options.rose_story.value):

            self.story_list.append("Rose")
            self.team_locs.append(rose_mission_locs)
            self.boss_locs.append(rose_boss_locs)


        if (self.options.chaotix_story.value):

            self.story_list.append("Chaotix")
            self.team_locs.append(chaotix_mission_locs)
            self.boss_locs.append(chaotix_boss_locs)


        if (len(self.story_list) < 1 or len(self.story_list) > 4):
            raise OptionError("[ERROR] Number of stories enabled is invalid.")

        #self.total_emblems = self.default_emblem_pool_size * len(self.story_list)
        self.required_emblems = math.floor(self.default_emblem_pool_size * len(self.story_list) *
        self.options.required_emblems_percent.value / 100)


        if self.options.number_level_gates.value > 3 and len(self.story_list) == 1:
            self.options.number_level_gates.value = 3


        if self.options.number_level_gates.value == 0:
            self.gate_cost = 0

        else:
            self.gate_cost = math.floor(self.required_emblems / (self.options.number_level_gates.value + 1))
            if self.gate_cost < 1:
                self.gate_cost = 1


        for i in range(self.options.number_level_gates.value):
            self.gate_emblem_costs.append((i + 1) * self.gate_cost)

        self.gate_emblem_costs.append(self.required_emblems)


        for i in range(len(self.story_list)):
            for ii in range(18):
                self.shuffleable_level_list.append(18 * i + ii)

            for ii in range(3):
                self.shuffleable_boss_list.append(3 * i + ii)

        #print("Shuffleable Level List here: " + str(self.shuffleable_level_list))

        self.random.shuffle(self.shuffleable_level_list)
        self.random.shuffle(self.shuffleable_boss_list)

        #print("Shuffleable Level List here: " + str(self.shuffleable_level_list))
        #print("Shuffleable Boss List here: " + str(self.shuffleable_boss_list))

        for i in range(self.options.number_level_gates.value):

            self.gate_boss_locs.append(self.boss_locs[math.floor((self.shuffleable_boss_list[i]) / 3)]
            [((self.shuffleable_boss_list[i]) % 3)])
            #format is 1 2 3 for first story bosses, 4 5 6 etc
        #print("self.gate_boss_locs here: " + str(self.gate_boss_locs))



    def create_regions(self):

        create_regions(self)

        victory_item = SonicHeroesItem("Victory", ItemClassification.progression, None, self.player)

        self.get_location("Metal Madness").place_locked_item(victory_item)

        #boss_gate_locked_items = []

        for i in range(self.options.number_level_gates.value):

            boss_gate_item = SonicHeroesItem(f"Boss Gate Item {i + 1}", ItemClassification.progression,
            0x93930009 + i + 1, self.player)


            #print("gate_boss_locs index is: " + str(self.gate_boss_locs[i][0]))
            for k in self.gate_boss_locs[i][0].keys():
                self.get_location(k).place_locked_item(boss_gate_item)
                #print("Creating Boss Item here: " + str(boss_gate_item))
                #print("Placing it here: " + str(self.get_location(k)))

        connect_entrances(self)



    def create_item(self, item: str) -> SonicHeroesItem:

        if item in junk_weights.keys():
            return SonicHeroesItem(item, ItemClassification.filler, item_name_to_id[item], self.player)


        return SonicHeroesItem(item, ItemClassification.progression, item_name_to_id[item], self.player)


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


        for i in range(len(self.gate_locs)):
            spoiler_handle.write(f"\nHere is gate_locs index {i} \n")
            for loc in self.gate_locs[i]:
                spoiler_handle.write(f"{loc}\n")



        for i in range(len(self.number_of_levels_in_gate)):
            spoiler_handle.write(f"\nThis is the numbers of levels in Gate {i}: {self.number_of_levels_in_gate[i]}\n")



        spoiler_handle.write(f"\nThis is the number of required emblems for the final boss: {self.required_emblems}\n")






    def fill_slot_data(self) -> id:
        return {
            "ModVersion": 100,

            "OptionsDict": self.options.as_dict(*sonic_heroes_option_names_list),
            #"Options": (attr.name for attr in dataclasses.fields(SonicHeroesOptions)
            #            if attr not in dataclasses.fields(PerGameCommonOptions)),

            #"Goal": self.options.goal.value,
            #"Goal Unlock Condition": self.options.goal_unlock_condition.value,
            #"Required Emblems Percent": self.options.required_emblems_percent.value,
            #"Number of Level Gates": self.options.number_level_gates.value,
            #"Sonic Story": self.options.sonic_story.value,
            #"Dark Story": self.options.dark_story.value,
            #"Rose Story": self.options.rose_story.value,
            #"Chaotix Story": self.options.chaotix_story.value,
            #"Emblem Pool Size": self.default_emblem_pool_size,
            "Gate Emblem Costs": self.gate_emblem_costs,
            "Required Emblems for Goal": self.required_emblems,
            #"Story List": self.story_list,
            "Shuffleable Levels": self.shuffleable_level_list,
            "Shuffleable Bosses": self.shuffleable_boss_list,
            "Number of Levels per Gate": self.number_of_levels_in_gate,
            #"Gate Locs": self.gate_locs,
            #"Gate Boss Locs":self.gate_boss_locs,
        }
