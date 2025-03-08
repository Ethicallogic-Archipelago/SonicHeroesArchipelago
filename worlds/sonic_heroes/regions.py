from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance
from .locations import *


def create_region(world, name: str, locations: List[Dict[str, int]], hint: Optional[str] = None):
    temp_string = ""
    ret = Region(name, world.player, world.multiworld, hint)
    for location in locations:
        for k, v in location.items():
            if k in world.disabled_locations: #currently not used
                continue
            temp_string += f"{k} "

            loc = SonicHeroesLocation(world.player, k, v, ret)
            ret.locations.append(loc)

    world.multiworld.regions.append(ret)

    #world.spoiler_string += f"\nCreating Region with name: {name} and locations: {temp_string}\n"



def get_extra_or_boss_locs(world, id: int) -> ExtraTuple[str, Dict[str, int]]:
    temp_string = ""
    temp_dict = {}

    if id == 0:
        temp_list = egg_hawk_locs
        temp_string = "Egg Hawk"

    elif id == 1:
        temp_list = team_fight_1_locs
        temp_string = "Team Fight 1"

    elif id == 2:
        temp_list = robot_carnival_locs
        temp_string = "Robot Carnival"

    elif id == 3:
        temp_list = egg_albatross_locs
        temp_string = "Egg Albatross"

    elif id == 4:
        temp_list = team_fight_2_locs
        temp_string = "Team Fight 2"

    elif id == 5:
        temp_list = robot_storm_locs
        temp_string = "Robot Storm"

    elif id == 6:
        temp_list = egg_emperor_locs
        temp_string = "Egg Emperor"

    else:
        temp_list = []

    for story in world.story_list:
        if story == "Sonic":
            temp_dict |= temp_list[0][0]

        if story == "Dark":
            temp_dict |= temp_list[1][0]

        if story == "Rose":
            temp_dict |= temp_list[2][0]

        if story == "Chaotix":
            temp_dict |= temp_list[3][0]


    return ExtraTuple(temp_string, temp_dict)





def create_regions(world):

    create_region(world, "Menu", [], "This is Menu Region")

    #emerald stages
    for i in range(7):
        create_region(world, f"Emerald {i + 1}", world.emerald_locs[i], f"Region for Emerald {i + 1}")



    #story missions (not bosses or extras)
    for team_index in range(len(world.story_list)):
        for location_number in range(14):

            create_region(world, f"Team {world.story_list[team_index]} Level {location_number + 1}",
             world.team_locs[team_index][location_number],
             f"Region for team {world.story_list[team_index]} Level {location_number + 1}")

    #gates (including 0) here
    for i in range(world.options.number_level_gates.value + 1):
        create_region(world, f"Gate {i}", [], f"Gate {i} Region")

    #gate bosses here
    for i in range(world.options.number_level_gates.value):
        create_region(world, f"Gate Boss between Gate {i} and Gate {i + 1}",
        boss_gate_locs[i], f"Region for Gate Boss {i}")

        #extras/arena fights here
        extra_tuple = get_extra_or_boss_locs(world, world.shuffleable_boss_list[i])

        create_region(world, f"{extra_tuple.name}", [extra_tuple.loc_dict,], f"Region for {extra_tuple.name}")

    #final boss
    create_region(world, "Metal Overlord", world.goal[0], "This is Metal Overlord Region")


def connect_entrances(world):

    names: Dict[str, int] = {}

    #0 is emblems and emeralds
    #1 is emblems
    #2 is emeralds

    for i in range(world.options.number_level_gates.value + 1):
            world.gate_locs.append([])

    if (world.options.goal_unlock_condition.value == 1):
        connect(world, "Menu", "Metal Overlord", lambda state:
        state.has("Emblem", world.player, world.required_emblems),
        rule_to_str=f"Emblems Required: {world.required_emblems}")

    elif (world.options.goal_unlock_condition.value == 2):
        connect(world, "Menu", "Metal Overlord", lambda state:
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player),
            rule_to_str=f"All 7 Chaos Emeralds Required")

    elif (world.options.goal_unlock_condition.value == 0):
        connect(world, "Menu", "Metal Overlord", lambda state:
            state.has("Emblem", world.player, world.required_emblems) and
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player),
            rule_to_str=f"Emblems Required: {world.required_emblems} AND all 7 Chaos Emeralds")

    #here is levels
    if world.options.number_level_gates.value == 0:
        for team in world.story_list:
            for location_number in range(14):
                connect(world, "Gate 0", f"Team {team} Level {location_number + 1}")
                if (location_number + 1 in world.emerald_mission_numbers):
                    connect(world, "Gate 0", f"Emerald {location_number + 1}")
    else:
        level_groups = world.options.number_level_gates + 1
        levels_per_gate = math.floor((len(world.story_list) * 14) / level_groups)
        total_levels = 14 * len(world.story_list)
        extra_levels = total_levels % level_groups

        #print(f'levels per gate: {levels_per_gate}')
        #print(f'total_levels: {total_levels}')
        #print(f'extra_levels: {extra_levels}')

        for i in range(level_groups):
            world.number_of_levels_in_gate.append(levels_per_gate)
            if (extra_levels > i):
                world.number_of_levels_in_gate[i] += 1

        level_iterator = 0

        for gate in range(level_groups):
            for level in range(world.number_of_levels_in_gate[gate]):
                level_id = world.shuffleable_level_list[level_iterator]
                team = world.story_list[math.floor(level_id / 14)]
                story_level_id = (level_id % 14) + 1
                connect(world, f"Gate {gate}", f"Team {team} Level {story_level_id}")
                if (story_level_id in world.emerald_mission_numbers):
                    connect(world, f"Gate {gate}", f"Emerald {int(story_level_id / 2)}")
                level_iterator += 1
            if gate == 0:
                connect(world, "Menu", f"Gate {gate}")
            else:
                connect(world, f"Gate {gate - 1}", f"Gate Boss between Gate {gate - 1} and Gate {gate}",
                lambda state, gate_i_= gate: state.has("Emblem", world.player, world.gate_cost * gate_i_),
                rule_to_str=f"Emblems Required: {world.gate_cost * gate}")
                extra_tuple = get_extra_or_boss_locs(world, world.shuffleable_boss_list[gate - 1])
                connect(world, f"Gate Boss between Gate {gate - 1} and Gate {gate}", f"{extra_tuple.name}")
                connect(world, f"Gate {gate - 1}", f"Gate {gate}",
                lambda state, gate_i_=gate: state.has(f"Boss Gate Item {gate_i_}", world.player),
                rule_to_str=f"Boss Gate Item {gate} Required")




def connect(
    world,
    source: str,
    target: str,
    rule: Optional[Callable] = None,
    reach: Optional[bool] = False,
    rule_to_str: Optional[str] = None,
) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, target, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    world.spoiler_string += f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n"

    return connection if reach else None

