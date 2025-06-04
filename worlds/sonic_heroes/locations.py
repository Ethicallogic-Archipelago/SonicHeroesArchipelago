
from BaseClasses import Location, LocationProgressType

from .names import ItemData, sonic_heroes_story_names, sonic_heroes_level_names, sonic_heroes_extra_names, location_id_name_dict

class SonicHeroesLocation(Location):
    game: str = "Sonic Heroes"


def generate_locations(world):

    #currentid = 0x939300A0

    generate_missions(world, 0)
    generate_missions(world, 1)
    generate_missions(world, 2)
    generate_missions(world, 3)

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


            #world.spoiler_string += f"Entering Location Dict Entry for extra: {world.shuffleable_boss_list[i]}\nThe Entry is: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]} {story} --- ID: {currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)} --- Region Name: {sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}\n\n"
            world.location_name_to_region[location_id_name_dict[currentid + (2 * world.shuffleable_boss_list[i]) + (42 * x)]] = f"{sonic_heroes_extra_names[world.shuffleable_boss_list[i]]}"

    #Final Boss
    world.location_name_to_region["Metal Overlord"] = f"Metal Overlord"

    if world.options.dark_sanity.value > 0 and (world.options.dark_story.value == 2 or world.options.dark_story.value == 3):
        generate_dark_sanity(world)

    if world.options.rose_sanity.value > 0 and (world.options.rose_story.value == 2 or world.options.rose_story.value == 3):
        generate_rose_sanity(world)

    if world.options.chaotix_sanity.value > 0 and world.options.chaotix_story.value > 0:
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

    if "SUPER SECRET HIDDEN" in name:
        location.progress_type = LocationProgressType.EXCLUDED

    if "Metal Overlord" in name:
        location.progress_type = LocationProgressType.EXCLUDED

    if "Emerald Stage" in name:
        if world.options.emerald_stage_location_type.value == 0:
            location.progress_type = LocationProgressType.PRIORITY

        elif world.options.emerald_stage_location_type.value == 2:
            location.progress_type = LocationProgressType.EXCLUDED

    if code in world.excluded_sanity_locations:
        location.progress_type = LocationProgressType.EXCLUDED
        world.spoiler_string += f"Adding Location: {name} to Excluded Locations\n"


    region.locations.append(location)

def generate_missions(world, storyindex):
    if world.story_options[storyindex] == 0: #disabled
        return

    elif world.story_options[storyindex] == 1: #Act 1 only
        for mission in range(14):
            world.location_name_to_region[
                f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 1"] = \
                f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

    elif world.story_options[storyindex] == 2: #Act 2 Only
        for mission in range(14):
            if storyindex == 0 and world.options.super_hard_mode_sonic_act_2.value:
                world.location_name_to_region[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Super Hard Mode"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
            else:
                world.location_name_to_region[
                    f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 2"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"


    elif world.story_options[storyindex] == 3: #Both Acts
        for mission in range(14):
            world.location_name_to_region[
                f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 1"] = \
                f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
            if storyindex == 0 and world.options.super_hard_mode_sonic_act_2.value:
                world.location_name_to_region[f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Super Hard Mode"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
            else:
                world.location_name_to_region[
                    f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 2"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

    generate_key_sanity(world, storyindex)
    generate_checkpoint_sanity(world, storyindex)

def generate_key_sanity(world, storyindex):
    if world.key_sanity_options[storyindex] == 0: #disabled
        return

    elif storyindex == 0 and world.story_options[0] == 2 and world.options.super_hard_mode_sonic_act_2.value == 1: #Sonic with Act 2 Only and Super Hard
        return

    elif world.key_sanity_options[storyindex] == 1: #only 1 Set
        for mission in range(14):
            for key in range(world.key_sanity_key_amounts[storyindex][mission]):
                if key + 1 == 4:
                    world.location_name_to_region[
                        f"SUPER SECRET HIDDEN Bonus Key"] = \
                        f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
                else:
                    world.location_name_to_region[
                        f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Bonus Key {key + 1}"] = \
                        f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"


    elif world.key_sanity_options[storyindex] == 2: #set for each act
        for mission in range(14):
            for key in range(world.key_sanity_key_amounts[storyindex][mission]):
                if world.story_options[storyindex] != 2: #Act 1 enabled
                    if key + 1 == 4:
                        world.location_name_to_region[
                            f"SUPER SECRET HIDDEN Act 1 Bonus Key"] = \
                            f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
                    else:
                        world.location_name_to_region[
                            f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 1 Bonus Key {key + 1}"] = \
                            f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

                if world.story_options[storyindex] != 1: #Act 2 enabled
                    if not(storyindex == 0 and world.options.super_hard_mode_sonic_act_2.value == 1): #check for Super Hard
                        if key + 1 == 4:
                            world.location_name_to_region[
                                f"SUPER SECRET HIDDEN Act 2 Bonus Key"] = \
                                f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"
                        else:
                            world.location_name_to_region[
                                f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 2 Bonus Key {key + 1}"] = \
                                f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"


def generate_checkpoint_sanity(world, storyindex):
    if world.checkpoint_sanity_options[storyindex] == 0:  # disabled
        return

    #"Final Fortress Rose Act 2 Checkpoint 1",
    #"Grand Metropolis Super Hard Mode Checkpoint 1",

    elif world.checkpoint_sanity_options[storyindex] == 1: #only 1 set
        for mission in range(14):
            for cp in range(world.checkpoint_amounts[storyindex][mission]):
                world.location_name_to_region[
                    f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Checkpoint {cp + 1}"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

    elif world.checkpoint_sanity_options[storyindex] == 2: #SuperHard Only (only Sonic)
        for mission in range(14):
            for cp in range(world.checkpoint_amounts[4][mission]):
                world.location_name_to_region[
                    f"{sonic_heroes_level_names[mission + 1]} Super Hard Mode Checkpoint {cp + 1}"] = \
                    f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"


    elif world.checkpoint_sanity_options[storyindex] == 3: #Each Act
        for mission in range(14):
            if world.story_options[storyindex] != 2:  # Act 1 enabled
                for cp in range(world.checkpoint_amounts[storyindex][mission]):
                    world.location_name_to_region[
                        f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 1 Checkpoint {cp + 1}"] = \
                        f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

            if world.story_options[storyindex] != 1:  # Act 2 enabled
                if world.options.super_hard_mode_sonic_act_2.value and storyindex == 0: #SuperHardMode
                    for cp in range(world.checkpoint_amounts[4][mission]):
                        world.location_name_to_region[
                            f"{sonic_heroes_level_names[mission + 1]} Super Hard Mode Checkpoint {cp + 1}"] = \
                            f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"

                else:
                    for cp in range(world.checkpoint_amounts[storyindex][mission]):
                        world.location_name_to_region[
                            f"{sonic_heroes_level_names[mission + 1]} {sonic_heroes_story_names[storyindex]} Act 2 Checkpoint {cp + 1}"] = \
                            f"Team {sonic_heroes_story_names[storyindex]} Level {mission + 1}"



def generate_dark_sanity(world):
    #0x9393014F (starts at 150) - 0x939306C7
    currentid = 0x9393014F

    for mission in range(14):
        for i in range(100, 0, -world.options.dark_sanity):
            world.location_name_to_region[location_id_name_dict[currentid + i + (mission * 100)]] = f"Team {sonic_heroes_story_names[1]} Level {mission + 1}"
            if i >= 101 - world.options.sanity_excluded_percent:
                world.excluded_sanity_locations.append(currentid + i + (mission * 100))


def generate_rose_sanity(world):
    #0x939306C7 (starts at 6C8) - 0x939311B7
    currentid = 0x939306C7

    for mission in range(14):
        for i in range(200, 0, -world.options.rose_sanity):
            world.location_name_to_region[location_id_name_dict[
                currentid + i + (mission * 200)]] = f"Team {sonic_heroes_story_names[2]} Level {mission + 1}"
            if i >= 201 - (world.options.sanity_excluded_percent * 2):
                world.excluded_sanity_locations.append(currentid + i + (mission * 200))


def generate_chaotix_sanity(world):
    #Chaotix Sanity
    #1189 checks - 524
    #Mission A only is 223 + CP
    #Mission B only is 266 + CP
    #Both is 489
    #SH - 10, 20
    #OP - 0, 0
    #GM - 85, 85 (time limit)
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
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 1"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 1"
            if i >= 20 - (20 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 20

    #Ocean Palace
    #no checks


    #Grand Metro
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (85):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 3"
            if i >= 85 - (85 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 85

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (85):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 3"
            if i >= 85 - (85 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 85


    #Power Plant
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (3):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 4"
            if i >= 3 - (3 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 3

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (5):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 4"
            if i >= 5 - (5 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 5


    #Casino Park
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (200, 0, -world.options.chaotix_sanity.value):
            world.location_name_to_region[
                location_id_name_dict[currentid + i]] = f"Team {sonic_heroes_story_names[3]} Level 5"
            if i - 1 >= 200 - (200 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i)

    currentid += 200

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (500, 0, -world.options.chaotix_sanity.value):
            world.location_name_to_region[
                location_id_name_dict[currentid + i]] = f"Team {sonic_heroes_story_names[3]} Level 5"
            if i - 1 >= 500 - (500 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i)

    currentid += 500


    #Bingo Highway
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 6"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 6"
            if i >= 20 - (20 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 20

    #Rail Canyon
    #no checks


    #Bullet Station
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (30):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 8"
            if i >= 30 - (30 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 30

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (50):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 8"
            if i >= 50 - (50 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 50


    #Frog Forest
    #no checks


    #Lost Jungle
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 10"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (20):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 10"
            if i >= 20 - (20 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 20

    #Hang Castle
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 11"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 11"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10


    #Mystic Mansion
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (60):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 12"
            if i >= 60 - (60 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 60

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (46):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 12"
            if i >= 46 - (46 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 46


    #Egg Fleet
    #no checks


    #Final Fortress
    if world.options.chaotix_story.value == 1 or world.options.chaotix_story.value == 3:
        for i in range (5):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 14"
            if i >= 5 - (5 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 5

    if world.options.chaotix_story.value == 2 or world.options.chaotix_story.value == 3:
        for i in range (10):
            world.location_name_to_region[
                location_id_name_dict[currentid + i + 1]] = f"Team {sonic_heroes_story_names[3]} Level 14"
            if i >= 10 - (10 * (world.options.sanity_excluded_percent / 100)):
                world.excluded_sanity_locations.append(currentid + i + 1)

    currentid += 10


