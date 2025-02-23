from typing import Dict, Optional, List, Tuple, NamedTuple
import math

from BaseClasses import Item, ItemClassification, MultiWorld


class SonicHeroesItem(Item):
    game: str = "Sonic Heroes"


class ItemData(NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    itemID: int

    #currently not used but will store the address if needed
    address: Tuple[int, int] = None


#def create_multiple(name: str, amount: int, world: MultiWorld, player: int, item_class: ItemClassification, itempool: List[SonicHeroesItem]):
def create_item(world: "SonicHeroesWorld", name: str, classification: ItemClassification, amount: Optional[int] = 1):

    for i in range(amount):
        world.multiworld.itempool.append(Item(name, classification, item_name_to_id[name], world.player))


def create_items(world: "SonicHeroesWorld"):

    total_location_count = len(world.story_list) * 32 + 7

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
    "Extra Life": 65,
    "50 Rings": 35
}

itemList: List[ItemData] = [
    ItemData(0x93930000, "Emblem", ItemClassification.progression, 0x01,),#(0x2b32, 0x04)),
    ItemData(0x93930001, "Green Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930002, "Blue Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930003, "Yellow Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930004, "White Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930005, "Cyan Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930006, "Purple Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930007, "Red Chaos Emerald", ItemClassification.progression, 0x01,),
    ItemData(0x93930008, "Extra Life", ItemClassification.filler, 0x01,),
    ItemData(0x93930009, "50 Rings", ItemClassification.filler, 0x01,),
]


item_name_to_id: Dict[str, int] = {item.itemName: item.code for item in itemList}




