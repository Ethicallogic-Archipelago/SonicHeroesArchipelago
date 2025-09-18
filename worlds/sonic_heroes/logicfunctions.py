
from .constants import *


def can_team_blast(world, team, level, state: CollectionState):
    #return False
    return has_char(world, team, level, state, speed=True, flying=True, power=True) #and can_light_attack(world, team, level, state)

def has_char(world, team, level, state: CollectionState, speed=False, flying=False, power=False, orcondition=False):
    conditions = []
    if speed:
        conditions.append(char_to_item_name[team][SPEED])
    if flying:
        conditions.append(char_to_item_name[team][FLYING])
    if power:
        conditions.append(char_to_item_name[team][POWER])

    if orcondition:
        return state.has_any(conditions, world.player)

    else:
        return state.has_all(conditions, world.player)


def has_char_levelup(world, team, level, state: CollectionState, levelup, speed=False, flying=False, power=False):
    if levelup < 1 or levelup > 3:
        print(f"Has Char LevelUp Called with bad LevelUp {levelup}")
        return False
    if sum([speed, flying, power]) > 1:
        print(f"Has Char LevelUp Called with multiple chars. team {team} level {level} levelup {levelup} speed {speed} flying {flying} power {power}")
        return False
    if speed:
        name = char_levelup_to_item_name[team][SPEED]
        return state.has(name, world.player, levelup)
    if flying:
        name = char_levelup_to_item_name[team][FLYING]
        return state.has(name, world.player, levelup)
    if power:
        name = char_levelup_to_item_name[team][POWER]
        return state.has(name, world.player, levelup)
    print(f"Has Char LevelUp Called with no chars")
    return False

def can_homing_attack(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][HOMINGATTACK]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_tornado(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][TORNADO]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_rocket_accel(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][ROCKETACCEL]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_light_dash(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][LIGHTDASH]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_triangle_jump(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][TRIANGLEJUMP]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_light_attack(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][LIGHTATTACK]
    return has_char(world, team, level, state, speed=True) and state.has(name, world.player, amount)

def can_speed_abilities(world, team, level, state: CollectionState, homing=False, tornado=False, rocket=False,lightdash=False, triangle=False, lightattack=False, orcondition=False):
    if not homing and not tornado and not rocket and not lightdash and not triangle and not lightattack:
        return False
    result = not orcondition
    if homing:
        if orcondition:
            result = result or can_homing_attack(world, team, level, state)
        else:
            result = result and can_homing_attack(world, team, level, state)
    if tornado:
        if orcondition:
            result = result or can_tornado(world, team, level, state)
        else:
            result = result and can_tornado(world, team, level, state)
    if rocket:
        if orcondition:
            result = result or can_rocket_accel(world, team, level, state)
        else:
            result = result and can_rocket_accel(world, team, level, state)
    if lightdash:
        if orcondition:
            result = result or can_light_dash(world, team, level, state)
        else:
            result = result and can_light_dash(world, team, level, state)
    if triangle:
        if orcondition:
            result = result or can_light_dash(world, team, level, state)
        else:
            result = result and can_light_dash(world, team, level, state)
    if lightattack:
        if orcondition:
            result = result or can_light_attack(world, team, level, state)
        else:
            result = result and can_light_attack(world, team, level, state)
    return result

def can_thundershoot_ground(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][THUNDERSHOOT]
    return has_char(world, team, level, state, flying=True) and has_char(world, team, level, state, speed=True, power=True, orcondition=True) and state.has(name, world.player, amount)

def can_thundershoot_air(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][THUNDERSHOOT]
    return has_char(world, team, level, state, flying=True) and has_char(world, team, level, state, speed=True, power=True, orcondition=True) and state.has(name, world.player, amount)

def can_thundershoot_both(world, team, level, state: CollectionState):
    return can_thundershoot_ground(world, team, level, state) and can_thundershoot_air(world, team, level, state)


def can_fly(world, team, level, state: CollectionState, speedreq=False, powerreq=False, orcondition=False):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][FLIGHT]
    result = True
    if speedreq or powerreq:
        result = result and has_char(world, team, level, state, speed=speedreq, power=powerreq, orcondition=orcondition)
    return has_char(world, team, level, state, flying=True) and state.has(name, world.player, amount) and result

def can_flower_sting(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][FLOWERSTING]
    return has_char(world, team, level, state, flying=True) and state.has(name, world.player, amount) and team == CHAOTIX


"""
def can_fake_ring_toss(world, team, level, state: CollectionState):
    return (team == SONIC or team == DARK) and (has_char(world, team, level, state, flying=True) and not has_char(world, team, level, state, speed=True, power=True, orcondition=True))

def can_cheese_cannon(world, team, level, state: CollectionState):
    return team == ROSE and (has_char(world, team, level, state, flying=True) and not has_char(world, team, level, state, speed=True, power=True, orcondition=True))

def can_flower_sting_attack(world, team, level, state: CollectionState):
    return can_flower_sting(world, team, level, state) and not has_char(world, team, level, state, speed=True, power=True, orcondition=True)
"""

def can_flying_abilities(world, team, level, state: CollectionState, thundershootair=False, thundershootground=False, thundershootboth=False, flyany=False, flyonechar = False, flyspeed = False, flypower = False, flyfull = False, flowersting=False, orcondition=False):
    if not thundershootair and not thundershootground and not thundershootboth and not flyany and not flyonechar and not flyspeed and not flypower and not flyfull and not flowersting:
        return False
    result = not orcondition
    if thundershootair:
        if orcondition:
            result = result or can_thundershoot_air(world, team, level, state)
        else:
            result = result and can_thundershoot_air(world, team, level, state)
    if thundershootground:
        if orcondition:
            result = result or can_thundershoot_ground(world, team, level, state)
        else:
            result = result and can_thundershoot_ground(world, team, level, state)
    if thundershootboth:
        if orcondition:
            result = result or can_thundershoot_both(world, team, level, state)
        else:
            result = result and can_thundershoot_both(world, team, level, state)
    if flyany:
        if orcondition:
            result = result or can_fly(world, team, level, state)
        else:
            result = result and can_fly(world, team, level, state)
    if flyonechar:
        if orcondition:
            result = result or can_fly(world, team, level, state, speedreq=True, powerreq=True, orcondition=True)
        else:
            result = result and can_fly(world, team, level, state, speedreq=True, powerreq=True, orcondition=True)
    if flyspeed:
        if orcondition:
            result = result or can_fly(world, team, level, state, speedreq=True)
        else:
            result = result and can_fly(world, team, level, state, speedreq=True)
    if flypower:
        if orcondition:
            result = result or can_fly(world, team, level, state, powerreq=True)
        else:
            result = result and can_fly(world, team, level, state, powerreq=True)
    if flyfull:
        if orcondition:
            result = result or can_fly(world, team, level, state, speedreq=True, powerreq=True)
        else:
            result = result and can_fly(world, team, level, state, speedreq=True, powerreq=True)
    if flowersting:
        if orcondition:
            result = result or can_flower_sting(world, team, level, state)
        else:
            result = result and can_flower_sting(world, team, level, state)
    return result

def can_break_things(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][BREAK]
    return has_char(world, team, level, state, power=True) and state.has(name, world.player, amount)

def can_break_key_cage(world, team, level, state: CollectionState):
    return True

def can_fire_dunk(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][FIREDUNK]
    return has_char(world, team, level, state, power=True) and has_char(world, team, level, state, speed=True, flying=True, orcondition=True) and state.has(name, world.player, amount)

def can_glide(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][GLIDE]
    return has_char(world, team, level, state, power=True) and state.has(name, world.player, amount)


def can_combo_finsh(world, team, level, state: CollectionState):
    name, amount = ability_to_item_req[team][level_to_game_region[level]][COMBOFINISHER]
    return has_char(world, team, level, state, power=True) and state.has(name, world.player, amount)

def can_power_abilities(world, team, level, state: CollectionState, breaknotcage=False, breakcage=False, firedunk=False, glide=False, combofinsh=False, orcondition=False):
    if not breaknotcage and not breakcage and not firedunk and not glide and not combofinsh:
        return False
    result = not orcondition
    if breaknotcage:
        if orcondition:
            result = result or can_break_things(world, team, level, state)
        else:
            result = result and can_break_things(world, team, level, state)
    if breakcage:
        if orcondition:
            result = result or can_break_key_cage(world, team, level, state)
        else:
            result = result and can_break_key_cage(world, team, level, state)
    if firedunk:
        if orcondition:
            result = result or can_fire_dunk(world, team, level, state)
        else:
            result = result and can_fire_dunk(world, team, level, state)
    if glide:
        if orcondition:
            result = result or can_glide(world, team, level, state)
        else:
            result = result and can_glide(world, team, level, state)
    if combofinsh:
        if orcondition:
            result = result or can_combo_finsh(world, team, level, state)
        else:
            result = result and can_combo_finsh(world, team, level, state)
    return result


def can_remove_ground_enemy_shield(world, team, level, state: CollectionState):
    return (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 3, speed=True)) or can_tornado(world, team, level, state) or can_rocket_accel(world, team, level, state) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_nothing(world, team, level, state: CollectionState):
    return True

def can_kill_ground_enemy_spear(world, team, level, state: CollectionState):
    return (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 1, speed=True)) or can_break_things(world, team, level, state) or (can_thundershoot_both(world, team, level, state) and has_char_levelup(world, team, level, state, 1, flying=True)) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_plain_shield(world, team, level, state: CollectionState):
    return (can_kill_ground_enemy_nothing(world, team, level, state) and can_remove_ground_enemy_shield(world, team, level, state)) or can_break_things(world, team, level, state) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_concrete_shield(world, team, level, state: CollectionState):
    return (can_kill_ground_enemy_nothing(world, team, level, state) and can_remove_ground_enemy_shield(world, team, level, state)) or (can_combo_finsh(world, team, level, state) and has_char_levelup(world, team, level, state, 2, power=True)) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_spike_shield(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_concrete_shield(world, team, level, state)

def can_kill_ground_enemy_klagen(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_cameron(world, team, level, state: CollectionState):
    return can_remove_ground_enemy_shield(world, team, level, state) or can_break_things(world, team, level, state) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_goldcameron(world, team, level, state: CollectionState):
    return can_remove_ground_enemy_shield(world, team, level, state) or can_team_blast(world, team, level, state)

def can_kill_ground_enemy_rhinoliner(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_eggbishop(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_e2000(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_e2000r(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_egghammer(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)

def can_kill_ground_enemy_heavyegghammer(world, team, level, state: CollectionState):
    return can_kill_ground_enemy_nothing(world, team, level, state)


def can_kill_ground_enemy(world, team, level, state: CollectionState, nothing=False, spear = False, plainshield = False, concreteshield = False, spikeshield = False, klagen = False, cameron = False, goldcameron = False, rhinoliner = False, eggbishop = False, e2000 = False, e2000r = False, egghammer = False, heavyegghammer = False, orcondition = False):
    if not nothing and not spear and not plainshield and not spikeshield and not klagen and not cameron and not goldcameron and not rhinoliner and not eggbishop and not e2000 and not e2000r and not egghammer and not heavyegghammer:
        return can_kill_ground_enemy_nothing(world, team, level, state)
    result = not orcondition
    if nothing:
        if orcondition:
            result = result or can_kill_ground_enemy_nothing(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_nothing(world, team, level, state)
    if spear:
        if orcondition:
            result = result or can_kill_ground_enemy_spear(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_spear(world, team, level, state)
    if plainshield:
        if orcondition:
            result = result or can_kill_ground_enemy_plain_shield(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_plain_shield(world, team, level, state)
    if concreteshield:
        if orcondition:
            result = result or can_kill_ground_enemy_concrete_shield(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_concrete_shield(world, team, level, state)
    if spikeshield:
        if orcondition:
            result = result or can_kill_ground_enemy_spike_shield(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_spike_shield(world, team, level, state)
    if klagen:
        if orcondition:
            result = result or can_kill_ground_enemy_klagen(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_klagen(world, team, level, state)
    if cameron:
        if orcondition:
            result = result or can_kill_ground_enemy_cameron(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_cameron(world, team, level, state)
    if goldcameron:
        if orcondition:
            result = result or can_kill_ground_enemy_goldcameron(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_goldcameron(world, team, level, state)
    if rhinoliner:
        if orcondition:
            result = result or can_kill_ground_enemy_rhinoliner(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_rhinoliner(world, team, level, state)
    if eggbishop:
        if orcondition:
            result = result or can_kill_ground_enemy_eggbishop(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_eggbishop(world, team, level, state)
    if e2000:
        if orcondition:
            result = result or can_kill_ground_enemy_e2000(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_e2000(world, team, level, state)
    if e2000r:
        if orcondition:
            result = result or can_kill_ground_enemy_e2000r(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_e2000r(world, team, level, state)
    if egghammer:
        if orcondition:
            result = result or can_kill_ground_enemy_egghammer(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_egghammer(world, team, level, state)
    if heavyegghammer:
        if orcondition:
            result = result or can_kill_ground_enemy_heavyegghammer(world, team, level, state)
        else:
            result = result and can_kill_ground_enemy_heavyegghammer(world, team, level, state)
    return result


def can_kill_flying_enemy_red_flapper(world, team, level, state: CollectionState, nothing=False, homing=False, firedunk=False):
    if nothing:
        return True
    return can_kill_flying_enemy_green_lightning(world, team, level, state, homing, firedunk)

def can_kill_flying_enemy_green_shot(world, team, level, state: CollectionState, nothing=False, homing=False, firedunk=False):
    if nothing:
        return True
    return can_kill_flying_enemy_green_lightning(world, team, level, state, homing, firedunk)

def can_kill_flying_enemy_green_lightning(world, team, level, state: CollectionState, homing=False, firedunk=False):
    condition = False
    if homing:
        condition = condition or (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 1, speed=True))
    if firedunk:
        condition = condition or can_fire_dunk(world, team, level, state)
    return (can_thundershoot_both(world, team, level, state) and has_char_levelup(world, team, level, state, 1, flying=True)) or condition or can_team_blast(world, team, level, state)
    # homing 1 or thundershoot 1 or SFA

def can_kill_flying_enemy_yellow_light(world, team, level, state: CollectionState, homing=False, firedunk=False):
    return can_kill_flying_enemy_green_lightning(world, team, level, state, homing, firedunk)

def can_kill_flying_enemy_blue_mgun(world, team, level, state: CollectionState, homing=False, firedunk=False):
    condition = False
    if homing:
        condition = condition or (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 2, speed=True))
    if firedunk:
        condition = condition or can_fire_dunk(world, team, level, state)
    return (can_thundershoot_both(world, team, level, state) and has_char_levelup(world, team, level, state, 2, flying=True)) or condition or can_team_blast(world, team, level, state)
    # homing 2 or thundershoot 2 or SFA

def can_kill_flying_enemy_black_spikey(world, team, level, state: CollectionState, homing=False, firedunk=False):
    return can_kill_flying_enemy_blue_mgun(world, team, level, state, homing, firedunk)

def can_kill_flying_enemy_purple_bombs(world, team, level, state: CollectionState, homing=False, firedunk=False):
    return can_kill_flying_enemy_blue_mgun(world, team, level, state, homing, firedunk)

def can_kill_flying_enemy_silver_armor(world, team, level, state: CollectionState, firedunk=False):
    condition = False
    if firedunk:
        condition = condition or can_fire_dunk(world, team, level, state)
    return ((can_thundershoot_both(world, team, level, state) and has_char_levelup(world, team, level, state, 2, flying=True)) and can_break_things(world, team, level, state)) or condition or can_team_blast(world, team, level, state)
    #thundershoot 2 and break or SFA

def can_kill_flying_enemy_falco(world, team, level, state: CollectionState):
    return (can_thundershoot_both(world, team, level, state) and has_char_levelup(world, team, level, state, 3, flying=True)) or can_team_blast(world, team, level, state)
    #thundershoot 3 or SFA


def can_kill_flying_enemy(world, team, level, state: CollectionState, red_flapper=False, green_shot=False, green_lightning=False, yellow_light=False, blue_mgun=False, black_spikey=False, silver_armor=False, purple_bombs=False, falco=False, nothing=False, homing=False, firedunk=False, orcondition=False):
    if not red_flapper and not green_shot and not green_lightning and not yellow_light and not blue_mgun and not black_spikey and not silver_armor and not purple_bombs and not falco:
        return False
    result = not orcondition
    if red_flapper:
        if orcondition:
            result = result or can_kill_flying_enemy_red_flapper(world, team, level, state, nothing=nothing, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_red_flapper(world, team, level, state, nothing=nothing, homing=homing, firedunk=firedunk)
    if green_shot:
        if orcondition:
            result = result or can_kill_flying_enemy_green_shot(world, team, level, state, nothing=nothing, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_green_shot(world, team, level, state, nothing=nothing, homing=homing, firedunk=firedunk)
    if green_lightning:
        if orcondition:
            result = result or can_kill_flying_enemy_green_lightning(world, team, level, state, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_green_lightning(world, team, level, state, homing=homing, firedunk=firedunk)
    if yellow_light:
        if orcondition:
            result = result or can_kill_flying_enemy_yellow_light(world, team, level, state, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_yellow_light(world, team, level, state, homing=homing, firedunk=firedunk)
    if blue_mgun:
        if orcondition:
            result = result or can_kill_flying_enemy_blue_mgun(world, team, level, state, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_blue_mgun(world, team, level, state, homing=homing, firedunk=firedunk)
    if black_spikey:
        if orcondition:
            result = result or can_kill_flying_enemy_black_spikey(world, team, level, state, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_black_spikey(world, team, level, state, homing=homing, firedunk=firedunk)
    if silver_armor:
        if orcondition:
            result = result or can_kill_flying_enemy_silver_armor(world, team, level, state, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_silver_armor(world, team, level, state, firedunk=firedunk)
    if purple_bombs:
        if orcondition:
            result = result or can_kill_flying_enemy_purple_bombs(world, team, level, state, homing=homing, firedunk=firedunk)
        else:
            result = result and can_kill_flying_enemy_purple_bombs(world, team, level, state, homing=homing, firedunk=firedunk)
    if falco:
        if orcondition:
            result = result or can_kill_flying_enemy_falco(world, team, level, state)
        else:
            result = result and can_kill_flying_enemy_falco(world, team, level, state)
    return result


#Objs Here
#in case I remove tp triggers here
def can_tp_obj(world, team, level, state: CollectionState):
    return True


def can_spring(world, team, level, state: CollectionState, single = False, triple = False, orcondition = False):
    if not single and not triple:
        return False

    result = not orcondition
    if single:
        if orcondition:
            result = result or can_single_spring(world, team, level, state)
        else:
            result = result and can_single_spring(world, team, level, state)
    if triple:
        if orcondition:
            result = result or can_triple_spring(world, team, level, state)
        else:
            result = result and can_triple_spring(world, team, level, state)
    return result



def can_single_spring(world, team, level, state: CollectionState):
    return True


def can_triple_spring(world, team, level, state: CollectionState):
    return True


def can_ring_group(world, team, level, state: CollectionState):
    return True

def can_hint_ring(world, team, level, state: CollectionState):
    return True

def can_switch(world, team, level, state: CollectionState, regular = False, push_pull = False, target = False, orcondition = False):
    if not regular and not push_pull and not target:
        return False

    result = not orcondition
    if regular:
        if orcondition:
            result = result or can_regular_switch(world, team, level, state)
        else:
            result = result and can_regular_switch(world, team, level, state)

    if push_pull:
        if orcondition:
            result = result or can_push_pull_switch(world, team, level, state)
        else:
            result = result and can_push_pull_switch(world, team, level, state)

    if target:
        if orcondition:
            result = result or can_target_switch(world, team, level, state)
        else:
            result = result and can_target_switch(world, team, level, state)

    return result

def can_regular_switch(world, team, level, state: CollectionState):
    return True

def can_push_pull_switch(world, team, level, state: CollectionState):
    return True

def can_target_switch(world, team, level, state: CollectionState):
    return True

def can_dash_panel(world, team, level, state: CollectionState):
    return True


def can_dash_ring(world, team, level, state: CollectionState):
    return True


def can_rainbow_hoops(world, team, level, state: CollectionState):
    return True


def can_dash_ramp(world, team, level, state: CollectionState):
    return True

def can_cannon_obj(world, team, level, state: CollectionState):
    return True

def can_cannon(world, team, level, state: CollectionState, speed=False, flying=False, power=False, orcondition=False):
    if not speed and not flying and not power:
        return False

    result = not orcondition
    if speed:
        if orcondition:
            result = result or can_cannon_speed(world, team, level, state)
        else:
            result = result and can_cannon_speed(world, team, level, state)

    if flying:
        if orcondition:
            result = result or can_cannon_flying(world, team, level, state)
        else:
            result = result and can_cannon_flying(world, team, level, state)

    if power:
        if orcondition:
            result = result or can_cannon_power(world, team, level, state)
        else:
            result = result and can_cannon_power(world, team, level, state)

    return result


def can_cannon_speed(world, team, level, state: CollectionState):
    return can_cannon_obj(world, team, level, state) and has_char(world, team, level, state, speed=True)


def can_cannon_flying(world, team, level, state: CollectionState):
    return can_cannon_obj(world, team, level, state) and has_char(world, team, level, state, flying=True)


def can_cannon_power(world, team, level, state: CollectionState):
    return can_cannon_obj(world, team, level, state) and has_char(world, team, level, state, power=True)

def can_weight(world, team, level, state: CollectionState):
    return True

def can_pulley(world, team, level, state: CollectionState):
    return True

def can_unbreakable_container(world, team, level, state: CollectionState):
    return True

def can_propeller(world, team, level, state: CollectionState):
    return True and (can_tornado(world, team, level, state) or can_rocket_accel(world, team, level, state)) or (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 3, speed=True))

def can_pole(world, team, level, state: CollectionState):
    return True and (can_tornado(world, team, level, state) or can_rocket_accel(world, team, level, state)) or (can_homing_attack(world, team, level, state) and has_char_levelup(world, team, level, state, 3, speed=True))

def can_gong(world, team, level, state: CollectionState):
    return True

def can_fan(world, team, level, state: CollectionState):
    return True and can_glide(world, team, level, state)


def can_ruins(world, team, level, state: CollectionState):
    return True


def can_small_stone_platform(world, team, level, state: CollectionState):
    return True


def can_falling_stone_structure(world, team, level, state: CollectionState):
    return True

def can_accel_road(world, team, level, state: CollectionState):
    return True

def can_falling_bridge(world, team, level, state: CollectionState):
    return True

def can_tilting_bridge(world, team, level, state: CollectionState):
    return True

def can_energy_column(world, team, level, state: CollectionState):
    return True

def can_elevator(world, team, level, state: CollectionState):
    return True

def can_pp_upward_path(world, team, level, state: CollectionState):
    return True

def can_shutter(world, team, level, state: CollectionState):
    return True

def can_pinball(world, team, level, state: CollectionState):
    return True

def can_green_bumper_spring(world, team, level, state: CollectionState):
    return True

def can_star_panel(world, team, level, state: CollectionState):
    return True

def can_floating_dice(world, team, level, state: CollectionState):
    return True

def can_rail(world, team, level, state: CollectionState):
    return True

def can_rail_switch(world, team, level, state: CollectionState):
    return True

def can_switchable_rail(world, team, level, state: CollectionState):
    return True

def can_3_rail_platform(world, team, level, state: CollectionState):
    return True

def can_rc_door(world, team, level, state: CollectionState):
    """
    This is the Door in Rail Canyon (prob not needed imo)
    """
    return True

def can_engine_core(world, team, level, state: CollectionState):
    return True

def can_big_gun_interior(world, team, level, state: CollectionState):
    return True


def can_barrel(world, team, level, state: CollectionState):
    """
    This refers to the barrel deco obj in rail canyon / bullet station
    """
    return True

def can_green_frog(world, team, level, state: CollectionState):
    return True

def can_black_frog(world, team, level, state: CollectionState):
    return True

def can_small_green_platform(world, team, level, state: CollectionState):
    return True

def can_small_bouncy_mushroom(world, team, level, state: CollectionState):
    return True

def can_tall_tree_platforms(world, team, level, state: CollectionState):
    return True

def can_large_yellow_platform(world, team, level, state: CollectionState):
    return True

def can_bouncy_fruit(world, team, level, state: CollectionState):
    return True

def can_large_bouncy_mushroom(world, team, level, state: CollectionState):
    return True

def can_swinging_vine(world, team, level, state: CollectionState):
    return True



def can_bobsled(world, team, level, state: CollectionState):
    return True
