from typing import Dict, Optional, List, Tuple, NamedTuple
import math

from BaseClasses import Item, ItemClassification


class SonicHeroesItem(Item):
    game: str = "Sonic Heroes"


class ItemData(NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification

def create_item(world: "SonicHeroesWorld", name: str, classification: ItemClassification, amount: Optional[int] = 1):

    for i in range(amount):
        world.multiworld.itempool.append(Item(name, classification, item_name_to_id[name], world.player))


def create_items(world: "SonicHeroesWorld"):

    total_location_count = len(world.story_list) * (28 + world.options.number_level_gates) + 7


    useful_emblems = world.default_emblem_pool_size * len(world.story_list) - world.required_emblems

    placed_items = 0


    #Emblems:
    create_item(world, "Emblem", ItemClassification.progression, world.required_emblems)

    placed_items += world.required_emblems


    create_item(world, "Emblem", ItemClassification.useful, useful_emblems)

    placed_items += useful_emblems


    #Emeralds:
    create_item(world, "Green Chaos Emerald", ItemClassification.progression)
    create_item(world, "Blue Chaos Emerald", ItemClassification.progression)
    create_item(world, "Yellow Chaos Emerald", ItemClassification.progression)
    create_item(world, "White Chaos Emerald", ItemClassification.progression)
    create_item(world, "Cyan Chaos Emerald", ItemClassification.progression)
    create_item(world, "Purple Chaos Emerald", ItemClassification.progression)
    create_item(world, "Red Chaos Emerald", ItemClassification.progression)

    placed_items += 7


    #Fillers:

    leftover_items = total_location_count - placed_items

    junk = get_junk_item_names(world.random, leftover_items)

    for name in junk:
        create_item(world, name, ItemClassification.filler)


def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk

junk_weights = {
    "Extra Life": 15,
    "5 Rings": 10,
    "10 Rings": 15,
    "20 Rings": 10,
    "Shield": 20,
    "Invincibility": 5,
}

itemList: List[ItemData] = [
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
    ItemData(0x9393000D, "Invincibility", ItemClassification.filler),
    #ItemData(0x9393000E, "Team Level Up", ItemClassification.filler),
    #ItemData(0x9393000F, "Bonus Stage Key", ItemClassification.filler),
]


item_name_to_id: Dict[str, int] = {item.itemName: item.code for item in itemList}




