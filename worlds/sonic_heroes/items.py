from typing import NamedTuple
import math

from BaseClasses import Item, ItemClassification

from .names import *


class SonicHeroesItem(Item):
    game: str = "Sonic Heroes"

def create_item(world, name: str, classification: ItemClassification, amount: int = 1):
    for i in range(amount):
        world.multiworld.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_items(world):

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    world.spoiler_string += f"THE FULL ITEM POOL SIZE IS {total_location_count}\n"

    useful_emblems = world.emblem_pool_size - world.required_emblems

    #Emblems:
    #create_item(world, "Emblem", ItemClassification.progression, world.emblem_pool_size)
    create_item(world, "Emblem", ItemClassification.progression, world.required_emblems)
    create_item(world, "Emblem", ItemClassification.useful, useful_emblems)

    if (world.options.goal_unlock_condition.value != 1):
        #Emeralds:
        create_item(world, "Green Chaos Emerald", ItemClassification.progression)
        create_item(world, "Blue Chaos Emerald", ItemClassification.progression)
        create_item(world, "Yellow Chaos Emerald", ItemClassification.progression)
        create_item(world, "White Chaos Emerald", ItemClassification.progression)
        create_item(world, "Cyan Chaos Emerald", ItemClassification.progression)
        create_item(world, "Purple Chaos Emerald", ItemClassification.progression)
        create_item(world, "Red Chaos Emerald", ItemClassification.progression)

    #Fillers:
    remaining_locations = total_location_count - world.emblem_pool_size

    if (world.options.goal_unlock_condition.value != 1):
        #remove 7 filler items if Emeralds are added
        remaining_locations -= 7


    #limit ring filler if ringsanity options are at 1
    checkRingFiller(world)


    #print(f"Remaining items here: {remaining_locations}")
    trap_count = round(remaining_locations * world.options.trap_fill.value / 100)
    junk_count = remaining_locations - trap_count

    trap_weights = {
    "Stealth Trap": world.options.stealth_trap_weight.value,
    "Freeze Trap": world.options.freeze_trap_weight.value,
    "No Swap Trap": world.options.no_swap_trap_weight.value,
    "Ring Trap": world.options.ring_trap_weight.value,
    "Charmy Trap": world.options.charmy_trap_weight.value
    }


    junk = get_junk_item_names(world.multiworld.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)

    trap = get_trap_item_names(world.multiworld.random, trap_count, trap_weights)
    for name in trap:
        create_item(world, name, ItemClassification.trap)


def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk


def get_trap_item_names(rand, k: int, trap_weights) -> str:
    trap = rand.choices(
        list(trap_weights.keys()),
        weights=list(trap_weights.values()),
        k=k)
    return trap

def checkRingFiller(world):

    #If RingSanity Interval at 1
    if ("Rose" in world.story_list and world.options.rose_sanity.value == 1 and world.options.rose_sanity.value > 1) or ("Chaotix" in world.story_list and world.options.chaotix_sanity.value == 1):

        #out of 800
        junk_weights["5 Rings"] = 15
        junk_weights["10 Rings"] = 10
        junk_weights["20 Rings"] = 5

        junk_weights["Extra Life"] += 35
        junk_weights["Shield"] += 35
        junk_weights["Speed Level Up"] += 35
        junk_weights["Power Level Up"] += 35
        junk_weights["Flying Level Up"] += 35
        junk_weights["Team Level Up"] += 35


    #If RingSanity Interval at 5
    if ("Rose" in world.story_list and world.options.rose_sanity.value == 5 and world.options.rose_sanity.value > 1) or ("Chaotix" in world.story_list and world.options.chaotix_sanity.value == 5):
        #out of 800
        junk_weights["5 Rings"] = 30
        junk_weights["10 Rings"] = 20
        junk_weights["20 Rings"] = 10

        junk_weights["Extra Life"] += 30
        junk_weights["Shield"] += 30
        junk_weights["Speed Level Up"] += 30
        junk_weights["Power Level Up"] += 30
        junk_weights["Flying Level Up"] += 30
        junk_weights["Team Level Up"] += 30

        #If RingSanity Interval at 10
    if ("Rose" in world.story_list and world.options.rose_sanity.value == 10 and world.options.rose_sanity.value > 1) or ("Chaotix" in world.story_list and world.options.chaotix_sanity.value == 10):
        #out of 800
        junk_weights["5 Rings"] = 60
        junk_weights["10 Rings"] = 40
        junk_weights["20 Rings"] = 20

        junk_weights["Extra Life"] += 20
        junk_weights["Shield"] += 20
        junk_weights["Speed Level Up"] += 20
        junk_weights["Power Level Up"] += 20
        junk_weights["Flying Level Up"] += 20
        junk_weights["Team Level Up"] += 20




itemList: list[ItemData] = [
    ItemData(0x93930000, "Emblem", ItemClassification.progression),
    ItemData(0x93930001, "Green Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930002, "Blue Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930003, "Yellow Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930004, "White Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930005, "Cyan Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930006, "Purple Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930007, "Red Chaos Emerald", ItemClassification.progression),
    ItemData(0x93930008, "Extra Life", ItemClassification.filler),
    ItemData(0x93930009, "5 Rings", ItemClassification.filler),
    ItemData(0x9393000A, "10 Rings", ItemClassification.filler),
    ItemData(0x9393000B, "20 Rings", ItemClassification.filler),
    ItemData(0x9393000C, "Shield", ItemClassification.filler),
    #ItemData(0x9393000D, "Invincibility", ItemClassification.filler),
    ItemData(0x9393000E, "Speed Level Up", ItemClassification.filler),
    ItemData(0x9393000F, "Power Level Up", ItemClassification.filler),
    ItemData(0x93930010, "Flying Level Up", ItemClassification.filler),
    ItemData(0x93930011, "Team Level Up", ItemClassification.filler),

    ItemData(0x93930100, "Stealth Trap", ItemClassification.trap),
    ItemData(0x93930101, "Freeze Trap", ItemClassification.trap),
    ItemData(0x93930102, "No Swap Trap", ItemClassification.trap),
    ItemData(0x93930103, "Ring Trap", ItemClassification.trap),
    ItemData(0x93930104, "Charmy Trap", ItemClassification.trap),
]

junk_weights = {
    "Extra Life": 160,
    "5 Rings": 120,
    "10 Rings": 80,
    "20 Rings": 40,
    "Shield": 160,
    #"Invincibility": 160,
    "Speed Level Up": 72,
    "Power Level Up": 72,
    "Flying Level Up": 72,
    "Team Level Up": 24,
}

#stealth
#OP 2
#FF 1 and 2 (Frogs)
#HC 2
#EF 1 and 2