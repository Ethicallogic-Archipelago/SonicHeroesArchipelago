from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.sonic_heroes import SonicHeroesWorld

from .constants import *
from .logicfunctions import *


def create_logic_mapping_dict_seaside_hill_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,  # No rules

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicSH": lambda state: can_break_key_cage(world, SONIC, SEASIDEHILL, state),

        "BreakKeyCageandRuinsSonicSH": lambda state: can_break_key_cage(world, SONIC, SEASIDEHILL, state) and can_ruins(world, SONIC, SEASIDEHILL, state),

        "BreakorCannonPowerSonicSH": lambda state: can_break_things(world, SONIC, SEASIDEHILL, state) or can_cannon_power(world, SONIC, SEASIDEHILL, state),

        "FlyingFullorRuinsSonicSH": lambda state: can_ruins(world, SONIC, SEASIDEHILL, state) or can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True),

        "FlyingFullSonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True),

        "FlyingOneCharorTripleSpringSonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True, orcondition=True) or can_triple_spring(world, SONIC, SEASIDEHILL, state),

        "FlyingFullor(RuinsandSingleSpringandSmallStonePlatform)SonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True) or (can_ruins(world, SONIC, SEASIDEHILL, state) and can_single_spring(world, SONIC, SEASIDEHILL, state) and can_small_stone_platform(world, SONIC, SEASIDEHILL, state)),

        "DashRampSonicSH": lambda state: can_dash_ramp(world, SONIC, SEASIDEHILL, state),

        "DashPanelorSpeedSonicSH": lambda state: can_dash_panel(world, SONIC, SEASIDEHILL, state) or has_char(world, SONIC, SEASIDEHILL, state, speed=True),

        "SingleSpringSonicSH": lambda state: can_single_spring(world, SONIC, SEASIDEHILL, state),

        "(BreakandSingleSpring)orFlyingAnySonicSH": lambda state: (can_break_things(world, SONIC, SEASIDEHILL, state) and can_single_spring(world, SONIC, SEASIDEHILL, state)) or can_fly(world, SONIC, SEASIDEHILL, state),

        "(BreakandTripleSpring)orFlyingAnySonicSH": lambda state: (can_break_things(world, SONIC, SEASIDEHILL, state) and can_triple_spring(world, SONIC, SEASIDEHILL, state)) or can_fly(world, SONIC, SEASIDEHILL, state),

        "FlyingAnySonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state),

        "FlyingAnyandSmallStonePlatformSonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state) and can_small_stone_platform(world, SONIC, SEASIDEHILL, state),

        "FlyingAnyorTripleSpringSonicSH": lambda state: can_fly(world, SONIC,SEASIDEHILL, state) or can_triple_spring(world, SONIC, SEASIDEHILL, state),

        "BreakorFlyingAnyorHomingSonicSH": lambda state: can_break_things(world, SONIC, SEASIDEHILL, state) or can_fly(world, SONIC, SEASIDEHILL, state) or can_homing_attack(world, SONIC, SEASIDEHILL, state),

        "BreakorFlyingAnySonicSH": lambda state: can_break_things(world, SONIC, SEASIDEHILL, state) or can_fly(world, SONIC, SEASIDEHILL, state),

        "(CannonAnyorFlyingFull)andRuinsSonicSH": lambda state: (can_cannon(world, SONIC, SEASIDEHILL, state, speed=True, flying=True, power=True, orcondition=True) or can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True)) and can_ruins(world, SONIC, SEASIDEHILL, state),

        "FlyingFullandRuinsSonicSH": lambda state: can_ruins(world, SONIC, SEASIDEHILL, state) and can_fly(world, SONIC, SEASIDEHILL, state, speedreq=True, powerreq=True),

        "CannonSpeedSonicSH": lambda state: can_cannon(world, SONIC, SEASIDEHILL, state, speed=True),

        "CannonFlyingSonicSH": lambda state: can_cannon(world, SONIC, SEASIDEHILL, state, flying=True),

        "CannonPowerSonicSH": lambda state: can_cannon(world, SONIC, SEASIDEHILL, state, power=True),

        "DashRingorFlyingAnySonicSH": lambda state: can_dash_ring(world, SONIC, SEASIDEHILL, state) or can_fly(world, SONIC, SEASIDEHILL, state),

        "DashRampandDashRingandFlyingAnySonicSH": lambda state: can_dash_ramp(world, SONIC, SEASIDEHILL, state) and can_dash_ring(world, SONIC, SEASIDEHILL, state) and can_fly(world, SONIC, SEASIDEHILL, state),

        "FlyingAnyandRuinsSonicSH": lambda state: can_fly(world, SONIC, SEASIDEHILL, state) and can_ruins(world, SONIC, SEASIDEHILL, state),

        "RuinsSonicSH": lambda state: can_ruins(world,SONIC,SEASIDEHILL, state),

        "DashPanelor(DashRingandFlyingAny)orSpeedSonicSH": lambda state: can_dash_panel(world,SONIC,SEASIDEHILL, state) or (can_dash_ring(world,SONIC,SEASIDEHILL, state) and can_fly(world,SONIC,SEASIDEHILL, state)) or has_char(world,SONIC,SEASIDEHILL, state, speed=True),

        "((BreakorHoming)andSingleSpring)orFlyingAnySonicSH": lambda state: ((can_break_things(world,SONIC,SEASIDEHILL, state) or can_homing_attack(world,SONIC,SEASIDEHILL, state)) and can_single_spring(world,SONIC,SEASIDEHILL, state)) or can_fly(world,SONIC,SEASIDEHILL, state),

        "TripsleSpringSonicSH": lambda state: can_triple_spring(world, SONIC, SEASIDEHILL, state),

        "DashRingandFlyingAnyandSingleSpringSonicSH": lambda state: can_dash_ring(world, SONIC, SEASIDEHILL, state) and can_fly(world, SONIC, SEASIDEHILL, state) and can_single_spring(world, SONIC, SEASIDEHILL, state),

        "Breakand(DashRingorFlyingAny)andSingleSpringSonicSH": lambda state: can_break_things(world, SONIC, SEASIDEHILL, state) and (can_dash_ring(world, SONIC, SEASIDEHILL, state) or can_fly(world, SONIC, SEASIDEHILL, state)) and can_single_spring(world, SONIC, SEASIDEHILL, state),

        "DashRingandFlyingAnySonicSH": lambda state: can_dash_ring(world, SONIC, SEASIDEHILL, state) and can_fly(world, SONIC, SEASIDEHILL, state),

        "GlideandRuinsandTripleSpringSonicSH": lambda state: can_glide(world, SONIC, SEASIDEHILL, state) and can_ruins(world, SONIC, SEASIDEHILL, state) and can_triple_spring(world, SONIC, SEASIDEHILL, state),

        "DashRampandRuinsSonicSH": lambda state: can_dash_ramp(world, SONIC, SEASIDEHILL, state) and can_ruins(world, SONIC, SEASIDEHILL, state),

        "BobsledSonicSH": lambda state: can_bobsled(world, SONIC, SEASIDEHILL, state),

        "TripleSpringSonicSH": lambda state: can_triple_spring(world, SONIC, SEASIDEHILL, state),

        "DashRingandSingleSpringSonicSH": lambda state: can_dash_ring(world, SONIC, SEASIDEHILL, state) and can_single_spring(world, SONIC, SEASIDEHILL, state),

        "DashRingSonicSH": lambda state: can_dash_ring(world, SONIC, SEASIDEHILL, state)
    }

def create_logic_mapping_dict_ocean_palace_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicOP": lambda state: can_break_key_cage(world, SONIC, OCEANPALACE, state),

        "DashRampSonicOP": lambda state: can_dash_ramp(world, SONIC, OCEANPALACE, state),

        "FlyingAnyorTripleSpringSonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state) or can_triple_spring(world, SONIC, OCEANPALACE, state),

        "BreakSonicOP": lambda state: can_break_things(world, SONIC, OCEANPALACE, state),

        "(DashRingorFlyingAny)andFallingStoneStructureSonicOP": lambda state: (can_dash_ring(world, SONIC, OCEANPALACE, state) or can_fly(world, SONIC, OCEANPALACE, state)) and can_falling_stone_structure(world, SONIC, OCEANPALACE, state),

        "FanandGlideSonicOP": lambda state: can_fan(world, SONIC, OCEANPALACE, state) and can_glide(world, SONIC, OCEANPALACE, state),

        "FallingStoneStructureandFlyingAnySonicOP": lambda state: can_falling_stone_structure(world, SONIC, OCEANPALACE, state) and can_fly(world, SONIC, OCEANPALACE, state),

        "FlyingAnySonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state),

        "FlyingFullSonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True),

        "TriangleJumpSonicOP": lambda state: can_triangle_jump(world, SONIC, OCEANPALACE, state),

        "FlyingFullor(FanandGlide)SonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True) or (can_fan(world, SONIC, OCEANPALACE, state) and can_glide(world, SONIC, OCEANPALACE, state)),

        "DashRampor(FlyingFullandRainbowHoops)SonicOP": lambda state: can_dash_ramp(world, SONIC, OCEANPALACE, state) or (can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True) or can_rainbow_hoops(world, SONIC, OCEANPALACE, state)),

        "BreakorFlyingAnySonicOP": lambda state: can_break_things(world, SONIC, OCEANPALACE, state) or can_fly(world, SONIC, OCEANPALACE, state),

        "CannonSpeedSonicOP": lambda state: can_cannon(world, SONIC, OCEANPALACE, state, speed=True),

        "CannonFlyingSonicOP": lambda state: can_cannon(world, SONIC, OCEANPALACE, state, flying=True),

        "CannonPowerSonicOP": lambda state: can_cannon(world, SONIC, OCEANPALACE, state, power=True),

        "KillGroundEnemyConcreteShieldSonicOP": lambda state: can_kill_ground_enemy(world, SONIC, OCEANPALACE, state, concreteshield=True),

        "KillFlyingEnemyGreenShotNothingSonicOP": lambda state: can_kill_flying_enemy(world, SONIC, OCEANPALACE, state, green_shot=True, nothing=True),

        "KillGroundEnemySpearConcreteShieldandKillFlyingEnemyGreenShotNothingSonicOP": lambda state: can_kill_ground_enemy(world, SONIC, OCEANPALACE, state, spear=True, concreteshield=True) and can_kill_flying_enemy(world, SONIC, OCEANPALACE, state, green_shot=True, nothing=True),

        "SingleSpringSonicOP": lambda state: can_single_spring(world, SONIC, OCEANPALACE, state),

        "DashRingandFlyingAnySonicOP": lambda state: can_dash_ring(world, SONIC, OCEANPALACE, state) and can_fly(world, SONIC, OCEANPALACE, state),

        "DashRingandFanandGlideSonicOP": lambda state: can_dash_ring(world, SONIC, OCEANPALACE, state) and can_fan(world, SONIC, OCEANPALACE, state) and can_glide(world, SONIC, OCEANPALACE, state),

        "KillGroundEnemySonicOP": lambda state: can_kill_ground_enemy(world, SONIC, OCEANPALACE, state),

        "FlyingAnyorHomingAttackSonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state) or can_homing_attack(world, SONIC, OCEANPALACE, state),

        "TripleSpringorFlyingFullSonicOP": lambda state: can_triple_spring(world, SONIC, OCEANPALACE, state) or can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True),

        "(FanandGlide)orFlyingFullSonicOP": lambda state: (can_fan(world, SONIC, OCEANPALACE, state) and can_glide(world, SONIC, OCEANPALACE, state)) or can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True),

        "FlyingFullorTripleSpringSonicOP": lambda state: can_fly(world, SONIC, OCEANPALACE, state, speedreq=True, powerreq=True) or can_triple_spring(world, SONIC, OCEANPALACE, state),

        "TripleSpringSonicOP": lambda state: can_triple_spring(world, SONIC, OCEANPALACE, state),

        "DashRingandSpeedcharandSingleSpringandSmallStonePlatformSonicOP": lambda state: can_dash_ring(world, SONIC, OCEANPALACE, state) and has_char(world, SONIC, OCEANPALACE, state, speed=True) and can_single_spring(world, SONIC, OCEANPALACE, state) and can_small_stone_platform(world, SONIC, OCEANPALACE, state),

        "BreakandSingleSpringSonicOP": lambda state: can_break_things(world, SONIC, OCEANPALACE, state) and can_single_spring(world, SONIC, OCEANPALACE, state)
    }

def create_logic_mapping_dict_grand_metropolis_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicGM": lambda state: can_break_key_cage(world, SONIC, GRANDMETROPOLIS, state),

        "DashRampSonicGM": lambda state: can_dash_ramp(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingFullSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state, speedreq=True, powerreq=True),

        "TripleSpringSonicGM": lambda state: can_triple_spring(world, SONIC, GRANDMETROPOLIS, state),

        "HomingAttackSonicGM": lambda state: can_homing_attack(world, SONIC, GRANDMETROPOLIS, state),

        "KillGroundEnemyCameronSonicGM": lambda state: can_kill_ground_enemy(world, SONIC, GRANDMETROPOLIS, state, cameron=True),

        "PushPullSwitchSonicGM": lambda state: can_switch(world, SONIC, GRANDMETROPOLIS, state, push_pull=True),

        "AccelRoadandKillFlyingEnemyRedNothingSonicGM": lambda state: can_accel_road(world, SONIC, GRANDMETROPOLIS, state) and can_kill_flying_enemy(world, SONIC, GRANDMETROPOLIS, state, red_flapper=True, nothing=True),

        "KillFlyingEnemyRedNothingSonicGM": lambda state: can_kill_flying_enemy(world, SONIC, GRANDMETROPOLIS, state, red_flapper=True, nothing=True),

        "BreakNotKeySonicGM": lambda state: can_break_things(world, SONIC, GRANDMETROPOLIS, state),

        "SwitchSonicGM": lambda state: can_switch(world, SONIC, GRANDMETROPOLIS, state, regular=True),

        "KillGroundEnemyNothingSonicGM": lambda state: can_kill_ground_enemy(world, SONIC, GRANDMETROPOLIS, state, nothing=True),

        "LightDashSonicGM": lambda state: can_light_dash(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingAnyorSingleSpringorTripleSpringSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state) or can_single_spring(world, SONIC, GRANDMETROPOLIS, state) or can_triple_spring(world, SONIC, GRANDMETROPOLIS, state),

        "HomingAttackandLightDashSonicGM": lambda state: can_homing_attack(world, SONIC, GRANDMETROPOLIS, state) and can_light_dash(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingAnySonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state),

        "SingleSpringSonicGM": lambda state: can_single_spring(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingAnyorLightDashSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state) or can_light_dash(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingAnyor(HomingAttackandLightDash)SonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state) or (can_homing_attack(world, SONIC, GRANDMETROPOLIS, state) and can_light_dash(world, SONIC, GRANDMETROPOLIS, state)),

        "(FlyingOneCharandUnbreakableContainer)orTripleSpringSonicGM": lambda state: (can_fly(world, SONIC, GRANDMETROPOLIS, state, speedreq=True, powerreq=True, orcondition=True) and can_unbreakable_container(world, SONIC, GRANDMETROPOLIS, state)) or can_triple_spring(world, SONIC, GRANDMETROPOLIS, state),

        "KillGroundEnemySpearConcreteShieldSonicGM": lambda state: can_kill_ground_enemy(world, SONIC, GRANDMETROPOLIS, state, spear=True, concreteshield=True),

        "DashRamporFlyingAnySonicGM": lambda state: can_dash_ramp(world, SONIC, GRANDMETROPOLIS, state) or can_fly(world, SONIC, GRANDMETROPOLIS, state),

        "PoleSonicGM": lambda state: can_pole(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingAnyorHomingorGlideSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state) or can_homing_attack(world, SONIC, GRANDMETROPOLIS, state) or can_glide(world, SONIC, GRANDMETROPOLIS, state),

        "PoleandSwitchSonicGM": lambda state: can_pole(world, SONIC, GRANDMETROPOLIS, state) and can_switch(world, SONIC, GRANDMETROPOLIS, state, regular=True),

        "LightDashorTripleSpringSonicGM": lambda state: can_light_dash(world, SONIC, GRANDMETROPOLIS, state) or can_triple_spring(world, SONIC, GRANDMETROPOLIS, state),

        "CannonSpeedSonicGM": lambda state: can_cannon(world, SONIC, GRANDMETROPOLIS, state, speed=True),

        "CannonFlyingSonicGM": lambda state: can_cannon(world, SONIC, GRANDMETROPOLIS, state, flying=True),

        "CannonPowerSonicGM": lambda state: can_cannon(world, SONIC, GRANDMETROPOLIS, state, power=True),

        "FlyingAnyorTripleSpringSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state) or can_triple_spring(world, SONIC, GRANDMETROPOLIS, state),

        "PoleandSingleSpringSonicGM": lambda state: can_pole(world, SONIC, GRANDMETROPOLIS, state) and can_single_spring(world, SONIC, GRANDMETROPOLIS, state),

        "FlyingOneCharandPoleandThunderShootSonicGM": lambda state: can_fly(world, SONIC, GRANDMETROPOLIS, state, speedreq=True, powerreq=True, orcondition=True) and can_pole(world, SONIC, GRANDMETROPOLIS, state) and can_thundershoot_both(world, SONIC, GRANDMETROPOLIS, state),

        "FallingBridgeandKillGroundEnemyCameronSonicGM": lambda state: can_falling_bridge(world, SONIC, GRANDMETROPOLIS, state) and can_kill_ground_enemy(world, SONIC, GRANDMETROPOLIS, state, cameron=True),

        "DashRingSonicGM": lambda state: can_dash_ring(world, SONIC, GRANDMETROPOLIS, state),

        "AccelRoadandKillGroundEnemyCameronSonicGM": lambda state: can_accel_road(world, SONIC, GRANDMETROPOLIS, state) and can_kill_ground_enemy(world, SONIC, GRANDMETROPOLIS, state, cameron=True),
    }

def create_logic_mapping_dict_power_plant_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicPP": lambda state: can_break_key_cage(world, SONIC, POWERPLANT, state),

        "DashRingSonicPP": lambda state: can_dash_ring(world, SONIC, POWERPLANT, state),

        "SingleSpringSonicPP": lambda state: can_single_spring(world, SONIC, POWERPLANT, state),

        "FlyingAnyorGlideSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_glide(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyRedNothingandPPUpwardPathSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True, nothing=True) and can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyGreenLightningNothingHomingFireDunkandEnergyColumnSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True, nothing=True, homing=True, firedunk=True) and can_energy_column(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyGreenLightningNothingHomingFireDunkandPPUpwardPathSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True, nothing=True, homing=True, firedunk=True) and can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "FlyingAnySonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state),

        "AccelRoadandKillFlyingEnemyGreenLightningNothingHomingFireDunkSonicPP": lambda state: can_accel_road(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True, nothing=True, homing=True, firedunk=True),

        "PPUpwardPathSonicPP": lambda state: can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "FlyingAnyandPulleySonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) and can_pulley(world, SONIC, POWERPLANT, state),

        "EnergyColumnandKillFlyingEnemyGreenLightningSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True),

        "FlyingAnyandPPUpwardPathSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) and can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "FlyingAnyorHomingorGlideSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state) or can_glide(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyRedandPoleandSwitch": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True) and can_pole(world, SONIC, POWERPLANT, state) and can_switch(world, SONIC, POWERPLANT, state, regular=True),

        "FlyingAnyorHomingorPPUpwardPathSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state) or can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyGreenLightningandPoleandSwitch": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True) and can_pole(world, SONIC, POWERPLANT, state) and can_switch(world, SONIC, POWERPLANT, state, regular=True),

        "KillGroundEnemyCameronSonicPP": lambda state: can_kill_ground_enemy(world, SONIC, POWERPLANT, state, cameron=True),

        "PulleySonicPP": lambda state: can_pulley(world, SONIC, POWERPLANT, state),

        "EnergyColumnandFlyingAnyandKillFlyingEnemyRedSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True),

        "EnergyColumnandFlyingAnyandKillGroundEnemyCameronSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state) and can_kill_ground_enemy(world, SONIC, POWERPLANT, state, cameron=True),

        "EnergyColumnandFlyingOneCharandKillFlyingEnemyRedSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state, speedreq=True, powerreq=True, orcondition=True) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True),

        "FlyingAnyorLightDashSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_light_dash(world, SONIC, POWERPLANT, state),

        "EnergyColumnandFlyingAnyandKillFlyingEnemyGreenLightningSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True),

        "FlyingAnyorTripleSpringSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_triple_spring(world, SONIC, POWERPLANT, state),

        "(DashRamporFlyingAny)andElevatorSonicPP": lambda state: (can_dash_ramp(world, SONIC, POWERPLANT, state) or can_fly(world, SONIC, POWERPLANT, state)) and can_elevator(world, SONIC, POWERPLANT, state),

        "FlyingAnyandShutterSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) and can_shutter(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyGreenShotNothingSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_shot=True, nothing=True),

        "ElevatorandFlyingAnySonicPP": lambda state: can_elevator(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state),

        "EnergyColumnandFlyingAnyandKillFlyingEnemyRedNothingSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True, nothing=True),

        "FlyingAnyorGlideorHomingSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_glide(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state),

        "DashPanelorFlyingAnyorLightDashorSpeedCharSonicPP": lambda state: can_dash_panel(world, SONIC, POWERPLANT, state) or can_fly(world, SONIC, POWERPLANT, state) or can_light_dash(world, SONIC, POWERPLANT, state) or has_char(world, SONIC, POWERPLANT, state, speed=True),

        "FlyingFullorPulleySonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state, speedreq=True, powerreq=True) or can_pulley(world, SONIC, POWERPLANT, state),

        "DashPanelorFlyingAnyorSpeedCharSonicPP": lambda state: can_dash_panel(world, SONIC, POWERPLANT, state) or can_fly(world, SONIC, POWERPLANT, state) or has_char(world, SONIC, POWERPLANT, state, speed=True),

        "EnergyColumnandFlyingAnyandKillFlyingEnemyGreenShotSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_shot=True),

        "EnergyColumnand(FlyingAnyorHoming)andKillFlyingEnemyRedHomingSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and (can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state)) and can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True, homing=True),

        "EnergyColumnandFlyingAnySonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyGreenShotNothingandSingleSpringSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_shot=True, nothing=True) and can_single_spring(world, SONIC, POWERPLANT, state),

        "KillFlyingEnemyRedNothingSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True, nothing=True),

        "KillFlyingEnemyRedSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, red_flapper=True),

        "KillFlyingEnemyGreenLightningSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True),

        "KillFlyingEnemyGreenLightningHomingFireDunkSonicPP": lambda state: can_kill_flying_enemy(world, SONIC, POWERPLANT, state, green_lightning=True, homing=True, firedunk=True),

        "EnergyColumnSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state),

        "KillGroundEnemyCameronandSingleSpringSonicPP": lambda state: can_kill_ground_enemy(world, SONIC, POWERPLANT, state, cameron=True),

        "EnergyColumnandKillGroundEnemyCameronSonicPP": lambda state: can_energy_column(world, SONIC, POWERPLANT, state) and can_kill_ground_enemy(world, SONIC, POWERPLANT, state, cameron=True),

        "PoleSonicPP": lambda state: can_pole(world, SONIC, POWERPLANT, state),

        "ElevatorSonicPP": lambda state: can_elevator(world, SONIC, POWERPLANT, state),

        "KillGroundEnemyCameronandPPUpwardPathSonicPP": lambda state: can_kill_ground_enemy(world, SONIC, POWERPLANT, state, cameron=True) and can_pp_upward_path(world, SONIC, POWERPLANT, state),

        "DashRamporFlyingAnySonicPP": lambda state: can_dash_ramp(world, SONIC, POWERPLANT, state) or can_fly(world, SONIC, POWERPLANT, state),

        "DashRingorFlyingAnySonicPP": lambda state: can_dash_ring(world, SONIC, POWERPLANT, state) or can_fly(world, SONIC, POWERPLANT, state),

        "FlyingAnyorHomingSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state),

        "DashRingandFlyingAnySonicPP": lambda state: can_dash_ring(world, SONIC, POWERPLANT, state) and can_fly(world, SONIC, POWERPLANT, state),

        "HomingandLightDashSonicPP": lambda state: can_homing_attack(world, SONIC, POWERPLANT, state) and can_light_dash(world, SONIC, POWERPLANT, state),

        "(FlyingAnyorHoming)andDashRingSonicPP": lambda state: (can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state)) and can_dash_ring(world, SONIC, POWERPLANT, state),

        "(FlyingAnyorHoming)andPulleySonicPP": lambda state: (can_fly(world, SONIC, POWERPLANT, state) or can_homing_attack(world, SONIC, POWERPLANT, state)) and can_pulley(world, SONIC, POWERPLANT, state),

        "FlyingAnyandSingleSpringSonicPP": lambda state: can_fly(world, SONIC, POWERPLANT, state) and can_single_spring(world, SONIC, POWERPLANT, state),
    }

def create_logic_mapping_dict_casino_park_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicCP": lambda state: can_break_key_cage(world, SONIC, CASINOPARK, state),

        "SpringSonicCP": lambda state: can_single_spring(world, SONIC, CASINOPARK, state),

        "PinballandSingleSpringSonicCP": lambda state: can_pinball(world, SONIC, CASINOPARK, state) and can_single_spring(world, SONIC, CASINOPARK, state),

        "FlyingAnyorGlideorHomingorStarPanelSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) or can_glide(world, SONIC, CASINOPARK, state) or can_star_panel(world, SONIC, CASINOPARK, state),

        "TripleSpringSonicCP": lambda state: can_triple_spring(world, SONIC, CASINOPARK, state),

        "FlyingAnyorGreenBumperSpringSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) or can_green_bumper_spring(world, SONIC, CASINOPARK, state),

        "LightDashandSwitchSonicCP": lambda state: can_light_dash(world, SONIC, CASINOPARK, state) and can_switch(world, SONIC, CASINOPARK, state, regular=True),

        "FlyingAnyorGlideorRocketAccelSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) or can_glide(world, SONIC, CASINOPARK, state) or can_rocket_accel(world, SONIC, CASINOPARK, state),

        "PushPullSwitchSonicCP": lambda state: can_switch(world, SONIC, CASINOPARK, state, push_pull=True),

        "FireDunkSonicCP": lambda state: can_fire_dunk(world, SONIC, CASINOPARK, state),

        "PinballSonicCP": lambda state: can_pinball(world, SONIC, CASINOPARK, state),

        "FloatingDiceorFlyingAnySonicCP": lambda state: can_floating_dice(world, SONIC, CASINOPARK, state) or can_fly(world, SONIC, CASINOPARK, state),

        "FlyingAnyandTripleSpringSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) and can_triple_spring(world, SONIC, CASINOPARK, state),

        "SingleSpringSonicCP": lambda state: can_single_spring(world, SONIC, CASINOPARK, state),

        "GongSonicCP": lambda state: can_gong(world, SONIC, CASINOPARK, state),

        "Cannonand(FlyingCharorSpeedChar)andPinballandPulleyandSingleSpringandTripleSpringSonicCP": lambda state: can_cannon(world, SONIC, CASINOPARK, state, speed=True, flying=True, orcondition=True) and can_pinball(world, SONIC, CASINOPARK, state) and can_pulley(world, SONIC, CASINOPARK, state) and can_single_spring(world, SONIC, CASINOPARK, state) and can_triple_spring(world, SONIC, CASINOPARK, state),

        "PulleyandTripleSpringSonicCP": lambda state: can_pulley(world, SONIC, CASINOPARK, state) and can_triple_spring(world, SONIC, CASINOPARK, state),

        "CannonandSpeedCharSonicCP": lambda state: can_cannon(world, SONIC, CASINOPARK, state, speed=True),

        "CannonandFlyingCharSonicCP": lambda state: can_cannon(world, SONIC, CASINOPARK, state, flying=True),

        "FlyingCharand(PowerCharorSpeedChar)andPushPullSwitchSonicCP": lambda state: has_char(world, SONIC, CASINOPARK, state, flying=True) and (has_char(world, SONIC, CASINOPARK, state, speed=True, power=True, orcondition=True)) and can_switch(world, SONIC, CASINOPARK, state, push_pull=True),

        "KillGroundEnemyGoldCameronKlagenPlainShieldSonicCP": lambda state: can_kill_ground_enemy(world, SONIC, CASINOPARK, state, plainshield=True, klagen=True, goldcameron=True),

        "FlyingAnySonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state),

        "DashPanelandSingleSpringSonicCP": lambda state: can_dash_panel(world, SONIC, CASINOPARK, state) and can_single_spring(world, SONIC, CASINOPARK, state),

        "CannonorFloatingDiceorFlyingAnyorGlideorRocketAccelSonicCP": lambda state: can_cannon(world, SONIC, CASINOPARK, state) or can_floating_dice(world, SONIC, CASINOPARK, state) or can_fly(world, SONIC, CASINOPARK, state) or can_glide(world, SONIC, CASINOPARK, state) or can_rocket_accel(world, SONIC, CASINOPARK, state),

        "GreenBumperSpringSonicCP": lambda state: can_green_bumper_spring(world, SONIC, CASINOPARK, state),

        "FlyingAnyandLightDashandPushPullSwitchSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) and can_light_dash(world, SONIC, CASINOPARK, state) and can_switch(world, SONIC, CASINOPARK, state, push_pull=True),

        "FlyingAnyandPushPullSwitchSonicCP": lambda state: can_fly(world, SONIC, CASINOPARK, state) and can_switch(world, SONIC, CASINOPARK, state, push_pull=True),
    }

def create_logic_mapping_dict_bingo_highway_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicBH": lambda state: can_break_key_cage(world, SONIC, BINGOHIGHWAY, state),

        "PinballSonicBH": lambda state: can_pinball(world, SONIC, BINGOHIGHWAY, state),

        "(FlyingAnyorKillFlyingEnemyGreenLightning)andSingleSpringSonicBH": lambda state: (can_fly(world, SONIC, BINGOHIGHWAY, state) or can_kill_flying_enemy(world, SONIC, BINGOHIGHWAY, state, green_lightning=True)) and can_single_spring(world, SONIC, BINGOHIGHWAY, state),

        "KillFlyingEnemyYellowLightHomingFireDunkSonicBH": lambda state: can_kill_flying_enemy(world, SONIC, BINGOHIGHWAY, state, yellow_light=True, homing=True, firedunk=True),

        "TeamBlastSonicBH": lambda state: can_team_blast(world, SONIC, BINGOHIGHWAY, state),

        "FanandGlideSonicBH": lambda state: can_fan(world, SONIC, BINGOHIGHWAY, state) and can_glide(world, SONIC, BINGOHIGHWAY, state),

        "FlyingAnySonicBH": lambda state: can_fly(world, SONIC, BINGOHIGHWAY, state),

        "FireDunkSonicBH": lambda state: can_fire_dunk(world, SONIC, BINGOHIGHWAY, state),

        "SingleSpringSonicBH": lambda state: can_single_spring(world, SONIC, BINGOHIGHWAY, state),

        "KillFlyingEnemySilverArmorFireDunkSonicBH": lambda state: can_kill_flying_enemy(world, SONIC, BINGOHIGHWAY, state, silver_armor=True, firedunk=True),

        "FloatingDiceandSwitchSonicBH": lambda state: can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True),

        "GongandPinballandSingleSpringSonicBH": lambda state: can_gong(world, SONIC, BINGOHIGHWAY, state) and can_pinball(world, SONIC, BINGOHIGHWAY, state) and can_single_spring(world, SONIC, BINGOHIGHWAY, state),

        "DashRingSonicBH": lambda state: can_dash_ring(world, SONIC, BINGOHIGHWAY, state),

        "FloatingDiceandFlyingAnyandKillFlyingEnemySilverArmorFireDunkandSwitchSonicBH": lambda state: can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and can_fly(world, SONIC, BINGOHIGHWAY, state) and can_kill_flying_enemy(world, SONIC, BINGOHIGHWAY, state, silver_armor=True, firedunk=True) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True),

        "FlyingAnyandPulleySonicBH": lambda state: can_fly(world, SONIC, BINGOHIGHWAY, state) and can_pulley(world, SONIC, BINGOHIGHWAY, state),

        "GreenBumperSpringandPinballandSingleSpringSonicBH": lambda state: can_green_bumper_spring(world, SONIC, BINGOHIGHWAY, state) and can_pinball(world, SONIC, BINGOHIGHWAY, state) and can_single_spring(world, SONIC, BINGOHIGHWAY, state),

        "FloatingDiceand(FlyingAnyorGreenBumperSpring)andKillGroundEnemyKlagenSonicBH": lambda state: can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and (can_fly(world, SONIC, BINGOHIGHWAY, state) or can_green_bumper_spring(world, SONIC, BINGOHIGHWAY, state)) and can_kill_ground_enemy(world, SONIC, BINGOHIGHWAY, state, klagen=True),

        "GreenBumperSpringSonicBH": lambda state: can_green_bumper_spring(world, SONIC, BINGOHIGHWAY, state),

        "FloatingDiceorFlyingAnySonicBH": lambda state: can_floating_dice(world, SONIC, BINGOHIGHWAY, state) or can_fly(world, SONIC, BINGOHIGHWAY, state),

        "TripleSpringSonicBH": lambda state: can_triple_spring(world, SONIC, BINGOHIGHWAY, state),

        "KillFlyingEnemySilverArmorFireDunkandSwitchSonicBH": lambda state: can_kill_flying_enemy(world, SONIC, BINGOHIGHWAY, state, silver_armor=True, firedunk=True),

        "KillGroundEnemyPlainShieldKlagenandSwitchSonicBH": lambda state: can_kill_ground_enemy(world, SONIC, BINGOHIGHWAY, state, plainshield=True, klagen=True) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True),

        "FireDunkandPinballSonicBH": lambda state: can_fire_dunk(world, SONIC, BINGOHIGHWAY, state) and can_pinball(world, SONIC, BINGOHIGHWAY, state),

        "FlyingAnyorStarPanelSonicBH": lambda state: can_fly(world, SONIC, BINGOHIGHWAY, state) or can_star_panel(world, SONIC, BINGOHIGHWAY, state),

        "FloatingDiceSonicBH": lambda state: can_floating_dice(world, SONIC, BINGOHIGHWAY, state),

        "((FloatingDiceandSwitch)orWeight)andFlyingAnyandPushPullSwitchSonicBH": lambda state: ((can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True)) or can_weight(world, SONIC, BINGOHIGHWAY, state)) and can_fly(world, SONIC, BINGOHIGHWAY, state) and can_switch(world, SONIC, BINGOHIGHWAY, state, push_pull=True),

        "GongSonicBH": lambda state: can_gong(world, SONIC, BINGOHIGHWAY, state),

        "((FloatingDiceandSwitch)orWeight)andFlyingAnySonicBH": lambda state: ((can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True)) or can_weight(world, SONIC, BINGOHIGHWAY, state)) and can_fly(world, SONIC, BINGOHIGHWAY, state),

        "FlyingFullorTripleSpringSonicBH": lambda state: can_fly(world, SONIC, BINGOHIGHWAY, state, speedreq=True, powerreq=True) or can_triple_spring(world, SONIC, BINGOHIGHWAY, state),

        "FireDunkandFloatingDiceand(FlyingAnyor(GreenBumperSpringandSingleSpring))andSwitchSonicBH": lambda state: can_fire_dunk(world, SONIC, BINGOHIGHWAY, state) and can_floating_dice(world, SONIC, BINGOHIGHWAY, state) and (can_fly(world, SONIC, BINGOHIGHWAY, state) or (can_green_bumper_spring(world, SONIC, BINGOHIGHWAY, state) and can_single_spring(world, SONIC, BINGOHIGHWAY, state))) and can_switch(world, SONIC, BINGOHIGHWAY, state, regular=True),

        "DashRingandSingleSpringSonicBH": lambda state: can_dash_ring(world, SONIC, BINGOHIGHWAY, state) and can_single_spring(world, SONIC, BINGOHIGHWAY, state),

        "DashRingandPinballandSingleSpringSonicBH": lambda state: can_dash_ring(world, SONIC, BINGOHIGHWAY, state) and can_pinball(world, SONIC, BINGOHIGHWAY, state) and can_single_spring(world, SONIC, BINGOHIGHWAY, state),
    }


def create_logic_mapping_dict_rail_canyon_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicRC": lambda state: can_break_key_cage(world, SONIC, RAILCANYON, state),

        "RailSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state),

        "FlyingAnyorSingleSpringSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) or can_single_spring(world, SONIC, RAILCANYON, state),

        "FlyingAnyorSwitchableRailSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) or can_switchable_rail(world, SONIC, RAILCANYON, state),

        "(BarrelandFlyingAny)orPulleySonicRC": lambda state: (can_barrel(world, SONIC, RAILCANYON, state) and can_fly(world, SONIC, RAILCANYON, state)) or can_pulley(world, SONIC, RAILCANYON, state),

        "3RailPlatformSonicRC": lambda state: can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "FlyingAnyand3RailPlatformSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) and can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "RailSwitchSonicRC": lambda state: can_rail_switch(world, SONIC, RAILCANYON, state),

        "FlyingAnyandRailSwitchSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) and can_rail_switch(world, SONIC, RAILCANYON, state),

        "RailSwitchandSwitchableRailSonicRC": lambda state: can_rail_switch(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state),

        "FlyingAnySonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state),

        "RailandSingleSpringSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state) and can_single_spring(world, SONIC, RAILCANYON, state),

        "RailandRailSwitchandSwitchableRailSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state) and can_rail_switch(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state),

        "TripleSpringSonicRC": lambda state: can_triple_spring(world, SONIC, RAILCANYON, state),

        "FlyingAnyandTripleSpringSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) and can_triple_spring(world, SONIC, RAILCANYON, state),

        "PoleSonicRC": lambda state: can_pole(world, SONIC, RAILCANYON, state),

        "RCStationDoorandSwitchSonicRC": lambda state: can_rc_door(world, SONIC, RAILCANYON, state) and can_switch(world, SONIC, RAILCANYON, state, regular=True),

        "RailandSwitchableRailSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state),

        "LightDashand3RailPlatformSonicRC": lambda state: can_light_dash(world, SONIC, RAILCANYON, state) and can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "FlyingAnyor(All3CharsandSwitch)SonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) or (has_char(world, SONIC, RAILCANYON, state, speed=True, flying=True, power=True) and can_switch(world, SONIC, RAILCANYON, state, regular=True)),

        "RailandTripleSpringSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state) and can_triple_spring(world, SONIC, RAILCANYON, state),

        "KillFlyingEnemyPurpleBombSonicRC": lambda state: can_kill_flying_enemy(world, SONIC, RAILCANYON, state, purple_bombs=True),

        "FlyingAnyorPulleySonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) or can_pulley(world, SONIC, RAILCANYON, state),

        "KillGroundEnemyNothingSonicRC": lambda state: can_kill_ground_enemy(world, SONIC, RAILCANYON, state, nothing=True),

        "FlyingAll3CharsandSwitchSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state, speedreq=True, powerreq=True) and can_switch(world, SONIC, RAILCANYON, state, regular=True),

        "SingleSpringSonicRC": lambda state: can_single_spring(world, SONIC, RAILCANYON, state),

        "FlyingAnyandSingleSpringSonicRC": lambda state: can_fly(world, SONIC, RAILCANYON, state) and can_single_spring(world, SONIC, RAILCANYON, state),

        "FanandRailandRailSwitchandSwitchableRailand3RailPlatformSonicRC": lambda state: can_fan(world, SONIC, RAILCANYON, state) and can_rail(world, SONIC, RAILCANYON, state) and can_rail_switch(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state) and can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "FanandRailandRailSwitchandSingleSpringandSwitchableRailand3RailPlatformSonicRC": lambda state: can_fan(world, SONIC, RAILCANYON, state) and can_rail(world, SONIC, RAILCANYON, state) and can_rail_switch(world, SONIC, RAILCANYON, state) and can_single_spring(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state) and can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "RailandRailSwitchandSwitchableRailand3RailPlatformSonicRC": lambda state: can_rail(world, SONIC, RAILCANYON, state) and can_rail_switch(world, SONIC, RAILCANYON, state) and can_switchable_rail(world, SONIC, RAILCANYON, state) and can_3_rail_platform(world, SONIC, RAILCANYON, state),

        "PoleandTargetSwitchSonicRC": lambda state: can_pole(world, SONIC, RAILCANYON, state) and can_target_switch(world, SONIC, RAILCANYON, state),
    }


def create_logic_mapping_dict_bullet_station_sonic(world: SonicHeroesWorld):
    return \
    {
        "": lambda state: True,

        "NOTPOSSIBLE": lambda state: False,

        "BreakKeyCageSonicBS": lambda state: can_break_key_cage(world, SONIC, BULLETSTATION, state),

        "RailSonicBS": lambda state: can_rail(world, SONIC, BULLETSTATION, state),

        "TriangleJumpSonicBS": lambda state: can_triangle_jump(world, SONIC, BULLETSTATION, state),

        "FlyingAnyorWeightSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) or can_weight(world, SONIC, BULLETSTATION, state),

        "FlyingAnySonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state),

        "FireDunkandTPObjSonicBS": lambda state: can_fire_dunk(world, SONIC, BULLETSTATION, state) and can_tp_obj(world, SONIC, BULLETSTATION, state),

        "BreakandEngineCoreSonicBS": lambda state: can_break_things(world, SONIC, BULLETSTATION, state) and can_engine_core(world, SONIC, BULLETSTATION, state),

        "BreakandRailSonicBS": lambda state: can_break_things(world, SONIC, BULLETSTATION, state) and can_rail(world, SONIC, BULLETSTATION, state),

        "SingleSpringandRailSonicBS": lambda state: can_single_spring(world, SONIC, BULLETSTATION, state) and can_rail(world, SONIC, BULLETSTATION, state),

        "CannonSonicBS": lambda state: can_cannon_obj(world, SONIC, BULLETSTATION, state),

        "FlyingAnyandRailSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) and can_rail(world, SONIC, BULLETSTATION, state),

        "CannonSpeedSonicBS": lambda state: can_cannon(world, SONIC, BULLETSTATION, state, speed=True),

        "CannonFlyingSonicBS": lambda state: can_cannon(world, SONIC, BULLETSTATION, state, flying=True),

        "CannonPowerSonicBS": lambda state: can_cannon(world, SONIC, BULLETSTATION, state, power=True),

        "RailandSingleSpringand3RailPlatformSonicBS": lambda state: can_rail(world, SONIC, BULLETSTATION, state) and can_single_spring(world, SONIC, BULLETSTATION, state) and can_3_rail_platform(world, SONIC, BULLETSTATION, state),

        "KillGroundEnemyPlainShieldSonicBS": lambda state: can_kill_ground_enemy(world, SONIC, BULLETSTATION, state, plainshield=True),

        "RailandRailSwitchandSwitchableRailSonicBS": lambda state: can_rail(world, SONIC, BULLETSTATION, state) and can_rail_switch(world, SONIC, BULLETSTATION, state) and can_switchable_rail(world, SONIC, BULLETSTATION, state),

        "BreakandSwitchSonicBS": lambda state: can_break_things(world, SONIC, BULLETSTATION, state) and can_switch(world, SONIC, BULLETSTATION, state, regular=True),

        "SingleSpringSonicBS": lambda state: can_single_spring(world, SONIC, BULLETSTATION, state),

        "FanorRailSonicBS": lambda state: can_fan(world, SONIC, BULLETSTATION, state) or can_rail(world, SONIC, BULLETSTATION, state),

        "PoleSonicBS": lambda state: can_pole(world, SONIC, BULLETSTATION, state),

        "All3CharsandSwitchSonicBS": lambda state: has_char(world, SONIC, BULLETSTATION, state, speed=True, flying=True, power=True) and can_switch(world, SONIC, BULLETSTATION, state, regular=True),

        "FireDunkSonicBS": lambda state: can_fire_dunk(world, SONIC, BULLETSTATION, state),

        "CannonFlyingandDashRingSonicBS": lambda state: can_cannon_flying(world, SONIC, BULLETSTATION, state) and can_dash_ring(world, SONIC, BULLETSTATION, state),

        "BreakSonicBS": lambda state: can_break_things(world, SONIC, BULLETSTATION, state),

        "All3CharsandBreakandSwitchSonicBS": lambda state: has_char(world, SONIC, BULLETSTATION, state, speed=True, flying=True, power=True) and can_break_things(world, SONIC, BULLETSTATION, state) and can_switch(world, SONIC, BULLETSTATION, state, regular=True),

        "BigCannonGunSonicBS": lambda state: can_big_gun_interior(world, SONIC, BULLETSTATION, state),

        "RailandRailSwitchandSwitchableRailand3RailPlatformSonicBS": lambda state: can_rail(world, SONIC, BULLETSTATION, state) and can_rail_switch(world, SONIC, BULLETSTATION, state) and can_switchable_rail(world, SONIC, BULLETSTATION, state) and can_3_rail_platform(world, SONIC, BULLETSTATION, state),

        "FanSonicBS": lambda state: can_fan(world, SONIC, BULLETSTATION, state),

        "FlyingAnyand3RailPlatformSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state),

        "LightDashSonicBS": lambda state: can_light_dash(world, SONIC, BULLETSTATION, state),

        "FlyingAnyandSwitchSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) and can_switch(world, SONIC, BULLETSTATION, state, regular=True),

        "FlyingAnyorPulleySonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) or can_pulley(world, SONIC, BULLETSTATION, state),

        "RailandRailSwitchandSingleSpringandSwitchableRailand3RailPlatformSonicBS": lambda state: can_rail(world, SONIC, BULLETSTATION, state) and can_rail_switch(world, SONIC, BULLETSTATION, state) and can_single_spring(world, SONIC, BULLETSTATION, state) and can_switchable_rail(world, SONIC, BULLETSTATION, state) and can_3_rail_platform(world, SONIC, BULLETSTATION, state),

        "KillGroundEnemyKlagenSonicBS": lambda state: can_kill_ground_enemy(world, SONIC, BULLETSTATION, state, klagen=True),

        "FlyingAll3CharsandSwitchSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state, speedreq=True, powerreq=True) and can_switch(world, SONIC, BULLETSTATION, state, regular=True),

        "FlyingAnyorTripleSpringSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) or can_triple_spring(world, SONIC, BULLETSTATION, state),

        "FlyingAnyorGlideorHomingSonicBS": lambda state: can_fly(world, SONIC, BULLETSTATION, state) or can_glide(world, SONIC, BULLETSTATION, state) or can_homing_attack(world, SONIC, BULLETSTATION, state),

        "BobsledandRailSwitchandSwitchableRailandSingleSpringSonicBS": lambda state: can_bobsled(world, SONIC, BULLETSTATION, state) and can_rail_switch(world, SONIC, BULLETSTATION, state) and can_switchable_rail(world, SONIC, BULLETSTATION, state) and can_single_spring(world, SONIC, BULLETSTATION, state),
    }










