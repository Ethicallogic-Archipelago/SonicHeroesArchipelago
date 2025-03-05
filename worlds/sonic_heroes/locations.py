from collections import namedtuple
from BaseClasses import Location



class SonicHeroesLocation(Location):
    game: str = "Sonic Heroes"


#use this in regions for Extras/TeamFights
ExtraTuple = namedtuple('ExtraTuple', ['name', 'loc_dict'])


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
        {"Casino Park Sonic 1": 0x939300A8},
        {"Casino Park Sonic 2": 0x939300A9},
    ],
    [
        {"Bingo Highway Sonic 1": 0x939300AA},
        {"Bingo Highway Sonic 2": 0x939300AB},
    ],
    [
        {"Rail Canyon Sonic 1": 0x939300AC},
        {"Rail Canyon Sonic 2": 0x939300AD},
    ],
    [
        {"Bullet Station Sonic 1": 0x939300AE},
        {"Bullet Station Sonic 2": 0x939300AF},
    ],
    [
        {"Frog Forest Sonic 1": 0x939300B0},
        {"Frog Forest Sonic 2": 0x939300B1},
    ],
    [
        {"Lost Jungle Sonic 1": 0x939300B2},
        {"Lost Jungle Sonic 2": 0x939300B3},
    ],
    [
        {"Hang Castle Sonic 1": 0x939300B4},
        {"Hang Castle Sonic 2": 0x939300B5},
    ],
    [
        {"Mystic Mansion Sonic 1": 0x939300B6},
        {"Mystic Mansion Sonic 2": 0x939300B7},
    ],
    [
        {"Egg Fleet Sonic 1": 0x939300B8},
        {"Egg Fleet Sonic 2": 0x939300B9},
    ],
    [
        {"Final Fortress Sonic 1": 0x939300BA},
        {"Final Fortress Sonic 2": 0x939300BB},
    ],
]


dark_mission_locs = [

    [
        {"Seaside Hill Dark 1": 0x939300CA},
        {"Seaside Hill Dark 2": 0x939300CB},
    ],
    [
        {"Ocean Palace Dark 1": 0x939300CC},
        {"Ocean Palace Dark 2": 0x939300CD},
    ],
    [
        {"Grand Metropolis Dark 1": 0x939300CE},
        {"Grand Metropolis Dark 2": 0x939300CF},
    ],
    [
        {"Power Plant Dark 1": 0x939300D0},
        {"Power Plant Dark 2": 0x939300D1},
    ],
    [
        {"Casino Park Dark 1": 0x939300D2},
        {"Casino Park Dark 2": 0x939300D3},
    ],
    [
        {"Bingo Highway Dark 1": 0x939300D4},
        {"Bingo Highway Dark 2": 0x939300D5},
    ],
    [
        {"Rail Canyon Dark 1": 0x939300D6},
        {"Rail Canyon Dark 2": 0x939300D7},
    ],
    [
        {"Bullet Station Dark 1": 0x939300D8},
        {"Bullet Station Dark 2": 0x939300D9},
    ],
    [
        {"Frog Forest Dark 1": 0x939300DA},
        {"Frog Forest Dark 2": 0x939300DB},
    ],
    [
        {"Lost Jungle Dark 1": 0x939300DC},
        {"Lost Jungle Dark 2": 0x939300DD},
    ],
    [
        {"Hang Castle Dark 1": 0x939300DE},
        {"Hang Castle Dark 2": 0x939300DF},
    ],
    [
        {"Mystic Mansion Dark 1": 0x939300E0},
        {"Mystic Mansion Dark 2": 0x939300E1},
    ],
    [
        {"Egg Fleet Dark 1": 0x939300E2},
        {"Egg Fleet Dark 2": 0x939300E3},
    ],
    [
        {"Final Fortress Dark 1": 0x939300E4},
        {"Final Fortress Dark 2": 0x939300E5},
    ],
]


rose_mission_locs = [

    [
        {"Seaside Hill Rose 1": 0x939300F4},
        {"Seaside Hill Rose 2": 0x939300F5},
    ],
    [
        {"Ocean Palace Rose 1": 0x939300F6},
        {"Ocean Palace Rose 2": 0x939300F7},
    ],
    [
        {"Grand Metropolis Rose 1": 0x939300F8},
        {"Grand Metropolis Rose 2": 0x939300F9},
    ],
    [
        {"Power Plant Rose 1": 0x939300FA},
        {"Power Plant Rose 2": 0x939300FB},
    ],
    [
        {"Casino Park Rose 1": 0x939300FC},
        {"Casino Park Rose 2": 0x939300FD},
    ],
    [
        {"Bingo Highway Rose 1": 0x939300FE},
        {"Bingo Highway Rose 2": 0x939300FF},
    ],
    [
        {"Rail Canyon Rose 1": 0x93930100},
        {"Rail Canyon Rose 2": 0x93930101},
    ],
    [
        {"Bullet Station Rose 1": 0x93930102},
        {"Bullet Station Rose 2": 0x93930103},
    ],
    [
        {"Frog Forest Rose 1": 0x93930104},
        {"Frog Forest Rose 2": 0x93930105},
    ],
    [
        {"Lost Jungle Rose 1": 0x93930106},
        {"Lost Jungle Rose 2": 0x93930107},
    ],
    [
        {"Hang Castle Rose 1": 0x93930108},
        {"Hang Castle Rose 2": 0x93930109},
    ],
    [
        {"Mystic Mansion Rose 1": 0x9393010A},
        {"Mystic Mansion Rose 2": 0x9393010B},
    ],
    [
        {"Egg Fleet Rose 1": 0x9393010C},
        {"Egg Fleet Rose 2": 0x9393010D},
    ],
    [
        {"Final Fortress Rose 1": 0x9393010E},
        {"Final Fortress Rose 2": 0x9393010F},
    ],
]


chaotix_mission_locs = [

    [
        {"Seaside Hill Chaotix 1": 0x9393011E},
        {"Seaside Hill Chaotix 2": 0x9393011F},
    ],
    [
        {"Ocean Palace Chaotix 1": 0x93930120},
        {"Ocean Palace Chaotix 2": 0x93930121},
    ],
    [
        {"Grand Metropolis Chaotix 1": 0x93930122},
        {"Grand Metropolis Chaotix 2": 0x93930123},
    ],
    [
        {"Power Plant Chaotix 1": 0x93930124},
        {"Power Plant Chaotix 2": 0x93930125},
    ],
    [
        {"Casino Park Chaotix 1": 0x93930126},
        {"Casino Park Chaotix 2": 0x93930127},
    ],
    [
        {"Bingo Highway Chaotix 1": 0x93930128},
        {"Bingo Highway Chaotix 2": 0x93930129},
    ],
    [
        {"Rail Canyon Chaotix 1": 0x9393012A},
        {"Rail Canyon Chaotix 2": 0x9393012B},
    ],
    [
        {"Bullet Station Chaotix 1": 0x9393012C},
        {"Bullet Station Chaotix 2": 0x9393012D},
    ],
    [
        {"Frog Forest Chaotix 1": 0x9393012E},
        {"Frog Forest Chaotix 2": 0x9393012F},
    ],
    [
        {"Lost Jungle Chaotix 1": 0x93930130},
        {"Lost Jungle Chaotix 2": 0x93930131},
    ],
    [
        {"Hang Castle Chaotix 1": 0x93930132},
        {"Hang Castle Chaotix 2": 0x93930133},
    ],
    [
        {"Mystic Mansion Chaotix 1": 0x93930134},
        {"Mystic Mansion Chaotix 2": 0x93930135},
    ],
    [
        {"Egg Fleet Chaotix 1": 0x93930136},
        {"Egg Fleet Chaotix 2": 0x93930137},
    ],
    [
        {"Final Fortress Chaotix 1": 0x93930138},
        {"Final Fortress Chaotix 2": 0x93930139},
    ],
]


emerald_locs = [
    [
        {"Ocean Palace Emerald Stage": 0x93930148},
    ],
    [
        {"Power Plant Emerald Stage": 0x93930149},
    ],
    [
        {"Bingo Highway Emerald Stage": 0x9393014A},
    ],
    [
        {"Bullet Station Emerald Stage": 0x9393014B},
    ],
    [
        {"Lost Jungle Emerald Stage": 0x9393014C},
    ],
    [
        {"Mystic Mansion Emerald Stage": 0x9393014D},
    ],
    [
        {"Final Fortress Emerald Stage": 0x9393014E},
    ],
]



boss_gate_locs = [
    [
        {"Boss Gate 1": 0x9393014F},
    ],
    [
        {"Boss Gate 2": 0x93930150},
    ],
    [
        {"Boss Gate 3": 0x93930151},
    ],
    [
        {"Boss Gate 4": 0x93930152},
    ],
    [
        {"Boss Gate 5": 0x93930153},
    ],
]



egg_hawk_locs = [
    [
        {"Egg Hawk Sonic": 0x939300BC},
    ],
    [
        {"Egg Hawk Dark": 0x939300E6},
    ],
    [
        {"Egg Hawk Rose": 0x93930110},
    ],
    [
        {"Egg Hawk Chaotix": 0x9393013A},
    ],
]



team_fight_1_locs = [
    [
        {"Team Rose Fight Sonic": 0x939300BE},
    ],
    [
        {"Team Chaotix Fight Dark": 0x939300E8},
    ],
    [
        {"Team Sonic Fight Rose": 0x93930112},
    ],
    [
        {"Team Dark Fight Chaotix": 0x9393013C},
    ],
]

robot_carnival_locs = [
    [
        {"Robot Carnival Sonic": 0x939300C0},
    ],
    [
        {"Robot Carnival Dark": 0x939300EA},
    ],
    [
        {"Robot Carnival Rose": 0x93930114},
    ],
    [
        {"Robot Carnival Chaotix": 0x9393013E},
    ],
]

egg_albatross_locs = [
    [
        {"Egg Albatross Sonic": 0x939300C2},
    ],
    [
        {"Egg Albatross Dark": 0x939300EC},
    ],
    [
        {"Egg Albatross Rose": 0x93930116},
    ],
    [
        {"Egg Albatross Chaotix": 0x93930140},
    ],
]


team_fight_2_locs = [
    [
        {"Team Dark Fight Sonic": 0x939300C4},
    ],
    [
        {"Team Sonic Fight Dark": 0x939300EE},
    ],
    [
        {"Team Chaotix Fight Rose": 0x93930118},
    ],
    [
        {"Team Rose Fight Chaotix": 0x93930142},
    ],
]


robot_storm_locs = [
    [
        {"Robot Storm Sonic": 0x939300C6},
    ],
    [
        {"Robot Storm Dark": 0x939300F0},
    ],
    [
        {"Robot Storm Rose": 0x9393011A},
    ],
    [
        {"Robot Storm Chaotix": 0x93930144},
    ],
]


egg_emperor_locs = [
    [
        {"Egg Emperor Sonic": 0x939300C8},
    ],
    [
        {"Egg Emperor Dark": 0x939300F2},
    ],
    [
        {"Egg Emperor Rose": 0x9393011C},
    ],
    [
        {"Egg Emperor Chaotix": 0x93930146},
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

for boss in egg_hawk_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in team_fight_1_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in robot_carnival_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in egg_albatross_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in team_fight_2_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in robot_storm_locs:
    for boss_loc in boss:
        tempdict |= boss_loc

for boss in egg_emperor_locs:
    for boss_loc in boss:
        tempdict |= boss_loc


for mission in emerald_locs:
    for mission_loc in mission:
        tempdict |= mission_loc


location_name_to_id = tempdict


