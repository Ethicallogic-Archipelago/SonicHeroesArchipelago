from typing import Dict, NamedTuple
from collections import namedtuple
from BaseClasses import Location, LocationProgressType

from .names import ItemData, LocationData, sonic_heroes_story_names, sonic_heroes_level_names, sonic_heroes_extra_names, location_dict

class SonicHeroesLocation(Location):
    game: str = "Sonic Heroes"


def generate_locations(world):

    currentid = 0x939300A0

    for story in range(4):  #for each story
        if sonic_heroes_story_names[story] in world.story_list: #check of story enabled
            for mission in range(14): #for each mission
                if world.options.enable_mission_a.value:  #if mission A enabled
                    #location_dict[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[story]} Act 1"] = LocData(currentid + (2 * mission) + (42 * story), f"Team {sonic_heroes_story_names[story]} Level {mission + 1}")
                    location_dict[currentid + (2 * mission) + (42 * story)].region = f"Team {world.story_list[story]} Level {mission + 1}"
                    # 0x939300a0: LocationData("Seaside Hill Sonic Act 1", "No Region", -99),


                if world.options.enable_mission_b.value:  #if mission B enabled
                    #location_dict[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[story]} Act 2"] = LocData(currentid + (2 * mission) + (42 * story) + 1, f"Team {sonic_heroes_story_names[story]} Level {mission + 1}")
                    location_dict[currentid + (2 * mission) + (42 * story) + 1].region = f"Team {world.story_list[story]} Level {mission + 1}"


    #emeralds
    for i in range(7):
        #location_dict[f"{sonic_heroes_level_names[2 * (i + 1)]} Emerald Stage"] = LocData(0x93930148 + i, f"Emerald {i + 1}")
        location_dict[0x93930148 + i].region = f"Emerald {i + 1}"


    #Boss Gate Locations
    #dont have ID so not needed
    #for i in range(world.options.number_level_gates.value):
        #location_dict[f"Boss Gate {i + 1}"] = LocData(None, f"Gate Boss between Gate {i} and Gate {i + 1}")



    currentid = 0x939300BC
    #extras
    x = 0
    for i in range(world.options.number_level_gates.value):
        for story in world.story_list:
            for k, v in sonic_heroes_story_names.items():
                if v == story:
                    x = k #x = 0-3 for example


            world.spoiler_string += f"Entering Location Dict Entry for extra: {world.shuffleable_boss_list[i]}\nThe Entry is: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]} {story} --- ID: {currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)} --- Region Name: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}\n\n"

            #location_dict[f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]} {story}"] = LocData(currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x), f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}")

            location_dict[currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)].region = f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}"
         

    #Final Boss
    #location_dict["Metal Overlord"] = LocData(None, "Metal Overlord")


    if world.options.dark_sanity: #dark sanity
        generate_dark_sanity(world)

    if world.options.rose_sanity: #rose sanity
        generate_rose_sanity(world)

    if world.options.chaotix_sanity: #chaotix sanity
        generate_chaotix_sanity(world)


    #world.location_name_to_id = {name: item.code for name, item in location_dict.items()}


    #print stuff here
    #world.spoiler_string += "LOCATION DICT HERE: \n\n"

    #sorted_dict = {}

    #for k, v in location_dict.items():
    #    if v.code != None:
    #        sorted_dict[v.code] = k

    #for k, v in sorted(sorted_dict.items()):
    #   world.spoiler_string += f"{hex(k)}: LocationData(\"{v}\", \"No Region\", {-1}),\n"




def create_locations(world, region):
    create_locations_from_dict(world, location_dict, region)


def create_locations_from_dict(world, loc_dict, region):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, data.name, key)


def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)

    if "Emerald Stage" in name:
        location.progress_type = LocationProgressType.PRIORITY
    region.locations.append(location)






def generate_dark_sanity(world):
    if not world.options.enable_mission_b.value:
        return None #leave if mission B not enabled

    #0x9393014F (starts at 150) - 0x939306C7
    currentid = 0x9393014F

    for mission in range(14):
        for i in range(100, 0, -world.options.dark_sanity_enemy_interval):
            #location_dict[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[1]} Act 2 Enemies Killed: {i}"] = LocData(currentid + i + (mission * 100), f"Team {sonic_heroes_story_names[1]} Level {mission + 1}")

            location_dict[currentid + i + (mission * 100)].region = f"Team {sonic_heroes_story_names[1]} Level {mission + 1}"


def generate_rose_sanity(world):
    if not world.options.enable_mission_b.value:
        return None #leave if mission B not enabled

    #0x939306C7 (starts at 6C8) - 0x939311B7
    currentid = 0x939306C7

    for mission in range(14):
        for i in range(200, 0, -world.options.rose_sanity_ring_interval):
            #location_dict[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[2]} Act 2 Rings Collected: {i}"] = LocData(currentid + i + (mission * 200), f"Team {sonic_heroes_story_names[2]} Level {mission + 1}")

            location_dict[currentid + i + (mission * 200)].region = f"Team {sonic_heroes_story_names[2]} Level {mission + 1}"




def generate_chaotix_sanity(world):
    #Chaotix Sanity
    #1189 checks - 524
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
            #location_dict[f"{sonic_heroes_level_names[1]} {sonic_heroes_story_names[3]} Act 1 Hermit Crabs Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 1")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 1"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            #location_dict[f"{sonic_heroes_level_names[1]} {sonic_heroes_story_names[3]} Act 2 Hermit Crabs Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 1")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 1"

    currentid += 20

    #Ocean Palace
    #no checks


    #Grand Metro
    if world.options.enable_mission_a.value:
        for i in range (85):
            #location_dict[f"{sonic_heroes_level_names[3]} {sonic_heroes_story_names[3]} Act 1 Enemies Killed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 3")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 3"

    currentid += 85

    if world.options.enable_mission_b.value:
        for i in range (85):
            #location_dict[f"{sonic_heroes_level_names[3]} {sonic_heroes_story_names[3]} Act 2 Enemies Killed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 3")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 3"

    currentid += 85


    #Power Plant
    if world.options.enable_mission_a.value:
        for i in range (3):
            #location_dict[f"{sonic_heroes_level_names[4]} {sonic_heroes_story_names[3]} Act 1 Gold Turtles Killed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 4")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 4"

    currentid += 3

    if world.options.enable_mission_b.value:
        for i in range (5):
            #location_dict[f"{sonic_heroes_level_names[4]} {sonic_heroes_story_names[3]} Act 2 Gold Turtles Killed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 4")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 4"

    currentid += 5


    #Casino Park
    if world.options.enable_mission_a.value:
        for i in range (200, 0, -world.options.chaotix_sanity_ring_interval.value):
            #location_dict[f"{sonic_heroes_level_names[5]} {sonic_heroes_story_names[3]} Act 1 Rings Collected: {i}"] = LocData(currentid + i, f"Team {sonic_heroes_story_names[3]} Level 5")

            location_dict[currentid + i].region = f"Team {sonic_heroes_story_names[3]} Level 5"

    currentid += 200

    if world.options.enable_mission_b.value:
        for i in range (500, 0, -world.options.chaotix_sanity_ring_interval.value):
            #location_dict[f"{sonic_heroes_level_names[5]} {sonic_heroes_story_names[3]} Act 2 Rings Collected: {i}"] = LocData(currentid + i, f"Team {sonic_heroes_story_names[3]} Level 5")

            location_dict[currentid + i].region = f"Team {sonic_heroes_story_names[3]} Level 5"

    currentid += 500


    #Bingo Highway
    if world.options.enable_mission_a.value:
        for i in range (10):
            #location_dict[f"{sonic_heroes_level_names[6]} {sonic_heroes_story_names[3]} Act 1 Casino Chips Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 6")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 6"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            #location_dict[f"{sonic_heroes_level_names[6]} {sonic_heroes_story_names[3]} Act 2 Casino Chips Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 6")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 6"

    currentid += 20

    #Rail Canyon
    #no checks


    #Bullet Station
    if world.options.enable_mission_a.value:
        for i in range (30):
            #location_dict[f"{sonic_heroes_level_names[8]} {sonic_heroes_story_names[3]} Act 1 Capsules Destroyed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 8")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 8"

    currentid += 30

    if world.options.enable_mission_b.value:
        for i in range (50):
            #location_dict[f"{sonic_heroes_level_names[8]} {sonic_heroes_story_names[3]} Act 2 Capsules Destroyed: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 8")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 8"

    currentid += 50


    #Frog Forest
    #no checks


    #Lost Jungle
    if world.options.enable_mission_a.value:
        for i in range (10):
            #location_dict[f"{sonic_heroes_level_names[10]} {sonic_heroes_story_names[3]} Act 1 Chao Saved: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 10")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 10"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (20):
            #location_dict[f"{sonic_heroes_level_names[10]} {sonic_heroes_story_names[3]} Act 2 Chao Saved: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 10")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 10"

    currentid += 20

    #Hang Castle
    if world.options.enable_mission_a.value:
        for i in range (10):
            #location_dict[f"{sonic_heroes_level_names[11]} {sonic_heroes_story_names[3]} Act 1 Keys Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 11")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 11"

    currentid += 10

    if world.options.enable_mission_b.value:
        for i in range (10):
            #location_dict[f"{sonic_heroes_level_names[11]} {sonic_heroes_story_names[3]} Act 2 Keys Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 11")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 11"

    currentid += 10


    #Mystic Mansion
    if world.options.enable_mission_a.value:
        for i in range (60):
            #location_dict[f"{sonic_heroes_level_names[12]} {sonic_heroes_story_names[3]} Act 1 Red Torches Extinguished: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 12")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 12"

    currentid += 60

    if world.options.enable_mission_b.value:
        for i in range (46):
            #location_dict[f"{sonic_heroes_level_names[12]} {sonic_heroes_story_names[3]} Act 2 Blue Torches Extinguished: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 12")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 12"

    currentid += 46


    #Egg Fleet
    #no checks


    #Final Fortress
    if world.options.enable_mission_a.value:
        for i in range (5):
            #location_dict[f"{sonic_heroes_level_names[14]} {sonic_heroes_story_names[3]} Act 1 Keys Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 14")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 14"

    currentid += 5

    if world.options.enable_mission_b.value:
        for i in range (10):
            #location_dict[f"{sonic_heroes_level_names[14]} {sonic_heroes_story_names[3]} Act 2 Keys Collected: {i + 1}"] = LocData(currentid + i + 1, f"Team {sonic_heroes_story_names[3]} Level 14")

            location_dict[currentid + i + 1].region = f"Team {sonic_heroes_story_names[3]} Level 14"

    currentid += 10


