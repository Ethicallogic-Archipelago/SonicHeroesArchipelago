from typing import TextIO

from BaseClasses import *
from worlds.AutoWorld import World, WebWorld
from . import csvdata
from .constants import *
from .csvdata import *
from .items import *
from .logic_mapping_sonic import *
from .options import *
from .regions import *


class SonicHeroesWeb(WebWorld):
    theme = PARTYTIMETHEME
    setup_en = (Tutorial(
        tutorial_name=TUTORIALNAME,
        description=TUTORIALDESC,
        language=TUTORIALLANGUAGE,
        file_name=TUTORIALFILENAME,
        link=TUTORIALLINK,
        authors=TUTORIALAUTHORS
    ))

    tutorials = [setup_en]
    #option_groups = sonic_heroes_option_groups


class SonicHeroesWorld(World):
    game = SONICHEROES
    web = SonicHeroesWeb()
    options_dataclass = SonicHeroesOptions
    options: SonicHeroesOptions
    item_name_to_id: ClassVar[dict[str, int]] = \
    {item.name: item.code for item in itemList}
    location_name_to_id: ClassVar[dict[str, int]] = {loc.name: loc.code for loc in get_full_location_list()}
    #{k: v for k, v in full_location_dict.items()}

    topology_present = True

    #ut_can_gen_without_yaml = False


    def __init__(self, multiworld, player):
        #PUT STUFF HERE
        #self.loc_id_to_loc = {}

        self.level_goal_event_locations = []
        self.region_to_location = {}
        self.region_list = []
        self.connection_list = []
        self.logic_mapping_dict = {}
        self.spoiler_string = ""
        self.extra_items = 0

        self.regular_regions = \
        [
            OCEANREGION,
            HOTPLANTREGION,
            CASINOREGION,
            TRAINREGION,
            BIGPLANTREGION,
            GHOSTREGION,
            SKYREGION,
        ]

        self.enabled_teams = \
        [
            SONIC,
            #DARK,
            #ROSE,
            #CHAOTIX,
            #SUPERHARD,
        ]

        self.allowed_levels = \
        [
            SEASIDEHILL,
            OCEANPALACE,
            GRANDMETROPOLIS,
            POWERPLANT,
            CASINOPARK,
            BINGOHIGHWAY,
            RAILCANYON,
            BULLETSTATION,
            FROGFOREST,
            LOSTJUNGLE,
            HANGCASTLE,
            MYSTICMANSION,
            EGGFLEET,
            FINALFORTRESS,
            #METALMADNESS
        ]

        self.fuzzer = False
        """
        Enable this for fuzzer testing protections
        """
        self.should_make_puml = True

        super().__init__(multiworld, player)


    def create_item(self, name: str) -> "Item":
        return SonicHeroesItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def generate_early(self) -> None:
        #Check invalid options here
        check_invalid_options(self)


        """
        #UT Stuff Here
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if SONICHEROES not in self.multiworld.re_gen_passthrough:
                return
            passthrough = self.multiworld.re_gen_passthrough[SONICHEROES]
            self.options.goal_unlock_condition = passthrough["goal_unlock_condition"]

        """

        reg = RegionCSVData(ANYTEAM, METALMADNESS, METALMADNESS, 0)
        self.region_list.append(reg)
        self.region_to_location[reg.name] = []

        self.logic_mapping_dict[ANYTEAM] = \
        {
            METALMADNESS:
                {
                    "": lambda state: True,
                },
        }


        if self.options.sonic_story > 0:
            # handle rule mapping here
            self.logic_mapping_dict[SONIC] = self.init_logic_mapping_sonic()

            #import csv data
            self.import_csv_data(SONIC)

            #map regions
            #map_sonic_regions(self)
            #map locations
            #map_sonic_locations(self)
            #map connections
            #map_sonic_connections(self)

        pass




    def create_regions(self) -> None:
        create_regions(self)

        victory_item = SonicHeroesItem(VICTORYITEM, ItemClassification.progression, None, self.player)
        self.get_location(VICTORYLOCATION).place_locked_item(victory_item)

        print(self.level_goal_event_locations)

        for loc_name in self.level_goal_event_locations:
            goal_unlock_item = SonicHeroesItem(GOALUNLOCKITEM, ItemClassification.progression, None, self.player)
            self.get_location(loc_name).place_locked_item(goal_unlock_item)
        pass


    def create_items(self) -> None:
        create_items(self)


        if self.options.sonic_story_starting_character == 0:
            self.multiworld.push_precollected(self.create_item(PLAYABLESONIC))
        if self.options.sonic_story_starting_character == 1:
            self.multiworld.push_precollected(self.create_item(PLAYABLETAILS))
        if self.options.sonic_story_starting_character == 2:
            self.multiworld.push_precollected(self.create_item(PLAYABLEKNUCKLES))
        pass


    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has(VICTORYITEM, self.player)
        pass

    def connect_entrances(self) -> None:
        connect_entrances(self)
        pass

    def generate_basic(self) -> None:
        pass

    def pre_fill(self) -> None:
        pass

    def post_fill(self) -> None:
        pass

    def generate_output(self, output_directory: str) -> None:
        pass

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        pass

    def fill_slot_data(self) -> Mapping[str, Any]:
        from Utils import visualize_regions
        if self.should_make_puml and not self.fuzzer:
            state = self.multiworld.get_all_state(False)
            state.update_reachable_regions(self.player)
            visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True, regions_to_highlight=state.reachable_regions[self.player])
            # !pragma layout smetana
            # put this at top to display PUML (after start UML)
        return \
        {
            "ModVersion": "1.5.0",
            "Goal": 0,
            "GoalUnlockCondition": self.options.goal_unlock_condition.value,
            "GoalLevelCompletions": self.options.goal_level_completions.value,
            "AbilityUnlocks": self.options.ability_unlocks.value,
            "SkipMetalMadness": 1,
            "RequiredRank": 0,
            "DontLoseBonusKey": 1,
            "SonicStory": self.options.sonic_story.value,
            "SuperHardModeSonicAct2": 0,
            "SonicKeySanity": self.options.sonic_key_sanity.value,
            "SonicCheckpointSanity": self.options.sonic_checkpoint_sanity.value,
            "DarkStory": 0,
            "DarkSanity": 0,
            "DarkKeySanity": 0,
            "DarkCheckpointSanity": 0,
            "RoseStory": 0,
            "RoseSanity": 0,
            "RoseKeySanity": 0,
            "RoseCheckpointSanity": 0,
            "ChaotixStory": 0,
            "ChaotixSanity": 0,
            "ChaotixKeySanity": 0,
            "ChaotixCheckpointSanity": 0,
            "RingLink": 1,
            "RingLinkOverlord": 0,
            "ModernRingLoss": 1,
            "DeathLink": 0,

            "RemoveCasinoParkVIPTableLaserGate": self.options.remove_casino_park_vip_table_laser_gate.value,

            "GateEmblemCosts": [1],
            "ShuffledLevels": [f"S{x}" for x in range(2, 16)],
            #"ShuffledLevels": ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11"],
            "ShuffledBosses": ["B23"],
            "GateLevelCounts": [14],
        }

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write(self.spoiler_string)
        pass

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        pass

    def write_spoiler_end(self, spoiler_handle: TextIO) -> None:
        pass




    def import_csv_data(self, team):
        #Regions First
        import_region_csv(self, team)
        #Locations Next
        import_location_csv(self, team)
        #Connections Third
        import_connection_csv(self, team)



    def init_logic_mapping_sonic(self):
        return \
            {
                SEASIDEHILL: create_logic_mapping_dict_seaside_hill_sonic(self),
                OCEANPALACE: create_logic_mapping_dict_ocean_palace_sonic(self),
                GRANDMETROPOLIS: create_logic_mapping_dict_grand_metropolis_sonic(self),
                POWERPLANT: create_logic_mapping_dict_power_plant_sonic(self),
                CASINOPARK: create_logic_mapping_dict_casino_park_sonic(self),
                BINGOHIGHWAY: create_logic_mapping_dict_bingo_highway_sonic(self),
                RAILCANYON: create_logic_mapping_dict_rail_canyon_sonic(self),
                BULLETSTATION: create_logic_mapping_dict_bullet_station_sonic(self),
                FROGFOREST: create_logic_mapping_dict_frog_forest_sonic(self),
                LOSTJUNGLE: create_logic_mapping_dict_lost_jungle_sonic(self),
                HANGCASTLE: create_logic_mapping_dict_hang_castle_sonic(self),
                MYSTICMANSION: create_logic_mapping_dict_mystic_mansion_sonic(self),
                EGGFLEET: create_logic_mapping_dict_egg_fleet_sonic(self),
                FINALFORTRESS: create_logic_mapping_dict_final_fortress_sonic(self),
            }



