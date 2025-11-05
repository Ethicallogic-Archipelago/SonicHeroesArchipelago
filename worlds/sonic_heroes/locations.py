
from BaseClasses import Location, LocationProgressType

from .constants import *

class SonicHeroesLocation(Location):
    game = SONICHEROES

def create_locations(world, region):

    if region.name in world.region_to_location.keys():
        for loc in world.region_to_location[region.name]:
            rule = None
            if loc.team in world.logic_mapping_dict.keys():
                if loc.level in world.logic_mapping_dict[loc.team].keys():
                    if loc.rulestr in world.logic_mapping_dict[loc.team][loc.level].keys():
                        rule = world.logic_mapping_dict[loc.team][loc.level][loc.rulestr]
                    else:
                        #print(f"Loc {loc.name} is missing the logic mapping for rulestr {loc.rulestr} with team {loc.team} and level {loc.level}")
                        pass
                else:
                    #print(f"Loc {loc.name} is missing the logic mapping for level {loc.level} with team {loc.team} and rulestr {loc.rulestr}")
                    pass
            else:
                #print(f"Loc {loc.name} is missing the logic mapping for team {loc.team} with rulestr {loc.rulestr} and level {loc.level}")
                pass
            create_location(world, region, loc.name, loc.code, rule)


def create_location(world, region, name, code, rule = None):
    #print(f"Creating location {name}")
    loc = Location(world.player, name, code, region)
    loc.access_rule = rule

    if loc.name == METALOVERLORD:
        #print(f"Setting {loc.name} to Excluded")
        loc.progress_type = LocationProgressType.EXCLUDED

    #print(f"Creating Location {name} for region {region.name}")

    region.locations.append(loc)
