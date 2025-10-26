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
        create_item(world, get_playable_char_item_name(CHARSONIC), ItemClassification.progression)
        total_location_count -= 1

    if world.options.sonic_story_starting_character != 1:
        create_item(world, get_playable_char_item_name(CHARTAILS), ItemClassification.progression)
        total_location_count -= 1

    if world.options.sonic_story_starting_character != 2:
        create_item(world, get_playable_char_item_name(CHARKNUCKLES), ItemClassification.progression)
        total_location_count -= 1


    if world.options.ability_unlocks == 0:
        for region in world.regular_regions:
            for team in world.enabled_teams:
                for ability in get_all_abilities_for_team(team):
                    create_item(world, get_ability_item_name_without_world(team, region, ability), ItemClassification.progression)
                    total_location_count -= 1


    elif world.options.ability_unlocks == 1:
        for team in world.enabled_teams:
            for ability in get_all_abilities_for_team(team):
                create_item(world, get_ability_item_name_without_world(team, ALLREGIONS, ability), ItemClassification.progression)
                total_location_count -= 1


    if world.options.goal_unlock_condition >= 1:
        create_item(world, GREENCHAOSEMERALD, ItemClassification.progression)
        create_item(world, BLUECHAOSEMERALD, ItemClassification.progression)
        create_item(world, YELLOWCHAOSEMERALD, ItemClassification.progression)
        create_item(world, WHITECHAOSEMERALD, ItemClassification.progression)
        create_item(world, CYANCHAOSEMERALD, ItemClassification.progression)
        create_item(world, PURPLECHAOSEMERALD, ItemClassification.progression)
        create_item(world, REDCHAOSEMERALD, ItemClassification.progression)
        total_location_count -= 7



    world.extra_items = total_location_count

    print(f"Extra Items count: {total_location_count}")

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

    ItemData(0x93930008, get_playable_char_item_name(CHARSONIC), ItemClassification.progression),
    ItemData(0x93930009, get_playable_char_item_name(CHARTAILS), ItemClassification.progression),
    ItemData(0x9393000A, get_playable_char_item_name(CHARKNUCKLES), ItemClassification.progression),
    ItemData(0x9393000B, get_playable_char_item_name(CHARSHADOW), ItemClassification.progression),
    ItemData(0x9393000C, get_playable_char_item_name(CHARROUGE), ItemClassification.progression),
    ItemData(0x9393000D, get_playable_char_item_name(CHAROMEGA), ItemClassification.progression),
    ItemData(0x9393000E, get_playable_char_item_name(CHARAMY), ItemClassification.progression),
    ItemData(0x9393000F, get_playable_char_item_name(CHARCREAM), ItemClassification.progression),
    ItemData(0x93930010, get_playable_char_item_name(CHARBIG), ItemClassification.progression),
    ItemData(0x93930011, get_playable_char_item_name(CHARESPIO), ItemClassification.progression),
    ItemData(0x93930012, get_playable_char_item_name(CHARCHARMY), ItemClassification.progression),
    ItemData(0x93930013, get_playable_char_item_name(CHARVECTOR), ItemClassification.progression),
    ItemData(0x93930014, get_playable_char_item_name(CHARSUPERHARDSONIC), ItemClassification.progression),
    ItemData(0x93930015, get_playable_char_item_name(CHARSUPERHARDTAILS), ItemClassification.progression),
    ItemData(0x93930016, get_playable_char_item_name(CHARSUPERHARDKNUCKLES), ItemClassification.progression),


    ItemData(0x93930020, get_ability_item_name_without_world(SONIC, ALLREGIONS, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x93930021, get_ability_item_name_without_world(SONIC, ALLREGIONS, TORNADO), ItemClassification.progression),
    ItemData(0x93930022, get_ability_item_name_without_world(SONIC, ALLREGIONS, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x93930023, get_ability_item_name_without_world(SONIC, ALLREGIONS, LIGHTDASH), ItemClassification.progression),
    ItemData(0x93930024, get_ability_item_name_without_world(SONIC, ALLREGIONS, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x93930025, get_ability_item_name_without_world(SONIC, ALLREGIONS, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x93930026, get_ability_item_name_without_world(SONIC, ALLREGIONS, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x93930027, get_ability_item_name_without_world(SONIC, ALLREGIONS, INVISIBILITY), ItemClassification.progression),
    ItemData(0x93930028, get_ability_item_name_without_world(SONIC, ALLREGIONS, SHURIKEN), ItemClassification.progression),
    ItemData(0x93930029, get_ability_item_name_without_world(SONIC, ALLREGIONS, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x9393002A, get_ability_item_name_without_world(SONIC, ALLREGIONS, FLIGHT), ItemClassification.progression),
    ItemData(0x9393002B, get_ability_item_name_without_world(SONIC, ALLREGIONS, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x9393002C, get_ability_item_name_without_world(SONIC, ALLREGIONS, CHEESECANNON), ItemClassification.progression),
    ItemData(0x9393002D, get_ability_item_name_without_world(SONIC, ALLREGIONS, FLOWERSTING), ItemClassification.progression),
    ItemData(0x9393002E, get_ability_item_name_without_world(SONIC, ALLREGIONS, POWERATTACK), ItemClassification.progression),
    ItemData(0x9393002F, get_ability_item_name_without_world(SONIC, ALLREGIONS, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x93930030, get_ability_item_name_without_world(SONIC, ALLREGIONS, GLIDE), ItemClassification.progression),
    ItemData(0x93930031, get_ability_item_name_without_world(SONIC, ALLREGIONS, FIREDUNK), ItemClassification.progression),
    ItemData(0x93930032, get_ability_item_name_without_world(SONIC, ALLREGIONS, BELLYFLOP), ItemClassification.progression),


    ItemData(0x93930040, get_ability_item_name_without_world(SONIC, OCEANREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x93930041, get_ability_item_name_without_world(SONIC, OCEANREGION, TORNADO), ItemClassification.progression),
    ItemData(0x93930042, get_ability_item_name_without_world(SONIC, OCEANREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x93930043, get_ability_item_name_without_world(SONIC, OCEANREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x93930044, get_ability_item_name_without_world(SONIC, OCEANREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x93930045, get_ability_item_name_without_world(SONIC, OCEANREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x93930046, get_ability_item_name_without_world(SONIC, OCEANREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x93930047, get_ability_item_name_without_world(SONIC, OCEANREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x93930048, get_ability_item_name_without_world(SONIC, OCEANREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x93930049, get_ability_item_name_without_world(SONIC, OCEANREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x9393004A, get_ability_item_name_without_world(SONIC, OCEANREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x9393004B, get_ability_item_name_without_world(SONIC, OCEANREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x9393004C, get_ability_item_name_without_world(SONIC, OCEANREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x9393004D, get_ability_item_name_without_world(SONIC, OCEANREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x9393004E, get_ability_item_name_without_world(SONIC, OCEANREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x9393004F, get_ability_item_name_without_world(SONIC, OCEANREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x93930050, get_ability_item_name_without_world(SONIC, OCEANREGION, GLIDE), ItemClassification.progression),
    ItemData(0x93930051, get_ability_item_name_without_world(SONIC, OCEANREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x93930052, get_ability_item_name_without_world(SONIC, OCEANREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x93930060, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x93930061, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, TORNADO), ItemClassification.progression),
    ItemData(0x93930062, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x93930063, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x93930064, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x93930065, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x93930066, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x93930067, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x93930068, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x93930069, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x9393006A, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x9393006B, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x9393006C, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x9393006D, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x9393006E, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x9393006F, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x93930070, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, GLIDE), ItemClassification.progression),
    ItemData(0x93930071, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x93930072, get_ability_item_name_without_world(SONIC, HOTPLANTREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x93930080, get_ability_item_name_without_world(SONIC, CASINOREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x93930081, get_ability_item_name_without_world(SONIC, CASINOREGION, TORNADO), ItemClassification.progression),
    ItemData(0x93930082, get_ability_item_name_without_world(SONIC, CASINOREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x93930083, get_ability_item_name_without_world(SONIC, CASINOREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x93930084, get_ability_item_name_without_world(SONIC, CASINOREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x93930085, get_ability_item_name_without_world(SONIC, CASINOREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x93930086, get_ability_item_name_without_world(SONIC, CASINOREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x93930087, get_ability_item_name_without_world(SONIC, CASINOREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x93930088, get_ability_item_name_without_world(SONIC, CASINOREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x93930089, get_ability_item_name_without_world(SONIC, CASINOREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x9393008A, get_ability_item_name_without_world(SONIC, CASINOREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x9393008B, get_ability_item_name_without_world(SONIC, CASINOREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x9393008C, get_ability_item_name_without_world(SONIC, CASINOREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x9393008D, get_ability_item_name_without_world(SONIC, CASINOREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x9393008E, get_ability_item_name_without_world(SONIC, CASINOREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x9393008F, get_ability_item_name_without_world(SONIC, CASINOREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x93930090, get_ability_item_name_without_world(SONIC, CASINOREGION, GLIDE), ItemClassification.progression),
    ItemData(0x93930091, get_ability_item_name_without_world(SONIC, CASINOREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x93930092, get_ability_item_name_without_world(SONIC, CASINOREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x939300A0, get_ability_item_name_without_world(SONIC, TRAINREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x939300A1, get_ability_item_name_without_world(SONIC, TRAINREGION, TORNADO), ItemClassification.progression),
    ItemData(0x939300A2, get_ability_item_name_without_world(SONIC, TRAINREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x939300A3, get_ability_item_name_without_world(SONIC, TRAINREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x939300A4, get_ability_item_name_without_world(SONIC, TRAINREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x939300A5, get_ability_item_name_without_world(SONIC, TRAINREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x939300A6, get_ability_item_name_without_world(SONIC, TRAINREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x939300A7, get_ability_item_name_without_world(SONIC, TRAINREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x939300A8, get_ability_item_name_without_world(SONIC, TRAINREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x939300A9, get_ability_item_name_without_world(SONIC, TRAINREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x939300AA, get_ability_item_name_without_world(SONIC, TRAINREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x939300AB, get_ability_item_name_without_world(SONIC, TRAINREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x939300AC, get_ability_item_name_without_world(SONIC, TRAINREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x939300AD, get_ability_item_name_without_world(SONIC, TRAINREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x939300AE, get_ability_item_name_without_world(SONIC, TRAINREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x939300AF, get_ability_item_name_without_world(SONIC, TRAINREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x939300B0, get_ability_item_name_without_world(SONIC, TRAINREGION, GLIDE), ItemClassification.progression),
    ItemData(0x939300B1, get_ability_item_name_without_world(SONIC, TRAINREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x939300B2, get_ability_item_name_without_world(SONIC, TRAINREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x939300C0, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x939300C1, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, TORNADO), ItemClassification.progression),
    ItemData(0x939300C2, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x939300C3, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x939300C4, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x939300C5, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x939300C6, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x939300C7, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x939300C8, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x939300C9, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x939300CA, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x939300CB, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x939300CC, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x939300CD, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x939300CE, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x939300CF, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x939300D0, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, GLIDE), ItemClassification.progression),
    ItemData(0x939300D1, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x939300D2, get_ability_item_name_without_world(SONIC, BIGPLANTREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x939300E0, get_ability_item_name_without_world(SONIC, GHOSTREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x939300E1, get_ability_item_name_without_world(SONIC, GHOSTREGION, TORNADO), ItemClassification.progression),
    ItemData(0x939300E2, get_ability_item_name_without_world(SONIC, GHOSTREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x939300E3, get_ability_item_name_without_world(SONIC, GHOSTREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x939300E4, get_ability_item_name_without_world(SONIC, GHOSTREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x939300E5, get_ability_item_name_without_world(SONIC, GHOSTREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x939300E6, get_ability_item_name_without_world(SONIC, GHOSTREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x939300E7, get_ability_item_name_without_world(SONIC, GHOSTREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x939300E8, get_ability_item_name_without_world(SONIC, GHOSTREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x939300E9, get_ability_item_name_without_world(SONIC, GHOSTREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x939300EA, get_ability_item_name_without_world(SONIC, GHOSTREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x939300EB, get_ability_item_name_without_world(SONIC, GHOSTREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x939300EC, get_ability_item_name_without_world(SONIC, GHOSTREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x939300ED, get_ability_item_name_without_world(SONIC, GHOSTREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x939300EE, get_ability_item_name_without_world(SONIC, GHOSTREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x939300EF, get_ability_item_name_without_world(SONIC, GHOSTREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x939300F0, get_ability_item_name_without_world(SONIC, GHOSTREGION, GLIDE), ItemClassification.progression),
    ItemData(0x939300F1, get_ability_item_name_without_world(SONIC, GHOSTREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x939300F2, get_ability_item_name_without_world(SONIC, GHOSTREGION, BELLYFLOP), ItemClassification.progression),


    ItemData(0x93930100, get_ability_item_name_without_world(SONIC, SKYREGION, HOMINGATTACK), ItemClassification.progression),
    ItemData(0x93930101, get_ability_item_name_without_world(SONIC, SKYREGION, TORNADO), ItemClassification.progression),
    ItemData(0x93930102, get_ability_item_name_without_world(SONIC, SKYREGION, ROCKETACCEL), ItemClassification.progression),
    ItemData(0x93930103, get_ability_item_name_without_world(SONIC, SKYREGION, LIGHTDASH), ItemClassification.progression),
    ItemData(0x93930104, get_ability_item_name_without_world(SONIC, SKYREGION, TRIANGLEJUMP), ItemClassification.progression),
    ItemData(0x93930105, get_ability_item_name_without_world(SONIC, SKYREGION, LIGHTATTACK), ItemClassification.progression),
    ItemData(0x93930106, get_ability_item_name_without_world(SONIC, SKYREGION, AMYHAMMERHOVER), ItemClassification.progression),
    ItemData(0x93930107, get_ability_item_name_without_world(SONIC, SKYREGION, INVISIBILITY), ItemClassification.progression),
    ItemData(0x93930108, get_ability_item_name_without_world(SONIC, SKYREGION, SHURIKEN), ItemClassification.progression),
    ItemData(0x93930109, get_ability_item_name_without_world(SONIC, SKYREGION, THUNDERSHOOT), ItemClassification.progression),
    ItemData(0x9393010A, get_ability_item_name_without_world(SONIC, SKYREGION, FLIGHT), ItemClassification.progression),
    ItemData(0x9393010B, get_ability_item_name_without_world(SONIC, SKYREGION, DUMMYRINGS), ItemClassification.progression),
    ItemData(0x9393010C, get_ability_item_name_without_world(SONIC, SKYREGION, CHEESECANNON), ItemClassification.progression),
    ItemData(0x9393010D, get_ability_item_name_without_world(SONIC, SKYREGION, FLOWERSTING), ItemClassification.progression),
    ItemData(0x9393010E, get_ability_item_name_without_world(SONIC, SKYREGION, POWERATTACK), ItemClassification.progression),
    ItemData(0x9393010F, get_ability_item_name_without_world(SONIC, SKYREGION, COMBOFINISHER), ItemClassification.progression),
    ItemData(0x93930110, get_ability_item_name_without_world(SONIC, SKYREGION, GLIDE), ItemClassification.progression),
    ItemData(0x93930111, get_ability_item_name_without_world(SONIC, SKYREGION, FIREDUNK), ItemClassification.progression),
    ItemData(0x93930112, get_ability_item_name_without_world(SONIC, SKYREGION, BELLYFLOP), ItemClassification.progression),




    #ItemData(0x939300B0, char_levelup_to_item_name[SONIC][SPEED], ItemClassification.progression),
    #ItemData(0x939300B1, char_levelup_to_item_name[SONIC][FLYING], ItemClassification.progression),
    #ItemData(0x939300B2, char_levelup_to_item_name[SONIC][POWER], ItemClassification.progression),


    ItemData(0x93930600, EXTRALIFE, ItemClassification.filler),
    ItemData(0x93930601, RINGS5, ItemClassification.filler),
    ItemData(0x93930602, RINGS10, ItemClassification.filler),
    ItemData(0x93930603, RINGS20, ItemClassification.filler),
    ItemData(0x93930604, SHIELD, ItemClassification.filler),
    ItemData(0x93930605, INVINCIBILITY, ItemClassification.filler, fillerweight=0),
    #ItemData(0x93930606, SPEEDLEVELUP, ItemClassification.filler),
    #ItemData(0x93930607, FLYINGLEVELUP, ItemClassification.filler),
    #ItemData(0x93930608, POWERLEVELUP, ItemClassification.filler),
    #ItemData(0x93930609, TEAMLEVELUP, ItemClassification.filler, fillerweight=25),
    ItemData(0x9393060A, TEAMBLASTREFILL, ItemClassification.filler),

    ItemData(0x93930700, STEALTHTRAP, ItemClassification.trap),
    ItemData(0x93930701, FREEZETRAP, ItemClassification.trap),
    ItemData(0x93930702, NOSWAPTRAP, ItemClassification.trap),
    ItemData(0x93930703, RINGTRAP, ItemClassification.trap),
    ItemData(0x93930704, CHARMYTRAP, ItemClassification.trap),
]


filler_items_to_weights = \
    {item.name: item.fillerweight for item in itemList if item.classification == ItemClassification.filler}

trap_items_to_weights = \
    {item.name: item.fillerweight for item in itemList if item.classification == ItemClassification.trap}
