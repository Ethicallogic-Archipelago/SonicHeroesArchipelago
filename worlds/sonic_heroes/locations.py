from BaseClasses import Location



class SonicHeroesLocation(Location):
    game: str = "Sonic Heroes"

"""

def create_location(player: int, reg: Region, name: str, code: int):
    location = SonicHeroesLocation(player, name, code, reg)
    reg.locations.append(location)


def create_locations_from_dict(loc_dict, reg, player):
    for (key, data) in loc_dict.items():
        if data.region != reg.name:
            continue
        create_location(player, reg, key, data.code)



def create_locations(player: int, options: SonicHeroesOptions, region: Region):

    if options.sonic_story:
        create_locations_from_dict(stage_list_sonic, region, player)

    if options.dark_story:
        create_locations_from_dict(stage_list_dark, region, player)

    if options.rose_story:
        create_locations_from_dict(stage_list_rose, region, player)

    if options.chaotix_story:
        create_locations_from_dict(stage_list_chaotix, region, player)

    create_locations_from_dict(emerald_stage_list, region, player)

"""


sonic_mission_locs = [

    [
        {"Seaside Hill Sonic 1": 0x939300A0},
        {"Seaside Hill Sonic 2": 0x939300A1},
    ],
    [
        {"Ocean Palace Sonic 1": 0x939300A2},
        {"Ocean Palace Sonic 2": 0x939300A3},
    ],
    [
        {"Grand Metropolis Sonic 1": 0x939300A4},
        {"Grand Metropolis Sonic 2": 0x939300A5},
    ],
    [
        {"Power Plant Sonic 1": 0x939300A6},
        {"Power Plant Sonic 2": 0x939300A7},
    ],
    [
        {"Casino Park Sonic 1": 0x939300A9},
        {"Casino Park Sonic 2": 0x939300AA},
    ],
    [
        {"Bingo Highway Sonic 1": 0x939300AB},
        {"Bingo Highway Sonic 2": 0x939300AC},
    ],
    [
        {"Rail Canyon Sonic 1": 0x939300AE},
        {"Rail Canyon Sonic 2": 0x939300AF},
    ],
    [
        {"Bullet Station Sonic 1": 0x939300B0},
        {"Bullet Station Sonic 2": 0x939300B1},
    ],
    [
        {"Frog Forest Sonic 1": 0x939300B2},
        {"Frog Forest Sonic 2": 0x939300B3},
    ],
    [
        {"Lost Jungle Sonic 1": 0x939300B4},
        {"Lost Jungle Sonic 2": 0x939300B5},
    ],
    [
        {"Hang Castle Sonic 1": 0x939300B7},
        {"Hang Castle Sonic 2": 0x939300B8},
    ],
    [
        {"Mystic Mansion Sonic 1": 0x939300B9},
        {"Mystic Mansion Sonic 2": 0x939300BA},
    ],
    [
        {"Egg Fleet Sonic 1": 0x939300BC},
        {"Egg Fleet Sonic 2": 0x939300BD},
    ],
    [
        {"Final Fortress Sonic 1": 0x939300BE},
        {"Final Fortress Sonic 2": 0x939300BF},
    ],
    [
        {"Team Rose Fight Sonic": 0x939300A8},
    ],
    [
        {"Robot Carnival Sonic": 0x939300AD},
    ],
    [
        {"Team Dark Fight Sonic": 0x939300B6},
    ],
    [
        {"Robot Storm Sonic": 0x939300BB},
    ],

]


dark_mission_locs = [

    [
        {"Seaside Hill Dark 1": 0x939300C0},
        {"Seaside Hill Dark 2": 0x939300C1},
    ],
    [
        {"Ocean Palace Dark 1": 0x939300C2},
        {"Ocean Palace Dark 2": 0x939300C3},
    ],
    [
        {"Grand Metropolis Dark 1": 0x939300C4},
        {"Grand Metropolis Dark 2": 0x939300C5},
    ],
    [
        {"Power Plant Dark 1": 0x939300C6},
        {"Power Plant Dark 2": 0x939300C7},
    ],
    [
        {"Casino Park Dark 1": 0x939300C9},
        {"Casino Park Dark 2": 0x939300CA},
    ],
    [
        {"Bingo Highway Dark 1": 0x939300CB},
        {"Bingo Highway Dark 2": 0x939300CC},
    ],
    [
        {"Rail Canyon Dark 1": 0x939300CE},
        {"Rail Canyon Dark 2": 0x939300CF},
    ],
    [
        {"Bullet Station Dark 1": 0x939300D0},
        {"Bullet Station Dark 2": 0x939300D1},
    ],
    [
        {"Frog Forest Dark 1": 0x939300D2},
        {"Frog Forest Dark 2": 0x939300D3},
    ],
    [
        {"Lost Jungle Dark 1": 0x939300D4},
        {"Lost Jungle Dark 2": 0x939300D5},
    ],
    [
        {"Hang Castle Dark 1": 0x939300D7},
        {"Hang Castle Dark 2": 0x939300D8},
    ],
    [
        {"Mystic Mansion Dark 1": 0x939300D9},
        {"Mystic Mansion Dark 2": 0x939300DA},
    ],
    [
        {"Egg Fleet Dark 1": 0x939300DC},
        {"Egg Fleet Dark 2": 0x939300DD},
    ],
    [
        {"Final Fortress Dark 1": 0x939300DE},
        {"Final Fortress Dark 2": 0x939300DF},
    ],
    [
        {"Team Chaotix Fight Dark": 0x939300C8},
    ],
    [
        {"Robot Carnival Dark": 0x939300CD},
    ],
    [
        {"Team Sonic Fight Dark": 0x939300D6},
    ],
    [
        {"Robot Storm Dark": 0x939300DB},
    ],

]


rose_mission_locs = [

    [
        {"Seaside Hill Rose 1": 0x939300E0},
        {"Seaside Hill Rose 2": 0x939300E1},
    ],
    [
        {"Ocean Palace Rose 1": 0x939300E2},
        {"Ocean Palace Rose 2": 0x939300E3},
    ],
    [
        {"Grand Metropolis Rose 1": 0x939300E4},
        {"Grand Metropolis Rose 2": 0x939300E5},
    ],
    [
        {"Power Plant Rose 1": 0x939300E6},
        {"Power Plant Rose 2": 0x939300E7},
    ],
    [
        {"Casino Park Rose 1": 0x939300E9},
        {"Casino Park Rose 2": 0x939300EA},
    ],
    [
        {"Bingo Highway Rose 1": 0x939300EB},
        {"Bingo Highway Rose 2": 0x939300EC},
    ],
    [
        {"Rail Canyon Rose 1": 0x939300EE},
        {"Rail Canyon Rose 2": 0x939300EF},
    ],
    [
        {"Bullet Station Rose 1": 0x939300F0},
        {"Bullet Station Rose 2": 0x939300F1},
    ],
    [
        {"Frog Forest Rose 1": 0x939300F2},
        {"Frog Forest Rose 2": 0x939300F3},
    ],
    [
        {"Lost Jungle Rose 1": 0x939300F4},
        {"Lost Jungle Rose 2": 0x939300F5},
    ],
    [
        {"Hang Castle Rose 1": 0x939300F7},
        {"Hang Castle Rose 2": 0x939300F8},
    ],
    [
        {"Mystic Mansion Rose 1": 0x939300F9},
        {"Mystic Mansion Rose 2": 0x939300FA},
    ],
    [
        {"Egg Fleet Rose 1": 0x939300FC},
        {"Egg Fleet Rose 2": 0x939300FD},
    ],
    [
        {"Final Fortress Rose 1": 0x939300FE},
        {"Final Fortress Rose 2": 0x939300FF},
    ],
    [
        {"Team Sonic Fight Rose": 0x939300E8},
    ],
    [
        {"Robot Carnival Rose": 0x939300ED},
    ],
    [
        {"Team Chaotix Fight Rose": 0x939300F6},
    ],
    [
        {"Robot Storm Rose": 0x939300FB},
    ],

]


chaotix_mission_locs = [

    [
        {"Seaside Hill Chaotix 1": 0x93930100},
        {"Seaside Hill Chaotix 2": 0x93930101},
    ],
    [
        {"Ocean Palace Chaotix 1": 0x93930102},
        {"Ocean Palace Chaotix 2": 0x93930103},
    ],
    [
        {"Grand Metropolis Chaotix 1": 0x93930104},
        {"Grand Metropolis Chaotix 2": 0x93930105},
    ],
    [
        {"Power Plant Chaotix 1": 0x93930106},
        {"Power Plant Chaotix 2": 0x93930107},
    ],
    [
        {"Casino Park Chaotix 1": 0x93930109},
        {"Casino Park Chaotix 2": 0x9393010A},
    ],
    [
        {"Bingo Highway Chaotix 1": 0x9393010B},
        {"Bingo Highway Chaotix 2": 0x9393010C},
    ],
    [
        {"Rail Canyon Chaotix 1": 0x9393010E},
        {"Rail Canyon Chaotix 2": 0x9393010F},
    ],
    [
        {"Bullet Station Chaotix 1": 0x93930110},
        {"Bullet Station Chaotix 2": 0x93930111},
    ],
    [
        {"Frog Forest Chaotix 1": 0x93930112},
        {"Frog Forest Chaotix 2": 0x93930113},
    ],
    [
        {"Lost Jungle Chaotix 1": 0x93930114},
        {"Lost Jungle Chaotix 2": 0x93930115},
    ],
    [
        {"Hang Castle Chaotix 1": 0x93930117},
        {"Hang Castle Chaotix 2": 0x93930118},
    ],
    [
        {"Mystic Mansion Chaotix 1": 0x93930119},
        {"Mystic Mansion Chaotix 2": 0x9393011A},
    ],
    [
        {"Egg Fleet Chaotix 1": 0x9393011C},
        {"Egg Fleet Chaotix 2": 0x9393011D},
    ],
    [
        {"Final Fortress Chaotix 1": 0x9393011E},
        {"Final Fortress Chaotix 2": 0x9393011F},
    ],
    [
        {"Team Dark Fight Chaotix": 0x93930108},
    ],
    [
        {"Robot Carnival Chaotix": 0x9393010D},
    ],
    [
        {"Team Rose Fight Chaotix": 0x93930116},
    ],
    [
        {"Robot Storm Chaotix": 0x9393011B},
    ],

]


emerald_locs = [
    [
        {"Ocean Palace Emerald Stage": 0x93930120},
    ],
    [
        {"Power Plant Emerald Stage": 0x93930121},
    ],
    [
        {"Bingo Highway Emerald Stage": 0x93930122},
    ],
    [
        {"Bullet Station Emerald Stage": 0x93930123},
    ],
    [
        {"Lost Jungle Emerald Stage": 0x93930124},
    ],
    [
        {"Mystic Mansion Emerald Stage": 0x93930125},
    ],
    [
        {"Final Fortress Emerald Stage": 0x93930126},
    ],
]

sonic_boss_locs = [
    [
        {"Egg Hawk Sonic": 0x9393012C},
    ],
    [
        {"Egg Albatross Sonic": 0x9393012D},
    ],
    [
        {"Egg Emperor Sonic": 0x9393012E},
    ],
]


dark_boss_locs = [
    [
        {"Egg Hawk Dark": 0x9393012F},
    ],
    [
        {"Egg Albatross Dark": 0x93930130},
    ],
    [
        {"Egg Emperor Dark": 0x93930131},
    ],
]


rose_boss_locs = [
    [
        {"Egg Hawk Rose": 0x93930132},
    ],
    [
        {"Egg Albatross Rose": 0x93930133},
    ],
    [
        {"Egg Emperor Rose": 0x93930134},
    ],
]


chaotix_boss_locs = [
    [
        {"Egg Hawk Chaotix": 0x93930135}, #0x93930135
    ],
    [
        {"Egg Albatross Chaotix": 0x93930136}, #0x93930136
    ],
    [
        {"Egg Emperor Chaotix": 0x93930137}, #0x93930137
    ],
]

goal_loc = [
    [
        {"Metal Madness": None},
    ],
]




tempdict = {}


for mission in sonic_mission_locs:
    for mission_loc in mission:
        tempdict |= mission_loc

for mission in dark_mission_locs:
    for mission_loc in mission:
        tempdict |= mission_loc

for mission in rose_mission_locs:
    for mission_loc in mission:
        tempdict |= mission_loc

for mission in chaotix_mission_locs:
    for mission_loc in mission:
        tempdict |= mission_loc

"""
for mission in *sonic_boss_locs:
    tempdict += *mission

for mission in *dark_boss_locs:
    tempdict += *mission

for mission in *rose_boss_locs:
    tempdict += *mission

for mission in *chaotix_boss_locs:
    tempdict += *mission
"""

for mission in emerald_locs:
    for mission_loc in mission:
        tempdict |= mission_loc

#print("location_name_to_id in locations is: " + str(tempdict))


location_name_to_id = tempdict


