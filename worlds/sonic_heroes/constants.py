from __future__ import annotations
import typing
from dataclasses import dataclass
from BaseClasses import CollectionState, ItemClassification

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld


#from .sanity import *
#from .sanitykey import *


@dataclass
class ItemData:
    code: int
    name: str
    classification: ItemClassification = ItemClassification.useful
    amount: int = 1
    fillerweight: int = 50

"""
@dataclass
class LocationData:
    #optionNeeded: str
    #consider list of str for multiple
    #optionValue: set[int]
    #consider list of set[int] for multiple
    name: str
    code: int
    team: str
    level: str
    region: str
    rule: CollectionState
    rulestr: str

    def __lt__(self, other):
        return self.code < other.code


@dataclass
class EntranceData:
    name: str
    sourceReg: str
    targetReg: str
    rule: CollectionState = None


@dataclass
class RegionData:
    name: str
    numberofObjChecks: int
    
"""


@dataclass
class RegionCSVData:
    team: str
    level: str
    name: str
    objchecks: int


@dataclass
class ConnectionCSVData:
    name: str
    team: str
    level: str
    source: str
    target: str
    #rule: CollectionState
    rulestr: str

@dataclass
class LocationCSVData:
    name: str
    code: int
    team: str
    level: str
    act: int
    region: str
    rulestr: str
    #rule: CollectionState
    loc_type: str
    hint_info: str
    notes: str


    def __lt__(self, other):
        return self.code < other.code



#class StrConst:
SONICHEROES = "Sonic Heroes"
PARTYTIMETHEME = "partyTime"
AND = "And"

TUTORIALNAME = "Multiworld Setup Guide"
TUTORIALDESC = "A guide to setting up the Sonic Heroes randomizer connected to an Archipelago Multiworld."
TUTORIALLANGUAGE = "English"
TUTORIALFILENAME = "setup_en.md"
TUTORIALLINK = "setup/en"
TUTORIALAUTHORS = ["EthicalLogic"]


SONIC = "Sonic"
DARK = "Dark"
ROSE = "Rose"
CHAOTIX = "Chaotix"
SUPERHARD = "SuperHard"

ANYTEAM = "Any Team"

SPEED = "Speed"
FLYING = "Flying"
POWER = "Power"
PROGRESSIVE = "Progressive"
PROGRESSIVELEVELUP = f"{PROGRESSIVE} Level-Up"
TWOCHARACTERS = "2 Characters"
THREECHARACTERS = "3 Characters"

PLAYABLE = "Playable"
CHARSONIC = "Sonic"
CHARTAILS = "Tails"
CHARKNUCKLES = "Knuckles"
CHARSHADOW = "Shadow"
CHARROUGE = "Rouge"
CHAROMEGA = "Omega"
CHARAMY = "Amy"
CHARCREAM = "Cream"
CHARBIG = "Big"
CHARESPIO = "Espio"
CHARCHARMY = "Charmy"
CHARVECTOR = "Vector"
CHARSUPERHARDSONIC = "SuperHard Sonic"
CHARSUPERHARDTAILS = "SuperHard Tails"
CHARSUPERHARDKNUCKLES = "SuperHard Knuckles"

SEASIDEHILL = "Seaside Hill"
OCEANPALACE = "Ocean Palace"
GRANDMETROPOLIS = "Grand Metropolis"
POWERPLANT = "Power Plant"
CASINOPARK = "Casino Park"
BINGOHIGHWAY = "Bingo Highway"
RAILCANYON = "Rail Canyon"
BULLETSTATION = "Bullet Station"
FROGFOREST = "Frog Forest"
LOSTJUNGLE = "Lost Jungle"
HANGCASTLE = "Hang Castle"
MYSTICMANSION = "Mystic Mansion"
EGGFLEET = "Egg Fleet"
FINALFORTRESS = "Final Fortress"
EGGHAWK = "Egg Hawk"
TEAMFIGHT1 = "Team Fight 1"
ROBOTCARNIVAL = "Robot Carnival"
EGGALBATROSS = "Egg Albatross"
TEAMFIGHT2 = "Team Fight 2"
ROBOTSTORM = "Robot Storm"
EGGEMPEROR = "Egg Emperor"
METALMADNESS = "Metal Madness"
METALOVERLORD = "Metal Overlord"

OCEANREGION = "Ocean Region"
HOTPLANTREGION = "HotPlant Region"
CASINOREGION = "Casino Region"
TRAINREGION = "Train Region"
BIGPLANTREGION = "BigPlant Region"
GHOSTREGION = "Ghost Region"
SKYREGION = "Sky Region"
SPECIALSTAGEREGION = "Special Stage Region"
BOSSREGION = "Boss Region"
FINALBOSSREGION = "Final Boss Region"

EMBLEM = "Emblem"
GREEN = "Green"
BLUE = "Blue"
YELLOW = "Yellow"
WHITE = "White"
CYAN = "Cyan"
PURPLE = "Purple"
RED = "Red"
CHAOSEMERALD = "Chaos Emerald"
GREENCHAOSEMERALD = f"{GREEN} {CHAOSEMERALD}"
BLUECHAOSEMERALD = f"{BLUE} {CHAOSEMERALD}"
YELLOWCHAOSEMERALD = f"{YELLOW} {CHAOSEMERALD}"
WHITECHAOSEMERALD = f"{WHITE} {CHAOSEMERALD}"
CYANCHAOSEMERALD = f"{CYAN} {CHAOSEMERALD}"
PURPLECHAOSEMERALD = f"{PURPLE} {CHAOSEMERALD}"
REDCHAOSEMERALD = f"{RED} {CHAOSEMERALD}"


emeralds = \
[
    GREENCHAOSEMERALD,
    BLUECHAOSEMERALD,
    YELLOWCHAOSEMERALD,
    WHITECHAOSEMERALD,
    CYANCHAOSEMERALD,
    PURPLECHAOSEMERALD,
    REDCHAOSEMERALD,
]

CHECKPOINT = "Checkpoint"
BONUSKEY = "Bonus Key"


PLAYABLESONIC = f"{PLAYABLE} {CHARSONIC}"
PLAYABLETAILS = f"{PLAYABLE} {CHARTAILS}"
PLAYABLEKNUCKLES = f"{PLAYABLE} {CHARKNUCKLES}"
PLAYABLESHADOW = f"{PLAYABLE} {CHARSHADOW}"
PLAYABLEROUGE = f"{PLAYABLE} {CHARROUGE}"
PLAYABLEOMEGA = f"{PLAYABLE} {CHAROMEGA}"
PLAYABLEAMY = f"{PLAYABLE} {CHARAMY}"
PLAYABLECREAM = f"{PLAYABLE} {CHARCREAM}"
PLAYABLEBIG = f"{PLAYABLE} {CHARBIG}"
PLAYABLEESPIO = f"{PLAYABLE} {CHARESPIO}"
PLAYABLECHARMY = f"{PLAYABLE} {CHARCHARMY}"
PLAYABLEVECTOR = f"{PLAYABLE} {CHARVECTOR}"
PLAYABLESUPERHARDSONIC = f"{PLAYABLE} {CHARSUPERHARDSONIC}"
PLAYABLESUPERHARDTAILS = f"{PLAYABLE} {CHARSUPERHARDTAILS}"
PLAYABLESUPERHARDKNUCKLES = f"{PLAYABLE} {CHARSUPERHARDKNUCKLES}"



EXTRALIFE = "Extra Life"
RINGS5 = "5 Ring Bundle"
RINGS10 = "10 Ring Bundle"
RINGS20 = "20 Ring Bundle"
SHIELD = "Shield"
INVINCIBILITY = "Invincibility"
SPEEDLEVELUP = "Speed Level Up"
POWERLEVELUP = "Power Level Up"
FLYINGLEVELUP = "Flying Level Up"
TEAMLEVELUP = "Team Level Up"
TEAMBLASTREFILL = "Team Blast Refill"

STEALTHTRAP = "Stealth Trap"
FREEZETRAP = "Freeze Trap"
NOSWAPTRAP = "No Swap Trap"
RINGTRAP = "Ring Trap"
CHARMYTRAP = "Charmy Trap"

MENU = "Menu"
MENUREGIONHINT = "This is Menu Region"
METALMADNESSREGIONHINT = "This is Metal Madness Region"
VICTORY = "Victory"
VICTORYITEM = f"{VICTORY} Item"
VICTORYLOCATION = f"{VICTORY} Location"

GOALUNLOCKITEM = "Goal Unlock Item"


NOTHING = "Nothing"
AMYHAMMERHOVER = "Amy Hammer Hover"
HOMINGATTACK = "Homing Attack"
TORNADO = "Tornado"
ROCKETACCEL = "Rocket Accel"
LIGHTDASH = "Light Dash"
TRIANGLEJUMP = "Triangle Jump"
LIGHTATTACK = "Light Attack"
INVISIBILITY = "Invisibility"
SHURIKEN = "Shuriken"

DUMMYRINGS = "Dummy Rings"
CHEESECANNON = "Cheese Cannon"
THUNDERSHOOT = "Thunder Shoot"
FLIGHT = "Flight"
FLOWERSTING = "Flower Sting"
FLYINGCHARACTERSPECIALMOVE = "Flying Character Special Move"

POWERATTACK = "Power Attack"
BREAK = "Break"
BELLYFLOP = "Belly Flop"
BREAKKEYCAGE = "Break Key Cage"
FIREDUNK = "Fire Dunk"
SLAM = "Slam"
ULTIMATEFIREDUNK = "Ultimate Fire Dunk"
#SLAM = "Slam"
GLIDE = "Glide"
TRIANGLEDIVE = "Triangle Dive"
COMBOFINISHER = "Combo Finisher"


ALLABILITIES = "All Abilities"

TEAMBLAST = "Team Blast"
GROUNDENEMY = "Ground Enemy"


SECRET = "Secret"
LOCATION = "Location"
LOCATIONS = "Locations"
SECRETLOCATIONS = f"{SECRET} {LOCATIONS}"
REGION = "Region"
REGIONS = "Regions"
ALLREGIONS = ""
CONNECTION = "Connection"
CONNECTIONS = "Connections"
SECRETREGION = f"{SECRET} {REGION}"
SECRETCONNECTION = f"{SECRET} {CONNECTION}"

TEAM = "Team"
LEVEL = "Level"
NAME = "Name"
CODE = "Code"
RULE = "Rule"
ACT = "Act"
SOURCE = "Source"
TARGET = "Target"
NOTES = "Notes"
OBJCHECKS = "ObjChecks"
LOCATIONTYPE = "Location Type"
HINTINFO = "Hint Info"




ALLSTAGEOBJS = "All Stage Objects"
SINGLESPRING = "Single Spring"
TRIPLESPRING = "Triple Spring"
RINGS = "Rings"
HINTRING = "Hint Ring"
REGULARSWITCH = "Regular Switch"
PUSHANDPULLSWITCH = "Push And Pull Switch"
TARGETSWITCH = "Target Switch"
DASHPANEL = "Dash Panel"
DASHRING = "Dash Ring"
RAINBOWHOOPS = "Rainbow Hoops"
CHECKPOINT = "Checkpoint"
DASHRAMP = "Dash Ramp"
CANNON = "Cannon"
REGULARWEIGHT = "Regular Weight"
BREAKABLEWEIGHT = "Breakable Weight"
ITEMBOX = "Item Box"
ITEMBALLOON = "Item Balloon"
GOALRING = "Goal Ring"
PULLEY = "Pulley"
WOODCONTAINER = "Wood Container"
IRONCONTAINER = "Iron Container"
UNBREAKABLECONTAINER = "Unbreakable Container"
CHAO = "Chao"
PROPELLER = "Propeller"
POLE = "Pole"
GONG = "Gong"
FAN = "Fan"
WARPFLOWER = "Warpflower"
BONUSKEY = "Bonus Key"
TELEPORTTRIGGER = "Teleport Trigger"
CEMENTBLOCKONRAILS = "Cement Block On Rails"
CEMENTSLIDINGBLOCK = "Cement Sliding Block"
CEMENTBLOCK = "Cement Block"
MOVINGRUINPLATFORM = "Moving Ruin Platform"
HERMITCRAB = "Hermit Crab"
SMALLSTONEPLATFORM = "Small Stone Platform"
CRUMBLINGSTONEPILLAR = "Crumbling Stone Pillar"
ENERGYROADSECTION = "Energy Road Section"
FALLINGDRAWBRIDGE = "Falling Drawbridge"
TILTINGBRIDGE = "Tilting Bridge"
BLIMPPLATFORM = "Blimp Platform"
ENERGYROADSPEEDEFFECT = "Energy Road Speed Effect"
ENERGYROADUPWARDSECTION = "Energy Road Upward Section"
ENERGYCOLUMN = "Energy Column"
ELEVATOR = "Elevator"
LAVAPLATFORM = "Lava Platform"
LIQUIDLAVA = "Liquid Lava"
ENERGYROADUPWARDEFFECT = "Energy Road Upward Effect"
SMALLBUMPER = "Small Bumper"
GREENFLOATINGBUMPER = "Green Floating Bumper"
PINBALLFLIPPER = "Pinball Flipper"
SMALLTRIANGLEBUMPER = "Small Triangle Bumper"
STARGLASSPANEL = "Star Glass Panel"
STARGLASSAIRPANEL = "Star Glass Air Panel"
LARGETRIANGLEBUMPER = "Large Triangle Bumper"
BREAKABLEGLASSFLOOR = "Breakable Glass Floor"
FLOATINGDICE = "Floating Dice"
TRIPLESLOTS = "Triple Slots"
SINGLESLOTS = "Single Slots"
BINGOCHART = "Bingo Chart"
BINGOCHIP = "Bingo Chip"
DASHARROW = "Dash Arrow"
POTATOCHIP = "Potato Chip"
SWITCHABLERAIL = "Switchable Rail"
RAILSWITCH = "Rail Switch"
SWITCHABLEARROW = "Switchable Arrow"
RAILBOOSTER = "Rail Booster"
RAILCROSSINGROADBLOCK = "Rail Crossing Roadblock"
CAPSULE = "Capsule"
RAILPLATFORM = "Rail Platform"
TRAINTRAIN = "Train Train"
ENGINECORE = "Engine Core"
BIGGUNINTERIOR = "Big Gun Interior"
BARREL = "Barrel"
CANYONBRIDGE = "Canyon Bridge"
TRAINTOP = "Train Top"
GREENFROG = "Green Frog"
SMALLGREENRAINPLATFORM = "Small Green Rain Platform"
SMALLBOUNCYMUSHROOM = "Small Bouncy Mushroom"
TALLVERTICALVINE = "Tall Vertical Vine"
TALLTREEWITHPLATFORMS = "Tall Tree With Platforms"
GRINDABLEGROWINGIVY = "Grindable Growing Ivy"
LARGEYELLOWPLATFORM = "Large Yellow Platform"
BOUNCYFRUIT = "Bouncy Fruit"
BIGBOUNCYMUSHROOM = "Big Bouncy Mushroom"
SWINGINGVINE = "Swinging Vine"
BLACKFROG = "Black Frog"
BOUNCYFALLINGFRUIT = "Bouncy Falling Fruit"
TELEPORTERSWITCH = "Teleporter Switch"
CASTLEFLOATINGPLATFORM = "Castle Floating Platform"
FLAMETORCH = "Flame Torch"
PUMPKINGHOST = "Pumpkin Ghost"
MANSIONFLOATINGPLATFORM = "Mansion Floating Platform"
CASTLEKEY = "Castle Key"
RECTANGULARFLOATINGPLATFORM = "Rectangular Floating Platform"
SQUAREFLOATINGPLATFORM = "Square Floating Platform"
FALLINGPLATFORM = "Falling Platform"
SELFDESTRUCTSWITCH = "Self Destruct Switch"
EGGMANCELLKEY = "Eggman Cell Key"
EGGFLAPPER = "Egg Flapper"
EGGPAWN = "Egg Pawn"
KLAGEN = "Klagen"
FALCO = "Falco"
EGGHAMMER = "Egg Hammer"
CAMERON = "Cameron"
RHINOLINER = "Rhino Liner"
EGGBISHOP = "Egg Bishop"
E2000 = "E2000"
SPECIALSTAGEORBS = "Special Stage Orbs"
APPEARCHAOSEMERALD = "Appear Chaos Emerald"
SPECIALSTAGESPRING = "Special Stage Spring"
SPECIALSTAGEDASHPANEL = "Special Stage Dash Panel"
SPECIALSTAGEDASHRING = "Special Stage Dash Ring"








team_char_names = \
{
    SONIC:
        [
            CHARSONIC,
            CHARTAILS,
            CHARKNUCKLES,
        ]
}


char_name_to_formation = \
{
    CHARSONIC: SPEED,
    CHARTAILS: FLYING,
    CHARKNUCKLES: POWER,
}


csv_file_headers = \
{
    REGION:
        [
            TEAM,
            LEVEL,
            NAME,
            OBJCHECKS
        ],

    CONNECTION:
        [
            TEAM,
            LEVEL,
            SOURCE,
            TARGET,
            RULE,
            NOTES
        ],
    LOCATION:
        [
            TEAM,
            LEVEL,
            NAME,
            CODE,
            ACT,
            REGION,
            RULE,
            LOCATIONTYPE,
            HINTINFO,
            NOTES
        ]
}



sonic_heroes_story_names: dict[int, str] = \
{
    0: SONIC,
    1: DARK,
    2: ROSE,
    3: CHAOTIX,
    4: SUPERHARD,
}

sonic_heroes_level_names: dict[int, str] = \
{
    1: SEASIDEHILL,
    2: OCEANPALACE,
    3: GRANDMETROPOLIS,
    4: POWERPLANT,
    5: CASINOPARK,
    6: BINGOHIGHWAY,
    7: RAILCANYON,
    8: BULLETSTATION,
    9: FROGFOREST,
    10: LOSTJUNGLE,
    11: HANGCASTLE,
    12: MYSTICMANSION,
    13: EGGFLEET,
    14: FINALFORTRESS,
}

sonic_heroes_extra_names: dict[int, str] = \
{
    0: EGGHAWK,
    1: TEAMFIGHT1,
    2: ROBOTCARNIVAL,
    3: EGGALBATROSS,
    4: TEAMFIGHT2,
    5: ROBOTSTORM,
    6: EGGEMPEROR,
}


item_teams = \
[
    ANYTEAM,
    SONIC,
    DARK,
    ROSE,
    CHAOTIX,
    SUPERHARD,
]

item_regions = \
[
    ALLREGIONS,
    OCEANREGION,
    HOTPLANTREGION,
    CASINOREGION,
    TRAINREGION,
    BIGPLANTREGION,
    GHOSTREGION,
    SKYREGION,
    SPECIALSTAGEREGION,
    BOSSREGION,
    FINALBOSSREGION,
]

item_abilities = \
[
    ALLABILITIES,
    HOMINGATTACK,
    TORNADO,
    ROCKETACCEL,
    LIGHTDASH,
    TRIANGLEJUMP,
    LIGHTATTACK,
    AMYHAMMERHOVER,
    INVISIBILITY,
    SHURIKEN,
    THUNDERSHOOT,
    FLIGHT,
    DUMMYRINGS,
    CHEESECANNON,
    FLOWERSTING,
    POWERATTACK,
    COMBOFINISHER,
    GLIDE,
    FIREDUNK,
    BELLYFLOP,
]

stage_objs = \
[
ALLSTAGEOBJS,
SINGLESPRING,
TRIPLESPRING,
RINGS,
HINTRING,
REGULARSWITCH,
PUSHANDPULLSWITCH,
TARGETSWITCH,
DASHPANEL,
DASHRING,
RAINBOWHOOPS,
CHECKPOINT,
DASHRAMP,
CANNON,
REGULARWEIGHT,
BREAKABLEWEIGHT,
ITEMBOX,
ITEMBALLOON,
GOALRING,
PULLEY,
WOODCONTAINER,
IRONCONTAINER,
UNBREAKABLECONTAINER,
CHAO,
PROPELLER,
POLE,
GONG,
FAN,
WARPFLOWER,
BONUSKEY,
TELEPORTTRIGGER,
CEMENTBLOCKONRAILS,
CEMENTSLIDINGBLOCK,
CEMENTBLOCK,
MOVINGRUINPLATFORM,
HERMITCRAB,
SMALLSTONEPLATFORM,
CRUMBLINGSTONEPILLAR,
ENERGYROADSECTION,
FALLINGDRAWBRIDGE,
TILTINGBRIDGE,
BLIMPPLATFORM,
ENERGYROADSPEEDEFFECT,
ENERGYROADUPWARDSECTION,
ENERGYCOLUMN,
ELEVATOR,
LAVAPLATFORM,
LIQUIDLAVA,
ENERGYROADUPWARDEFFECT,
SMALLBUMPER,
GREENFLOATINGBUMPER,
PINBALLFLIPPER,
SMALLTRIANGLEBUMPER,
STARGLASSPANEL,
STARGLASSAIRPANEL,
LARGETRIANGLEBUMPER,
BREAKABLEGLASSFLOOR,
FLOATINGDICE,
TRIPLESLOTS,
SINGLESLOTS,
BINGOCHART,
BINGOCHIP,
DASHARROW,
POTATOCHIP,
SWITCHABLERAIL,
RAILSWITCH,
SWITCHABLEARROW,
RAILBOOSTER,
RAILCROSSINGROADBLOCK,
CAPSULE,
RAILPLATFORM,
TRAINTRAIN,
ENGINECORE,
BIGGUNINTERIOR,
BARREL,
CANYONBRIDGE,
TRAINTOP,
GREENFROG,
SMALLGREENRAINPLATFORM,
SMALLBOUNCYMUSHROOM,
TALLVERTICALVINE,
TALLTREEWITHPLATFORMS,
GRINDABLEGROWINGIVY,
LARGEYELLOWPLATFORM,
BOUNCYFRUIT,
BIGBOUNCYMUSHROOM,
SWINGINGVINE,
BLACKFROG,
BOUNCYFALLINGFRUIT,
TELEPORTERSWITCH,
CASTLEFLOATINGPLATFORM,
FLAMETORCH,
PUMPKINGHOST,
MANSIONFLOATINGPLATFORM,
CASTLEKEY,
RECTANGULARFLOATINGPLATFORM,
SQUAREFLOATINGPLATFORM,
FALLINGPLATFORM,
SELFDESTRUCTSWITCH,
EGGMANCELLKEY,
EGGFLAPPER,
EGGPAWN,
KLAGEN,
FALCO,
EGGHAMMER,
CAMERON,
RHINOLINER,
EGGBISHOP,
E2000,
SPECIALSTAGEORBS,
APPEARCHAOSEMERALD,
SPECIALSTAGESPRING,
SPECIALSTAGEDASHPANEL,
SPECIALSTAGEDASHRING,
]


level_to_game_region: dict[str, str] = \
{
    SEASIDEHILL: OCEANREGION,
    OCEANPALACE: OCEANREGION,
    GRANDMETROPOLIS: HOTPLANTREGION,
    POWERPLANT: HOTPLANTREGION,
    CASINOPARK: CASINOREGION,
    BINGOHIGHWAY: CASINOREGION,
    RAILCANYON: TRAINREGION,
    BULLETSTATION: TRAINREGION,
    FROGFOREST: BIGPLANTREGION,
    LOSTJUNGLE: BIGPLANTREGION,
    HANGCASTLE: GHOSTREGION,
    MYSTICMANSION: GHOSTREGION,
    EGGFLEET: SKYREGION,
    FINALFORTRESS: SKYREGION,
}

game_region_to_level: dict[str, list[str]] = \
{
    OCEANREGION:
        [
            SEASIDEHILL,
            OCEANPALACE
        ],
    HOTPLANTREGION:
        [
            GRANDMETROPOLIS,
            POWERPLANT,
        ],
    CASINOREGION:
        [
            CASINOPARK,
            BINGOHIGHWAY,
        ],
    TRAINREGION:
        [
            RAILCANYON,
            BULLETSTATION,
        ],
    BIGPLANTREGION:
        [
            FROGFOREST,
            LOSTJUNGLE,
        ],
    GHOSTREGION:
        [
            HANGCASTLE,
            MYSTICMANSION,
        ],
    SKYREGION:
        [
            EGGFLEET,
            FINALFORTRESS,
        ],
}


ability_item_req_counts = \
{
    AMYHAMMERHOVER: 0,
    HOMINGATTACK: 1,
    TORNADO: 2,
    ROCKETACCEL: 2,
    LIGHTDASH: 3,
    TRIANGLEJUMP: 3, #maybe separate tri jump and light dash
    LIGHTATTACK: 3,

    DUMMYRINGS: 1,
    CHEESECANNON: 1,
    FLOWERSTING: 1,
    THUNDERSHOOT: 2,
    FLIGHT: 3,

    BREAK: 0,
    COMBOFINISHER: 1,
    GLIDE: 2,
    FIREDUNK: 3,
    ULTIMATEFIREDUNK: 3,
    BELLYFLOP: 3,
}


character_abilities = \
{
    SPEED:
        [
            HOMINGATTACK,
            TORNADO,
            ROCKETACCEL,
        ],
    FLYING:
        [
            THUNDERSHOOT,
            FLIGHT,
        ],
    POWER:
        [
            #POWERATTACK,
            GLIDE,
            COMBOFINISHER,
            FIREDUNK,
        ],
    CHARSONIC:
        [
            LIGHTDASH,
            TRIANGLEJUMP,
            LIGHTATTACK,
        ],
    CHARTAILS:
        [
            DUMMYRINGS
        ],
    CHARKNUCKLES:
        [],
}



def get_csv_file_name(team: str, level: str, file_type: str, secret: bool = False) -> str:
    if secret:
        return f"{level} {SECRET} {team} {file_type}".replace(" ", "")

    return f"{level} {team} {file_type}".replace(" ", "")


def is_there_a_secret_csv_file(team: str, level: str) -> bool:
    if team == SONIC and level == GRANDMETROPOLIS:
        return True
    return False


def get_char_name_from_team(team: str, speed = False, flying = False, power = False):
    if sum([speed, flying, power]) > 1:
        print(f"Get Char Name From Team called with multiple chars. team {team} speed {speed} flying {flying} power {power}")
        return ""
    if speed:
        return team_char_names[team][0]
    if flying:
        return team_char_names[team][1]
    if power:
        return team_char_names[team][2]
    return ""


def get_region_name_from_level(world: SonicHeroesWorld, level: str) -> str:
    region: str = level_to_game_region[level]
    if world.options.ability_unlocks == 1:
        region = ALLREGIONS
    return region

def get_playable_char_item_name(char: str) -> str:
    return f"{PLAYABLE} {char}"


def get_all_abilities_for_team(team: str):
    result = []
    result += [abilities for char_name in team_char_names[team] for abilities in get_all_abilities_for_character(char_name)]
    return result

def get_all_abilities_for_character(char_name: str):
    result = []
    result += character_abilities[char_name_to_formation[char_name]]
    result += character_abilities[char_name]
    return result


def get_ability_item_name(world: SonicHeroesWorld, team: str, region: str, ability: str) -> str:
    if world.options.ability_unlocks == 1:
        region = ALLREGIONS
    return get_ability_item_name_without_world(team, region, ability)


def get_ability_item_name_without_world(team: str, region: str, ability: str) -> str:
    result = ""
    if team != ANYTEAM:
        result += f"{team} "

    result += f"{ability}"

    if region != ALLREGIONS:
        result += f" {region}"
    return result


def get_all_ability_item_names_for_character_and_region(world: SonicHeroesWorld, team: str, char_name: str, region: str) -> list[str]:
    result = []
    abilities = get_all_abilities_for_character(char_name)

    if world.options.ability_unlocks == 1:
        region = ALLREGIONS

    for ability in abilities:
        result.append(get_ability_item_name(world, team, region, ability))
    return result


def get_stage_obj_item_name(world: SonicHeroesWorld, team: str, region: str, stage_obj: str) -> str:
    if world.options.ability_unlocks == 1:
        region = ALLREGIONS
    return get_stage_obj_item_name_without_world(team, region, stage_obj)


def get_stage_obj_item_name_without_world(team: str, region: str, stage_obj: str) -> str:
    result = ""
    if team != ANYTEAM:
        result += f"{team} "

    result += f"{stage_obj}"

    if region != ALLREGIONS:
        result += f" {region}"
    return result