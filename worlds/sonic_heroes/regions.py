from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance
from .locations import *



def create_region(world: "SonicHeroesWorld", name: str, locations: List[Dict[str, int]], hint: Optional[str] = None):
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

    world.spoiler_string += f"\nCreating Region with name: {name} and locations: {temp_string}\n"



def get_extra_or_boss_locs(world: "SonicHeroesWorld", id: int) -> ExtraTuple[str, Dict[str, int]]:
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





def create_regions(world: "SonicHeroesWorld"):

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
    create_region(world, "Metal Madness", world.goal[0], "This is Metal Madness Region")


def connect_entrances(world: "SonicHeroesWorld"):

    names: Dict[str, int] = {}

    #0 is emblems and emeralds
    #1 is emblems
    #2 is emeralds

    for i in range(world.options.number_level_gates.value + 1):
            world.gate_locs.append([])

    if (world.options.goal_unlock_condition.value == 1):

        connect(world, names, "Menu", "Metal Madness", lambda state:
        state.has("Emblem", world.player, world.required_emblems))

    elif (world.options.goal_unlock_condition.value == 2):

        connect(world, names, "Menu", "Metal Madness", lambda state:
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player))

    elif (world.options.goal_unlock_condition.value == 0):


        connect(world, names, "Menu", "Metal Madness", lambda state:
            state.has("Emblem", world.player, world.required_emblems) and
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player))


    #here is levels
    if world.options.number_level_gates.value == 0:

        for team in world.story_list:
            for location_number in range(14):
                connect(world, names, "Gate 0", f"Team {team} Level {location_number + 1}")

                if (location_number + 1 in world.emerald_mission_numbers):
                    connect(world, names, "Gate 0", f"Emerald {location_number + 1}")

    else:

        number_of_missions_per_gate = math.floor((len(world.story_list) * 14) /
        (world.options.number_level_gates.value + 1))

        total_missions = 14 * len(world.story_list)

        extra_missions = total_missions % number_of_missions_per_gate


        for i in range(world.options.number_level_gates + 1):

            world.number_of_levels_in_gate.append(number_of_missions_per_gate)

            if (extra_missions > i):
                world.number_of_levels_in_gate[i] += 1


        placed_missions = 0

        for gate_i in range(world.options.number_level_gates.value + 1):

            for mission_ii in range(number_of_missions_per_gate):

                x = world.shuffleable_level_list[placed_missions]

                #gate 0
                connect(world, names, f"Gate {gate_i}",
                f"Team {world.story_list[math.floor(x / 14)]} Level {(x % 14) + 1}")

                placed_missions += 1

                if ((x % 14) + 1 in world.emerald_mission_numbers):
                    connect(world, names, f"Gate {gate_i}", f"Emerald {int(((x % 14) + 1) / 2)}")

            if extra_missions > 0:

                x = world.shuffleable_level_list[placed_missions]

                connect(world, names, f"Gate {gate_i}", f"Team {world.story_list[math.floor(x / 14)]} Level {(x % 14) + 1}")

                placed_missions += 1

                extra_missions -= 1

                if ((x % 14) + 1 in world.emerald_mission_numbers):
                    connect(world, names, f"Gate {gate_i}", f"Emerald {int(((x % 14) + 1) / 2)}")

            if gate_i == 0:
                connect(world, names, "Menu", f"Gate {gate_i}")

            else:

                #have to lambda capture here
                connect(world, names, f"Gate {gate_i - 1}", f"Gate Boss between Gate {gate_i - 1} and Gate {gate_i}",
                lambda state, gate_i_= gate_i: state.has("Emblem", world.player, world.gate_cost * gate_i_))


                extra_tuple = get_extra_or_boss_locs(world, world.shuffleable_boss_list[gate_i - 1])

                connect(world, names, f"Gate Boss between Gate {gate_i - 1} and Gate {gate_i}", f"{extra_tuple.name}")


                connect(world, names, "Menu", f"Gate {gate_i}",
                lambda state, gate_i_=gate_i: state.has(f"Boss Gate Item {gate_i_}", world.player))




def connect(
    world: "SonicHeroesWorld",
    used_names: Dict[str, int],
    source: str,
    target: str,
    rule: Optional[Callable] = None,
    reach: Optional[bool] = False,
) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (" " * used_names[target])

    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    world.spoiler_string += f"\nConnection Region {source} to Region {target}\n"


    return connection if reach else None

