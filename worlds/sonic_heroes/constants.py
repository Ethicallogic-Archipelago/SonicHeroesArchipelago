import typing
from dataclasses import dataclass
from BaseClasses import CollectionState, ItemClassification

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
RINGS5 = "5 Rings"
RINGS10 = "10 Rings"
RINGS20 = "20 Rings"
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


NOTHING = "Nothing"
HOMINGATTACK = "Homing Attack"
TORNADO = "Tornado"
ROCKETACCEL = "Rocket Accel"
LIGHTDASH = "Light Dash"
TRIANGLEJUMP = "Triangle Jump"
LIGHTATTACK = "Light Attack"

THUNDERSHOOT = "ThunderShoot"
FLIGHT = "Flight"
FLOWERSTING = "FlowerSting"
FLYINGCHARACTERSPECIALMOVE = "Flying Character Special Move"

POWERATTACK = "Power Attack"
BREAK = "Break"
BREAKKEYCAGE = "Break Key Cage"
FIREDUNK = "Fire Dunk"
SLAM = "Slam"
GLIDE = "Glide"
COMBOFINISHER = "Combo Finisher"

TEAMBLAST = "Team Blast"
GROUNDENEMY = "Ground Enemy"


SECRET = "Secret"
LOCATION = "Location"
LOCATIONS = "Locations"
SECRETLOCATIONS = f"{SECRET} {LOCATIONS}"
REGION = "Region"
CONNECTION = "Connection"
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


csv_file_names = \
{
    SONIC:
        {
            SEASIDEHILL:
                {
                    REGION: "SeasideHillSonicRegions",
                    CONNECTION: "SeasideHillSonicConnections",
                },
            OCEANPALACE:
                {
                    REGION: "OceanPalaceSonicRegions",
                    CONNECTION: "OceanPalaceSonicConnections",
                },
            GRANDMETROPOLIS:
                {
                    REGION: "GrandMetropolisSonicRegions",
                    CONNECTION: "GrandMetropolisSonicConnections",
                },
            POWERPLANT:
                {
                    REGION: "PowerPlantSonicRegions",
                    CONNECTION: "PowerPlantSonicConnections",
                },
            CASINOPARK:
                {
                    REGION: "CasinoParkSonicRegions",
                    CONNECTION: "CasinoParkSonicConnections",
                },

            BINGOHIGHWAY:
                {
                    REGION: "BingoHighwaySonicRegions",
                    CONNECTION: "BingoHighwaySonicConnections",
                },
            RAILCANYON:
                {
                    REGION: "RailCanyonSonicRegions",
                    CONNECTION: "RailCanyonSonicConnections",
                },
            BULLETSTATION:
                {
                    REGION: "BulletStationSonicRegions",
                    CONNECTION: "BulletStationSonicConnections",
                },
            FROGFOREST:
                {
                    REGION: "FrogForestSonicRegions",
                    CONNECTION: "FrogForestSonicConnections",
                },
            LOSTJUNGLE:
                {
                    REGION: "LostJungleSonicRegions",
                    CONNECTION: "LostJungleSonicConnections",
                },
            HANGCASTLE:
                {
                    REGION: "HangCastleSonicRegions",
                    CONNECTION: "HangCastleSonicConnections",
                },
            MYSTICMANSION:
                {
                    REGION: "MysticMansionSonicRegions",
                    CONNECTION: "MysticMansionSonicConnections",
                },
        }
}


secret_csv_file_names = \
{
    SONIC:
        {
            GRANDMETROPOLIS:
                {
                    REGION: "GrandMetropolisSecretSonicRegions",
                    CONNECTION: "GrandMetropolisSecretSonicConnections",
                }
        }
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


progressive_ability_item_names = \
{
    SONIC:
        {
            OCEANREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {OCEANREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {OCEANREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {OCEANREGION}",
                },
            HOTPLANTREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {HOTPLANTREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {HOTPLANTREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {HOTPLANTREGION}",
                },
            CASINOREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {CASINOREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {CASINOREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {CASINOREGION}",
                },
            TRAINREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {TRAINREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {TRAINREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {TRAINREGION}",
                },
            BIGPLANTREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {BIGPLANTREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {BIGPLANTREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {BIGPLANTREGION}",
                },
            GHOSTREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {GHOSTREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {GHOSTREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {GHOSTREGION}",
                },
            SKYREGION:
                {
                    SPEED: f"{PROGRESSIVE} {SPEED} {SONIC} {SKYREGION}",
                    FLYING: f"{PROGRESSIVE} {FLYING} {SONIC} {SKYREGION}",
                    POWER: f"{PROGRESSIVE} {POWER} {SONIC} {SKYREGION}",
                },
        }
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


char_to_item_name = \
{
    SONIC:
        {
            SPEED: PLAYABLESONIC,
            FLYING: PLAYABLETAILS,
            POWER: PLAYABLEKNUCKLES,
        },

}


char_levelup_to_item_name = \
{
    SONIC:
        {
            SPEED: f"{PROGRESSIVELEVELUP} {CHARSONIC}",
            FLYING: f"{PROGRESSIVELEVELUP} {CHARTAILS}",
            POWER: f"{PROGRESSIVELEVELUP} {CHARKNUCKLES}",
        },
    DARK:
        {
            SPEED: f"{PROGRESSIVELEVELUP} {CHARSHADOW}",
            FLYING: f"{PROGRESSIVELEVELUP} {CHARROUGE}",
            POWER: f"{PROGRESSIVELEVELUP} {CHAROMEGA}",
        },
}



ability_to_item_req = \
{
    SONIC:
        {
            OCEANREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][OCEANREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][OCEANREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][OCEANREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][OCEANREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][OCEANREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][OCEANREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][OCEANREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][OCEANREGION][POWER], 3),
                },
            HOTPLANTREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][HOTPLANTREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][HOTPLANTREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][HOTPLANTREGION][POWER], 3),
                },
            CASINOREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][CASINOREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][CASINOREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][CASINOREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][CASINOREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][CASINOREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][CASINOREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][CASINOREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][CASINOREGION][POWER], 3),
                },
            TRAINREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][TRAINREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][TRAINREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][TRAINREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][TRAINREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][TRAINREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][TRAINREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][TRAINREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][TRAINREGION][POWER], 3),
                },
            BIGPLANTREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][BIGPLANTREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][BIGPLANTREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][BIGPLANTREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][BIGPLANTREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][BIGPLANTREGION][POWER], 3),
                },
            GHOSTREGION:
                {
                    HOMINGATTACK: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 1),
                    TORNADO: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 2),
                    ROCKETACCEL: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 2),
                    LIGHTDASH: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 3),
                    TRIANGLEJUMP: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 4),
                    LIGHTATTACK: (progressive_ability_item_names[SONIC][GHOSTREGION][SPEED], 4),

                    THUNDERSHOOT: (progressive_ability_item_names[SONIC][GHOSTREGION][FLYING], 1),
                    FLIGHT: (progressive_ability_item_names[SONIC][GHOSTREGION][FLYING], 2),
                    FLOWERSTING: (progressive_ability_item_names[SONIC][GHOSTREGION][FLYING], 3),

                    BREAK: (progressive_ability_item_names[SONIC][GHOSTREGION][POWER], 0),
                    FIREDUNK: (progressive_ability_item_names[SONIC][GHOSTREGION][POWER], 1),
                    GLIDE: (progressive_ability_item_names[SONIC][GHOSTREGION][POWER], 2),
                    COMBOFINISHER: (progressive_ability_item_names[SONIC][GHOSTREGION][POWER], 3),
                },
        },
}






