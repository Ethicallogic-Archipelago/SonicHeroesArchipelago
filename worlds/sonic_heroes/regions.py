from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance, MultiWorld
from .locations import *


def create_region(world, name: str, hint: str):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region)

    if name == "Metal Overlord":
        location = Location(world.player, "Victory Location", None, region)
        region.locations.append(location)

    if "Gate Boss between " in name:
        #Region name: f"Gate Boss between Gate {i} and Gate {i + 1}"
        location = Location(world.player, f"Boss Gate {int(name[-1:])}", None, region)
        region.locations.append(location)

    world.multiworld.regions.append(region)


def create_regions(world):

    create_region(world, "Menu", "This is Menu Region")

    #emerald stages
    for i in range(7):
        create_region(world, f"Emerald {i + 1}", f"Region for Emerald {i + 1}")


    #story missions (not bosses or extras)
    for team_index in range(len(world.story_list)):
        for location_number in range(14):

            create_region(world, f"Team {world.story_list[team_index]} Level {location_number + 1}",
             f"Region for team {world.story_list[team_index]} Level {location_number + 1}")

    #gates (including 0) here
    for i in range(world.options.number_level_gates.value + 1):
        create_region(world, f"Gate {i}", f"Gate {i} Region")

    #gate bosses here
    for i in range(world.options.number_level_gates.value):
        create_region(world, f"Gate Boss between Gate {i} and Gate {i + 1}",
        f"Region for Gate Boss {i}")

        #extras/arena fights here
        create_region(world, sonic_heroes_extra_names[world.shuffleable_boss_list[i]], f"Region for {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}")

    #final boss
    create_region(world, "Metal Overlord", "This is Metal Overlord Region")


def connect_entrances(world):

    names: dict[str, int] = {}

    #0 is emblems and emeralds
    #1 is emblems
    #2 is emeralds

    if world.options.goal_unlock_condition.value == 1:
        connect(world, f"Gate {world.options.number_level_gates.value}", "Metal Overlord", lambda state:
        state.has("Emblem", world.player, world.required_emblems),
        rule_to_str=f"Emblems Required: {world.required_emblems}")

    elif world.options.goal_unlock_condition.value == 2:
        connect(world, f"Gate {world.options.number_level_gates.value}", "Metal Overlord", lambda state:
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player),
            rule_to_str=f"All 7 Chaos Emeralds Required")

    elif world.options.goal_unlock_condition.value == 0:
        connect(world, f"Gate {world.options.number_level_gates.value}", "Metal Overlord", lambda state:
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
        connect(world, "Menu", "Gate 0")
        for team in world.story_list:
            for location_number in range(14):
                connect(world, "Gate 0", f"Team {team} Level {location_number + 1}")

        for i in range(7):
            connect(world, "Gate 0", f"Emerald {i + 1}")

        world.gate_level_counts.append(14 * len(world.story_list))

    else:
        level_groups = world.options.number_level_gates + 1
        #levels_per_gate = math.floor((len(world.story_list) * 14) / level_groups)
        #total_levels = 14 * len(world.story_list)
        #extra_levels = total_levels % level_groups

        #for i in range(level_groups):
            #world.gate_level_counts.append(levels_per_gate)
            #if (extra_levels > i):
                #world.gate_level_counts[i] += 1

        level_iterator = 0

        for gate in range(level_groups):
            for level in range(world.gate_level_counts[gate]):
                level_id = world.shuffleable_level_list[level_iterator]
                team = world.story_list[math.floor(level_id / 14)]
                story_level_id = (level_id % 14) + 1
                connect(world, f"Gate {gate}", f"Team {team} Level {story_level_id}")

                if story_level_id in world.emerald_mission_numbers:
                    if int(story_level_id / 2) not in world.placed_emeralds:
                        connect(world, f"Gate {gate}", f"Emerald {int(story_level_id / 2)}")
                        world.placed_emeralds.append(int(story_level_id / 2))

                level_iterator += 1
            if gate == 0:
                connect(world, "Menu", f"Gate {gate}")
            else:
                connect(world, f"Gate {gate - 1}", f"Gate Boss between Gate {gate - 1} and Gate {gate}",
                lambda state, gate_i_= gate: state.has("Emblem", world.player, world.gate_cost * gate_i_),
                rule_to_str=f"Emblems Required: {world.gate_cost * gate}")
                connect(world, f"Gate Boss between Gate {gate - 1} and Gate {gate}", f"{sonic_heroes_extra_names[world.shuffleable_boss_list[gate - 1]]}")

                connect(world, f"Gate Boss between Gate {gate - 1} and Gate {gate}", f"Gate {gate}",
                lambda state, gate_i_=gate: state.has(f"Boss Gate Item {gate_i_}", world.player),
                rule_to_str=f"Boss Gate Item {gate} Required")



def connect(
    world,
    source: str,
    target: str,
    rule = None,
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
    #print(f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n")

    return connection if reach else None

