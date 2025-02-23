from typing import List, Dict, Optional, Callable
import math

from BaseClasses import Region, Entrance, EntranceType


from .locations import SonicHeroesLocation



def create_region(world: "SonicHeroesWorld", name: str, locations: List[Dict[str, int]], hint: Optional[str] = None):
    ret = Region(name, world.player, world.multiworld, hint)
    for location in locations:
        #print("location in region is: " + str(location))
        for k, v in location.items():
            if k in world.disabled_locations: #currently not used
                continue

            loc = SonicHeroesLocation(world.player, k, v, ret)
            ret.locations.append(loc)

    world.multiworld.regions.append(ret)


def create_regions(world: "SonicHeroesWorld"):

    #menu
    #menu_region = Region("Menu", world.player, world.multiworld, "This is Menu Region")
    #world.multiworld.regions.append(menu_region)
    create_region(world, "Menu", [], "This is Menu Region")

    """
    final_region = Region("Metal Madness", world.player, world.multiworld, "This is Metal Madness Region")

    for location in world.goal[0]:
        for k, v in location.items():
            loc = SonicHeroesLocation(world.player, k, v, final_region)

    final_region.locations.append(loc)

    world.multiworld.regions.append(final_region)
    """


    #emerald stages
    #print("world.emerald_locs is: " + str(world.emerald_locs))
    for i in range(7):

        #print("world.emerald_locs index : " + str(world.emerald_locs[i]))
        create_region(world, "Emerald " + str(i + 1), world.emerald_locs[i], "Region for Emerald " + str(i + 1))

    #story missions (not bosses)
    for team_index in range(len(world.story_list)):
        for location_number in range(18):

            #print("Creating region: Team " + str(world.story_list[team_index]) + " Mission " + str(location_number + 1))
            #print("This region has locations: " + str(world.team_locs[team_index][location_number]))

            create_region(world, "Team " + str(world.story_list[team_index]) + " Mission " + str(location_number + 1),
            #check team_locs here
             world.team_locs[team_index][location_number], "Region for team " + str(world.story_list[team_index] + " Mission "
              + str(location_number + 1)))

    #for region in world.multiworld.get_regions():
        #for location in region.get_locations():

            #print("This region has these locations: " + str(location))


    #level gates here
    for i in range(world.options.number_level_gates.value + 1):
        create_region(world, "Gate " + str(i), [], "Gate " + str(i) + "Region") #gate_locs is a List of List of locations

    #gate bosses here
    for i in range(world.options.number_level_gates.value):
        create_region(world, "Gate Boss between Gate " + str(i) + " and Gate " +
        str(i + 1), world.gate_boss_locs[i], "Region for Gate Boss " + str(i)) #also a list of list of locations

        print("Region Created: " + "Gate Boss between Gate " + str(i) + " and Gate " +
        str(i + 1) + " and locations in here is: " + str(world.gate_boss_locs[i]))




    #final boss
    #print("world.goal is: " + str(world.goal))
    create_region(world, "Metal Madness", world.goal[0], "This is Metal Madness Region")



    for region in world.multiworld.regions:
        #print("region in list is: " + str(region))
        pass


def connect_entrances(world: "SonicHeroesWorld"):

    names: Dict[str, int] = {}

    connect(world, names, "Menu", "Gate 0")

    #0 is emblems and emeralds
    #1 is emblems
    #2 is emeralds

    if (world.options.goal_unlock_condition.value == 1):

        connect(world, names, "Menu", "Metal Madness", lambda state:
        state.has("Emblem", world.player, world.required_emblems))

    elif (world.options.goal_unlock_condition.value == 2):

        connect(world, names, "Menu", "Metal Madness", lambda state:
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player))

    elif (world.options.goal_unlock_condition.value == 0):


        connect(world, names, "Menu", "Metal Madness", lambda state:
            state.has("Emblem", world.player, world.required_emblems) and
            state.has("Green Chaos Emerald", world.player) and
            state.has("Blue Chaos Emerald", world.player) and
            state.has("Yellow Chaos Emerald", world.player) and
            state.has("White Chaos Emerald", world.player) and
            state.has("Cyan Chaos Emerald", world.player) and
            state.has("Purple Chaos Emerald", world.player) and
            state.has("Red Chaos Emerald", world.player))


    #here is levels
    if world.options.number_level_gates.value == 0:

        for team in world.story_list:
            for location_number in range(18):
                connect(world, names, "Gate 0", "Team " + str(team) + " Mission " + str(location_number + 1))

                if (location_number + 1 in world.emerald_mission_numbers):
                    connect(world, names, "Gate 0", "Emerald " + str(location_number + 1))

    else:

        number_of_missions_per_gate = math.floor((len(world.story_list) * 18) /
        (world.options.number_level_gates.value + 1))

        total_missions = 18 * len(world.story_list)

        extra_missions = total_missions % number_of_missions_per_gate

        placed_missions = 0

        for gate_i in range(world.options.number_level_gates.value + 1):

            for mission_ii in range(number_of_missions_per_gate):

                x = world.shuffleable_level_list[placed_missions]

                #gate 0
                connect(world, names, "Gate " + str(gate_i), "Team " + str(world.story_list[math.floor((x - 1) / 18)]) + " Mission " + str(((x - 1) % 18) + 1))

                print("Connecting Region: " + "Gate " + str(gate_i) + " to Region: " + "Team " + str(world.story_list[math.floor((x - 1) / 18)]) + " Mission " + str(((x - 1) % 18) + 1))

                placed_missions += 1

                if (((x - 1) % 18) + 1 in world.emerald_mission_numbers):
                    connect(world, names, "Gate " + str(gate_i), "Emerald " + str(int((((x - 1) % 18) + 1) / 2)))

                    print("Connecting Region: " + "Gate " + str(gate_i) + " to Region: " + "Emerald " + str(int((((x - 1) % 18) + 1) / 2)))

            if extra_missions > 0:

                x = world.shuffleable_level_list[placed_missions]
                #gate 0
                connect(world, names, "Gate " + str(gate_i), "Team " + str(world.story_list[math.floor((x - 1) / 18)]) + " Mission " + str(((x - 1) % 18) + 1))

                print("Connecting Region: " + "Gate " + str(gate_i) + " to Region: " + "Team " + str(world.story_list[math.floor((x - 1) / 18)]) + " Mission " + str(((x - 1) % 18) + 1))

                placed_missions += 1

                extra_missions -= 1

                if (((x - 1) % 18) + 1 in world.emerald_mission_numbers):
                    connect(world, names, "Gate " + str(gate_i), "Emerald " + str(int((((x - 1) % 18) + 1) / 2)))
                    print("Connecting Region: " + "Gate " + str(gate_i) + " to Region: " + "Emerald " + str(int((((x - 1) % 18) + 1) / 2)))

            if gate_i == 0:
                connect(world, names, "Menu", "Gate " + str(gate_i))

            else:

                #gate boss
                #"Gate Boss between Gate " + str(i) + " and Gate " + str(i + 1)
                #"Boss Gate Item " + str(i + 1)

                connect(world, names, "Gate " + str(gate_i - 1), "Gate Boss between Gate " + str(gate_i - 1) +
                " and Gate " + str(gate_i), lambda state, gate_i_= gate_i: state.has("Emblem", world.player, world.gate_cost * gate_i_))

                #connect(world, names, "Gate " + str(gate_i - 1), "Gate Boss between Gate " + str(gate_i - 1) +
                #" and Gate " + str(gate_i))


                print("Connecting Region: " + "Gate " + str(gate_i - 1) + " to Region: " + "Gate Boss between Gate " + str(gate_i - 1) +
                " and Gate " + str(gate_i) + " ::: And the rule is needed emblems: " + str(world.gate_cost * gate_i))

                #connect(world, names, "Gate Boss between Gate " + str(gate_i - 1) +
                #" and Gate " + str(gate_i), "Gate " + str(gate_i), lambda state: state.has("Boss Gate Item " + str(gate_i), world.player))

                #connect(world, names, "Menu", "Gate " + str(gate_i), lambda state: state.has("Boss Gate Item " + str(gate_i), world.player))

                connect(world, names, "Menu", f"Gate {gate_i}", lambda state, gate_i_=gate_i: state.has(f"Boss Gate Item {gate_i_}", world.player))


                print("Connecting Region: " + "Menu" + " to Region: " + "Gate " + str(gate_i) + " ::: And the rule is Boss Gate Item " + str(gate_i))



def connect(
    world: "SonicHeroesWorld",
    used_names: Dict[str, int],
    source: str,
    target: str,
    rule: Optional[Callable] = None,
    reach: Optional[bool] = False,
) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (" " * used_names[target])

    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
    return connection if reach else None

