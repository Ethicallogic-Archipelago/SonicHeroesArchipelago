from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld

import csv

from . import Connections, Locations, Regions
from ..constants import *


def get_full_location_list() -> list[LocationCSVData]:
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # noqa

    full_location_list = []

    with files(Locations).joinpath(f"{LOCATIONS}.csv").open() as csv_file:
        reader = csv.DictReader(csv_file)
        for x in reader:
            #full_location_list[f"{x[LEVEL]} {x[TEAM]} {ACT} {x[ACT]} {x[NAME]}".replace(f"{ACT} 0 ", "")] = x[CODE]
            loc = LocationCSVData(x[NAME], int(x[CODE], 16), x[TEAM], x[LEVEL], int(x[ACT]), x[REGION], x[RULE], x[LOCATIONTYPE], x[HINTINFO], x[NOTES])
            full_location_list.append(loc)

    return full_location_list



def import_location_csv(world: SonicHeroesWorld, team: str):
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # noqa

    for region in world.region_list:
        #print(region)
        pass

    with files(Locations).joinpath(f"{LOCATIONS}.csv").open() as csv_file:
        reader = csv.DictReader(csv_file)
        for x in reader:
            loc = LocationCSVData(x[NAME], int(x[CODE], 16), x[TEAM], x[LEVEL], int(x[ACT]), x[REGION], x[RULE], x[LOCATIONTYPE], x[HINTINFO], x[NOTES])
            #world.loc_id_to_loc[loc.code] = loc
            if is_loc_in_world(world, team, loc):
                #print(f"Adding Location {loc.name} to Region to Location[{loc.region}]")
                world.region_to_location[loc.region].append(loc)

    if world.options.secret_locations:
        for level in world.allowed_levels:
            if is_there_a_secret_csv_file(team, level, LOCATIONS):
                file_name = get_csv_file_name(team, level, LOCATIONS, True)

                with files(Locations).joinpath(f"{file_name}.csv").open() as csv_file:
                    reader = csv.DictReader(csv_file)
                    for x in reader:
                        loc = LocationCSVData(x[NAME], int(x[CODE], 16), x[TEAM], x[LEVEL], int(x[ACT]), x[REGION],
                                              x[RULE], x[LOCATIONTYPE], x[HINTINFO], x[NOTES])
                        # world.loc_id_to_loc[loc.code] = loc
                        if is_loc_in_world(world, team, loc):
                            # print(f"Adding Location {loc.name} to Region to Location[{loc.region}]")
                            world.region_to_location[loc.region].append(loc)



def import_region_csv(world: SonicHeroesWorld, team: str):
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # noqa


    for level in world.allowed_levels:
        file_name = get_csv_file_name(team, level, REGIONS, False)
        print(f"File Name here: {file_name}")

    #for level, v in csv_file_names[team].items():
        #file_name = v[REGION]

        with files(Regions).joinpath(f"{file_name}.csv").open() as csv_file:
            reader = csv.DictReader(csv_file)
            for x in reader:

                if TEAM not in x:
                    print(x)


                reg = RegionCSVData(x[TEAM], x[LEVEL], f"{x[LEVEL]} {x[TEAM]} {x[NAME]}", x[OBJCHECKS])
                world.region_list.append(reg)
                world.region_to_location[reg.name] = []

        if world.options.secret_locations:
            if is_there_a_secret_csv_file(team, level, REGIONS):
                file_name = get_csv_file_name(team, level, REGIONS, True)

            #if v[SECRETREGION] is not None:
                #file_name = v[SECRETREGION]
                with files(Regions).joinpath(f"{file_name}.csv").open() as csv_file:
                    reader = csv.DictReader(csv_file)
                    for x in reader:
                        reg = RegionCSVData(x[TEAM], x[LEVEL], f"{x[LEVEL]} {x[TEAM]} {x[NAME]}", x[OBJCHECKS])
                        world.region_list.append(reg)
                        world.region_to_location[reg.name] = []

        #print(f"Finished with File Name: {file_name}")




def import_connection_csv(world: SonicHeroesWorld, team: str):
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # noqa

    id = 0


    for level in world.allowed_levels:
        file_name = get_csv_file_name(team, level, CONNECTIONS, False)
        print(f"File Name here: {file_name}")

    #for level, v in csv_file_names[team].items():
        #file_name = v[CONNECTION]
        #print(f"File Name here: {file_name}")
        with files(Connections).joinpath(f"{file_name}.csv").open() as csv_file:
            reader = csv.DictReader(csv_file)
            for x in reader:
                rule = x[RULE]
                if "" == x[RULE]:
                    rule = "Nothing"

                source = find_index_of_region(world,f"{x[LEVEL]} {x[TEAM]} {x[SOURCE]}")
                target = find_index_of_region(world,f"{x[LEVEL]} {x[TEAM]} {x[TARGET]}")

                if source < 0:
                    raise ValueError("Source Out of Bounds")
                if target < 0:
                    raise ValueError("Target Out of Bounds")

                conn = ConnectionCSVData(f"{source} > {target} with Rule: {rule}", x[TEAM], x[LEVEL], f"{x[LEVEL]} {x[TEAM]} {x[SOURCE]}", f"{x[LEVEL]} {x[TEAM]} {x[TARGET]}", x[RULE])
                id += 1
                world.connection_list.append(conn)


def is_loc_in_world(world: SonicHeroesWorld, team: str, loc: LocationCSVData) -> bool:
    codes: list[int] = \
        [
            #0x9393230E,
            #0x939300a4,
            #0x939300a6,
            #0x93931706,
            #0x93931708,
            #0x93931806,
            #0x93931808,
            #0x93931906,
            #0x93931908,
            #0x93932009,
            #0x9393200D,
            #0x93932109,
            #0x9393210D,
            #0x93932209,
            #0x9393220D,
        ]

    if loc.name == METALOVERLORD:
        for locCsvData in world.region_to_location[loc.region]:
            if locCsvData.name == METALOVERLORD:
                return False
        print(f"Adding {loc.name} to {loc.region}")
        return True


    if loc.code in codes:
        print(f"Loc {loc.name} ID {hex(loc.code)} has a region {loc.region}")

    if loc.team != team and loc.team != "Any":
        if loc.code in codes:
            print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not matching team")
        return False

    if loc.loc_type == "Secret" and not world.options.secret_locations:
        if loc.code in codes:
            print(f"Loc {loc.name} ID {hex(loc.code)} failed because of secret type")
        return False

    if loc.loc_type == "Normal":
        if team == "Sonic":
            if loc.level not in world.allowed_levels:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not in allowed levels Normal")
                return False

            if world.options.sonic_story == 1 and loc.act != 1 and "Metal Overlord" not in loc.name:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 1 when Act 1 only")
                return False

            elif world.options.sonic_story == 2 and loc.act != 2 and "Metal Overlord" not in loc.name:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 2 when Act 2 only")
                return False


    if loc.loc_type == "Boss":
        return False
    if loc.loc_type == "Emerald":
        return False
    if loc.loc_type == "ObjSanity":
        return False

    if loc.loc_type == "CheckpointSanity":
        if team == "Sonic":
            if loc.level not in world.allowed_levels:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not in allowed levels Checkpoint Sanity")
                return False
            if world.options.sonic_checkpoint_sanity == 0:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of Checkpoint Sanity Disabled")
                return False

            elif world.options.sonic_checkpoint_sanity == 1 and loc.act != 0:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 0 with Checkpoint Sanity only 1 Set")
                return False

            elif world.options.sonic_checkpoint_sanity == 2:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of Checkpoint Sanity Super Hard only")
                return False

            elif world.options.sonic_checkpoint_sanity == 3:
                if loc.act == 0:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of Act 0 with Checkpoint Sanity set to each Act")
                    return False
                if world.options.sonic_story == 1 and loc.act != 1:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 1 when Act 1 only")
                    return False
                if world.options.sonic_story == 2 and loc.act != 2:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 2 when Act 2 only")
                    return False


    if loc.loc_type == "KeySanity":
        if team == "Sonic":
            if loc.level not in world.allowed_levels:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not in allowed levels Key Sanity")
                return False

            if world.options.sonic_key_sanity == 0:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of Key Sanity Disabled")
                return False

            elif world.options.sonic_key_sanity == 1 and loc.act != 0:
                if loc.code in codes:
                    print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 0 when only 1 Set")
                return False

            elif world.options.sonic_key_sanity == 2:
                if loc.act == 0:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of Act 0 when each Act")
                    return False
                if world.options.sonic_story == 1 and loc.act != 1:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 1 when only Act 1")
                    return False
                if world.options.sonic_story == 2 and loc.act != 2:
                    if loc.code in codes:
                        print(f"Loc {loc.name} ID {hex(loc.code)} failed because of not Act 2 when only Act 2")
                    return False

    return True


def find_index_of_region(world, name):
    index = 0
    for reg in world.region_list:
        if reg.name == name:
            return index
        index += 1
    return -1
