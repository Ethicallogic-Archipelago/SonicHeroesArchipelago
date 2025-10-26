from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld

from typing import Optional

from BaseClasses import Entrance, Region
from .constants import *
from .locations import *


class SonicHeroesRegion(Region):
    game = SONICHEROES



def create_region(world: SonicHeroesWorld, name: str, hint: str = ""):
    region = SonicHeroesRegion(name, world.player, world.multiworld)
    create_locations(world, region)

    if name == METALOVERLORD:
        location = SonicHeroesLocation(world.player, VICTORYLOCATION, None, region)
        region.locations.append(location)

    #Seaside Hill (Team) Goal
    name_split = name.split(" ")


    if name_split[-1] == "Goal":
        for team in world.enabled_teams:
            last_word_of_team = team.split(" ")[-1]
            if name_split[-2] == last_word_of_team:
                level_name = name_split[0] + " " + name_split[1]
                if level_name in world.allowed_levels:
                    location = SonicHeroesLocation(world.player, f"{name} Event Location", None, region)
                    region.locations.append(location)
                    world.level_goal_event_locations.append(f"{name} Event Location")

    world.multiworld.regions.append(region)


def create_regions(world: SonicHeroesWorld):
    create_region(world, MENU, MENUREGIONHINT)
    create_region(world, METALOVERLORD, METALMADNESSREGIONHINT)

    create_regions_from_region_list(world)
    pass


def create_regions_from_region_list(world: SonicHeroesWorld):
    #world.region_list = []
    for reg in world.region_list:
        create_region(world, reg.name)
    pass



def connect_entrances(world: SonicHeroesWorld):
    goal_rule_dict = {}

    for team in world.enabled_teams:
        for char_name in team_char_names[team]:
            goal_rule_dict[get_playable_char_item_name(char_name)] = 1
            if world.options.goal_unlock_condition != 1:
                goal_rule_dict[GOALUNLOCKITEM] = world.options.goal_level_completions.value

    if world.options.goal_unlock_condition != 0:
        for emerald in emeralds:
            goal_rule_dict[emerald] = 1

    goal_rule = lambda state: state.has_all_counts(goal_rule_dict, world.player)


    for team in world.enabled_teams:
        for reg in world.allowed_levels:
            connect(world,f"{MENU} -> {reg} {team} Start", MENU, f"{reg} {team} Start", None, rule_to_str="None")

    #connect(world, f"{MENU} -> {SEASIDEHILL} {SONIC} Start", MENU, f"{SEASIDEHILL} {SONIC} Start", None, rule_to_str="None")

    connect(world, f"Goal Connection", MENU, METALMADNESS, goal_rule, rule_to_str=f"Goal Rule")

    connect(world, f"Goal Connection 2", METALMADNESS, METALOVERLORD, goal_rule, rule_to_str=f"Goal Rule")

    connect_entrances_from_connection_list(world)
    pass


def connect_entrances_from_connection_list(world: SonicHeroesWorld):
    for connection in world.connection_list:
        connect(world, connection.name, connection.source, connection.target, world.logic_mapping_dict[connection.team][connection.level][connection.rulestr], rule_to_str=connection.rulestr)



def connect(world: SonicHeroesWorld, name: str, source: str, target: str, rule=None, reach: Optional[bool] = False, rule_to_str: Optional[str] = None,) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    #world.spoiler_string += f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n"
    #print(f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n")

    return connection if reach else None






