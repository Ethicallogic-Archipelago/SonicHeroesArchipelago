from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld


from BaseClasses import Item
from .constants import *


class SonicHeroesItem(Item):
    game: str = SONICHEROES


def create_item(world: SonicHeroesWorld, name: str, classification: ItemClassification, amount: int = 1):
    for i in range(amount):
        world.multiworld.itempool.append(SonicHeroesItem(name, classification, world.item_name_to_id[name], world.player))

def create_filler_items(world: SonicHeroesWorld, amount: int):
    filler_list = world.multiworld.random.choices(list(filler_items_to_weights.keys()), weights=list(filler_items_to_weights.values()), k=amount)

    for name in filler_list:
        create_item(world, name, ItemClassification.filler)

def create_trap_items(world: SonicHeroesWorld, amount: int):
    trap_list = world.multiworld.random.choices(list(trap_items_to_weights.keys()), weights=list(trap_items_to_weights.values()), k=amount)

    for name in trap_list:
        create_item(world, name, ItemClassification.trap)


def create_items(world: SonicHeroesWorld):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

    #create_item(world, EMBLEM, ItemClassification.progression)
    #total_location_count -= 1

    if world.options.sonic_story_starting_character != 0:
        create_item(world, PLAYABLESONIC, ItemClassification.progression)
        total_location_count -= 1

    if world.options.sonic_story_starting_character != 1:
        create_item(world, PLAYABLETAILS, ItemClassification.progression)
        total_location_count -= 1

    if world.options.sonic_story_starting_character != 2:
        create_item(world, PLAYABLEKNUCKLES, ItemClassification.progression)
        total_location_count -= 1


    create_item(world, progressive_ability_item_names[SONIC][OCEANREGION][SPEED], ItemClassification.progression, 4)
    total_location_count -= 4

    create_item(world, progressive_ability_item_names[SONIC][OCEANREGION][FLYING], ItemClassification.progression, 2)
    total_location_count -= 2

    create_item(world, progressive_ability_item_names[SONIC][OCEANREGION][POWER], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], ItemClassification.progression, 4)
    total_location_count -= 4

    create_item(world, progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], ItemClassification.progression, 2)
    total_location_count -= 2

    create_item(world, progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, progressive_ability_item_names[SONIC][CASINOREGION][SPEED], ItemClassification.progression, 4)
    total_location_count -= 4

    create_item(world, progressive_ability_item_names[SONIC][CASINOREGION][FLYING], ItemClassification.progression, 2)
    total_location_count -= 2

    create_item(world, progressive_ability_item_names[SONIC][CASINOREGION][POWER], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, progressive_ability_item_names[SONIC][TRAINREGION][SPEED], ItemClassification.progression, 4)
    total_location_count -= 4

    create_item(world, progressive_ability_item_names[SONIC][TRAINREGION][FLYING], ItemClassification.progression, 2)
    total_location_count -= 2

    create_item(world, progressive_ability_item_names[SONIC][TRAINREGION][POWER], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], ItemClassification.progression, 4)
    total_location_count -= 4

    create_item(world, progressive_ability_item_names[SONIC][BIGPLANTREGION][FLYING], ItemClassification.progression, 2)
    total_location_count -= 2

    create_item(world, progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], ItemClassification.progression, 3)
    total_location_count -= 3


    create_item(world, char_levelup_to_item_name[SONIC][SPEED], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, char_levelup_to_item_name[SONIC][FLYING], ItemClassification.progression, 3)
    total_location_count -= 3

    create_item(world, char_levelup_to_item_name[SONIC][POWER], ItemClassification.progression, 3)
    total_location_count -= 3

    world.extra_items = total_location_count

    create_filler_items(world, world.extra_items)
        #create_item(world, EXTRALIFE, ItemClassification.filler)


itemList: list[ItemData] = \
[
    ItemData(0x93930000, EMBLEM, ItemClassification.progression),
    ItemData(0x93930001, GREENCHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930002, BLUECHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930003, YELLOWCHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930004, WHITECHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930005, CYANCHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930006, PURPLECHAOSEMERALD, ItemClassification.progression),
    ItemData(0x93930007, REDCHAOSEMERALD, ItemClassification.progression),

    ItemData(0x93930008, PLAYABLESONIC, ItemClassification.progression),
    ItemData(0x93930009, PLAYABLETAILS, ItemClassification.progression),
    ItemData(0x9393000A, PLAYABLEKNUCKLES, ItemClassification.progression),
    ItemData(0x9393000B, PLAYABLESHADOW, ItemClassification.progression),
    ItemData(0x9393000C, PLAYABLEROUGE, ItemClassification.progression),
    ItemData(0x9393000D, PLAYABLEOMEGA, ItemClassification.progression),
    ItemData(0x9393000E, PLAYABLEAMY, ItemClassification.progression),
    ItemData(0x9393000F, PLAYABLECREAM, ItemClassification.progression),
    ItemData(0x93930010, PLAYABLEBIG, ItemClassification.progression),
    ItemData(0x93930011, PLAYABLEESPIO, ItemClassification.progression),
    ItemData(0x93930012, PLAYABLECHARMY, ItemClassification.progression),
    ItemData(0x93930013, PLAYABLEVECTOR, ItemClassification.progression),
    ItemData(0x93930014, PLAYABLESUPERHARDSONIC, ItemClassification.progression),
    ItemData(0x93930015, PLAYABLESUPERHARDTAILS, ItemClassification.progression),
    ItemData(0x93930016, PLAYABLESUPERHARDKNUCKLES, ItemClassification.progression),

    ItemData(0x93930017, progressive_ability_item_names[SONIC][OCEANREGION][SPEED], ItemClassification.progression),
    ItemData(0x93930018, progressive_ability_item_names[SONIC][OCEANREGION][FLYING], ItemClassification.progression),
    ItemData(0x93930019, progressive_ability_item_names[SONIC][OCEANREGION][POWER], ItemClassification.progression),

    ItemData(0x9393001A, progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], ItemClassification.progression),
    ItemData(0x9393001B, progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], ItemClassification.progression),
    ItemData(0x9393001C, progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], ItemClassification.progression),
    
    ItemData(0x9393001D, progressive_ability_item_names[SONIC][CASINOREGION][SPEED], ItemClassification.progression),
    ItemData(0x9393001E, progressive_ability_item_names[SONIC][CASINOREGION][FLYING], ItemClassification.progression),
    ItemData(0x9393001F, progressive_ability_item_names[SONIC][CASINOREGION][POWER], ItemClassification.progression),
    
    ItemData(0x93930020, progressive_ability_item_names[SONIC][TRAINREGION][SPEED], ItemClassification.progression),
    ItemData(0x93930021, progressive_ability_item_names[SONIC][TRAINREGION][FLYING], ItemClassification.progression),
    ItemData(0x93930022, progressive_ability_item_names[SONIC][TRAINREGION][POWER], ItemClassification.progression),

    ItemData(0x93930023, progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], ItemClassification.progression),
    ItemData(0x93930024, progressive_ability_item_names[SONIC][BIGPLANTREGION][FLYING], ItemClassification.progression),
    ItemData(0x93930025, progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], ItemClassification.progression),

    ItemData(0x93930026, progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], ItemClassification.progression),
    ItemData(0x93930027, progressive_ability_item_names[SONIC][GHOSTREGION][FLYING], ItemClassification.progression),
    ItemData(0x93930028, progressive_ability_item_names[SONIC][GHOSTREGION][POWER], ItemClassification.progression),

    ItemData(0x93930029, progressive_ability_item_names[SONIC][SKYREGION][SPEED], ItemClassification.progression),
    ItemData(0x9393002A, progressive_ability_item_names[SONIC][SKYREGION][FLYING], ItemClassification.progression),
    ItemData(0x9393002B, progressive_ability_item_names[SONIC][SKYREGION][POWER], ItemClassification.progression),
    #to A9

    ItemData(0x939300B0, char_levelup_to_item_name[SONIC][SPEED], ItemClassification.progression),
    ItemData(0x939300B1, char_levelup_to_item_name[SONIC][FLYING], ItemClassification.progression),
    ItemData(0x939300B2, char_levelup_to_item_name[SONIC][POWER], ItemClassification.progression),


    ItemData(0x939300C0, EXTRALIFE, ItemClassification.filler),
    ItemData(0x939300C1, RINGS5, ItemClassification.filler),
    ItemData(0x939300C2, RINGS10, ItemClassification.filler),
    ItemData(0x939300C3, RINGS20, ItemClassification.filler),
    ItemData(0x939300C4, SHIELD, ItemClassification.filler),
    #ItemData(0x939300C5, INVINCIBILITY, ItemClassification.filler),
    #ItemData(0x939300C6, SPEEDLEVELUP, ItemClassification.filler),
    #ItemData(0x939300C7, FLYINGLEVELUP, ItemClassification.filler),
    #ItemData(0x939300C8, POWERLEVELUP, ItemClassification.filler),
    #ItemData(0x939300C9, TEAMLEVELUP, ItemClassification.filler, fillerweight=25),
    ItemData(0x939300CA, TEAMBLASTREFILL, ItemClassification.filler),

    ItemData(0x93930100, STEALTHTRAP, ItemClassification.trap),
    ItemData(0x93930101, FREEZETRAP, ItemClassification.trap),
    ItemData(0x93930102, NOSWAPTRAP, ItemClassification.trap),
    ItemData(0x93930103, RINGTRAP, ItemClassification.trap),
    ItemData(0x93930104, CHARMYTRAP, ItemClassification.trap),
]


filler_items_to_weights = \
    {item.name: item.fillerweight for item in itemList if item.classification == ItemClassification.filler}

trap_items_to_weights = \
    {item.name: item.fillerweight for item in itemList if item.classification == ItemClassification.trap}
