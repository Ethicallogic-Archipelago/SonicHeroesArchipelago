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

    goal_rule = lambda state: (state.has(PLAYABLESONIC, world.player, 1) and state.has(PLAYABLETAILS, world.player, 1) and state.has(PLAYABLEKNUCKLES, world.player, 1) and state.has(char_levelup_to_item_name[SONIC][SPEED], world.player, 3) and  state.has(char_levelup_to_item_name[SONIC][FLYING], world.player, 3) and state.has(char_levelup_to_item_name[SONIC][POWER], world.player, 3) and state.has(progressive_ability_item_names[SONIC][OCEANREGION][SPEED], world.player, 4) and state.has(progressive_ability_item_names[SONIC][OCEANREGION][FLYING], world.player, 2) and state.has(progressive_ability_item_names[SONIC][OCEANREGION][POWER], world.player, 3) and state.has(progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], world.player, 4) and state.has(progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], world.player, 2) and state.has(progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], world.player, 3) and state.has(progressive_ability_item_names[SONIC][CASINOREGION][SPEED], world.player, 4) and state.has(progressive_ability_item_names[SONIC][CASINOREGION][FLYING], world.player, 2) and state.has(progressive_ability_item_names[SONIC][CASINOREGION][POWER], world.player, 3) and state.has(progressive_ability_item_names[SONIC][TRAINREGION][SPEED], world.player, 4) and state.has(progressive_ability_item_names[SONIC][TRAINREGION][FLYING], world.player, 2) and state.has(progressive_ability_item_names[SONIC][TRAINREGION][POWER], world.player, 3))


    connect(world, f"{MENU} -> {SEASIDEHILL} {SONIC} Start", MENU, f"{SEASIDEHILL} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {OCEANPALACE} {SONIC} Start", MENU, f"{OCEANPALACE} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {GRANDMETROPOLIS} {SONIC} Start", MENU, f"{GRANDMETROPOLIS} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {POWERPLANT} {SONIC} Start", MENU, f"{POWERPLANT} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {CASINOPARK} {SONIC} Start", MENU, f"{CASINOPARK} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {BINGOHIGHWAY} {SONIC} Start", MENU, f"{BINGOHIGHWAY} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {RAILCANYON} {SONIC} Start", MENU, f"{RAILCANYON} {SONIC} Start", None, rule_to_str="None")
    connect(world, f"{MENU} -> {BULLETSTATION} {SONIC} Start", MENU, f"{BULLETSTATION} {SONIC} Start", None, rule_to_str="None")


    connect(world, f"Goal Connection", MENU, METALOVERLORD, goal_rule, rule_to_str=f"Goal Rule")

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

    world.spoiler_string += f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n"
    #print(f"\nConnecting Region {source} to Region {target} with rule: {rule_to_str}\n")

    return connection if reach else None






