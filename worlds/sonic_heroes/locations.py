from typing import Dict, NamedTuple
from collections import namedtuple
from BaseClasses import Location, LocationProgressType

from .names import ItemData, sonic_heroes_story_names, sonic_heroes_level_names, sonic_heroes_extra_names, location_id_name_dict

class SonicHeroesLocation(Location):
    game: str = "Sonic Heroes"


def generate_locations(world):

    currentid = 0x939300A0

    for story in range(4):  #for each story
        if sonic_heroes_story_names[story] in world.story_list: #check of story enabled
            for mission in range(14): #for each mission
                if world.options.enable_mission_a.value:  #if mission A enabled
                    world.location_name_to_region[location_id_name_dict[currentid + (2 * mission) + (42 * story)]] = f"Team {sonic_heroes_story_names[story]} Level {mission + 1}"

                if world.options.enable_mission_b.value:  #if mission B enabled
                    world.location_name_to_region[location_id_name_dict[currentid + (2 * mission) + (
                                42 * story) + 1]] = f"Team {sonic_heroes_story_names[story]} Level {mission + 1}"

    #emeralds
    for i in range(7):
        world.location_name_to_region[location_id_name_dict[0x93930148 + i]] = f"Emerald {i + 1}"

    currentid = 0x939300BC
    #extras
    x = 0
    for i in range(world.options.number_level_gates.value):
        for story in world.story_list:
            for k, v in sonic_heroes_story_names.items():
                if v == story:
                    x = k #x = 0-3 for example


            world.spoiler_string += f"Entering Location Dict Entry for extra: {world.shuffleable_boss_list[i]}\nThe Entry is: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]} {story} --- ID: {currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)} --- Region Name: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}\n\n"
            #location_dict[currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)].region = f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}"
            world.location_name_to_region[location_id_name_dict[currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)]] = f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}"

    #Final Boss
    world.location_name_to_region[location_id_name_dict[0x9393165d]] = f"Metal Overlord"

    if world.options.dark_sanity: #dark sanity
        generate_dark_sanity(world)

    if world.options.rose_sanity: #rose sanity
        generate_rose_sanity(world)

    if world.options.chaotix_sanity: #chaotix sanity
        generate_chaotix_sanity(world)


def create_locations(world, region):
    create_locations_from_dict(world, world.location_name_to_region, region)


def create_locations_from_dict(world, loc_dict, region):
    for (loc_name, reg_name) in loc_dict.items():
        if reg_name != region.name:
            continue
        create_location(world, region, loc_name, world.location_name_to_id[loc_name])


def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)

    if "Metal Overlord" in name:
        location.progress_type = LocationProgressType.EXCLUDED

    if "Emerald Stage" in name:
        if world.options.emerald_stage_location_type.value == 0:
            location.progress_type = LocationProgressType.PRIORITY

        elif world.options.emerald_stage_location_type.value == 2:
            location.progress_type = LocationProgressType.EXCLUDED

    region.locations.append(location)






def generate_dark_sanity(world):
    if not world.options.enable_mission_b.value:
        return None #leave if mission B not enabled

    #0x9393014F (starts at 150) - 0x939306C7
    currentid = 0x9393014F

    for mission in range(14):
        for i in range(100, 0, -world.options.dark_sanity_enemy_interval):
            world.location_name_to_region[location_id_name_dict[currentid + i + (mission * 100)]] = f"Team {sonic_heroes_story_names[1]} Level {mission + 1}"


def generate_rose_sanity(world):
    if not world.options.enable_mission_b.value:
        return None #leave if mission B not enabled

    #0x939306C7 (starts at 6C8) - 0x939311B7
    currentid = 0x939306C7

    for mission in range(14):
        for i in range(200, 0, -world.options.rose_sanity_ring_interval):
            world.location_name_to_region[location_id_name_dict[
                currentid + i + (mission * 200)]] = f"Team {sonic_heroes_story_names[2]} Level {mission + 1}"


def generate_chaotix_sanity(world):
    #Chaotix Sanity
    #1189 checks - 524
    #Mission B only is 266 + CP
    #SH - 10, 20
    #OP - 0, 0
    #GM - 85, 85
    #PP - 3, 5
    #CP - 200, 500 - 700, 140, 70, 35
    #BH - 10, 20
    #RC - 0, 0
    #BS - 30, 50
    #FF - 0, 0
    #LJ - 10, 20
    #HC - 10, 10
    #MM - 60, 46
    #EF - 0, 0
    #FF - 5, 10

    #0x939311B7 (starts at 1B8) - 0x93934867
    currentid = 0x939311B7

    #Seaside Hill
    if world.options.enable_mission_a.value:
        for i in range (10):
            world.location_name_to_region[location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 1"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 1"

    currentid += 20

    #Ocean Palace
    #no checks


    #Grand Metro
    if world.options.enable_mission_a.value:
        for i in range (85):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 3"

    currentid += 85

    if world.options.enable_mission_b.value:
        for i in range (85):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 3"

    currentid += 85


    #Power Plant
    if world.options.enable_mission_a.value:
        for i in range (3):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 4"

    currentid += 3

    if world.options.enable_mission_b.value:
        for i in range (5):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 4"

    currentid += 5


    #Casino Park
    if world.options.enable_mission_a.value:
        for i in range (200, 0, -world.options.chaotix_sanity_ring_interval.value):
            world.location_name_to_region[
                location_id_name_dict[currentid + i]] = f"Team {sonic_heroes_story_names[3]} Level 5"

    currentid += 200

    if world.options.enable_mission_b.value:
        for i in range (500, 0, -world.options.chaotix_sanity_ring_interval.value):
            world.location_name_to_region[
                location_id_name_dict[currentid + i]] = f"Team {sonic_heroes_story_names[3]} Level 5"

    currentid += 500


    #Bingo Highway
    if world.options.enable_mission_a.value:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 6"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 6"

    currentid += 20

    #Rail Canyon
    #no checks


    #Bullet Station
    if world.options.enable_mission_a.value:
        for i in range (30):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 8"

    currentid += 30

    if world.options.enable_mission_b.value:
        for i in range (50):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 8"

    currentid += 50


    #Frog Forest
    #no checks


    #Lost Jungle
    if world.options.enable_mission_a.value:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 10"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 10"

    currentid += 20

    #Hang Castle
    if world.options.enable_mission_a.value:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 11"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 11"

    currentid += 10


    #Mystic Mansion
    if world.options.enable_mission_a.value:
        for i in range (60):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 12"

    currentid += 60

    if world.options.enable_mission_b.value:
        for i in range (46):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 12"

    currentid += 46


    #Egg Fleet
    #no checks


    #Final Fortress
    if world.options.enable_mission_a.value:
        for i in range (5):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 14"

    currentid += 5

    if world.options.enable_mission_b.value:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 14"

    currentid += 10


