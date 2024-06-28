from dataclasses import dataclass


@dataclass
class Nature:
    atk: int | float
    dff: int | float
    spd: int | float


natures = {
    "neutral": Nature(atk=1, dff=1, spd=1),
    "bold": Nature(atk=0.75, dff=1.25, spd=1),
    "aggro": Nature(atk=1.25, dff=0.75, spd=1),
    "hasty": Nature(atk=0.875, dff=0.875, spd=1.25),
}


class Monster:
    def __init__(self, name, data, nature: Nature, level=0) -> None:
        self.name = name
        self.nature = nature  # applies multiplier to stats
        self.type = data["type"]
        self.max_hp = data["max_hp"]
        self.c_hp = self.max_hp
        self.max_sp = data["max_sp"]
        self.c_sp = self.max_sp
        self.atk = data["atk"] * self.nature.atk
        self.dff = data["dff"] * self.nature.dff
        self.spd = data["spd"] * self.nature.spd
        self.sp_atk = data["sp_atk"]
        self.sp_dff = data["sp_dff"]
        self.eva = 100
        self.acc = 100
        self.moves = list
        self.moveset = data["moveset"]
        self.status = "None"
        self.t_exp = 0
        self.level = level

    def is_hurt(self):
        if self.status == "poisoned":
            psn_dmg = round((self.max_hp * 0.05), None)
            self.c_hp -= 1 if psn_dmg <= 0 else psn_dmg
        elif self.status == "badly poisoned":
            psn_dmg = round((self.max_hp * 0.08), None)
            self.c_hp -= 1 if psn_dmg <= 0 else psn_dmg
        elif self.status == "burned":  # add 2/3 max power
            fire_dmg = round((self.max_hp * 0.075), None)
            self.c_hp -= 1 if fire_dmg <= 0 else fire_dmg
            pass

    def can_attack(self):
        if self.status in ["asleep", "paralyzed"]:
            return False
        return True

    def check_lvl(self):
        pass

    def level_up(self):
        self.atk += self.atk * (self.level / 100) * self.nature.atk
        self.dff += self.atk * (self.level / 100) * self.nature.atk
        self.spd += self.spd * (self.level / 100) * self.nature.spd
        self.sp_atk += self.sp_atk * (self.level / 100)
        self.sp_dff += self.sp_dff * (self.level / 100)
        pass

    def learn_move(self):
        pass

    def evolve(self):
        pass


class Battle:
    def __init__(self, condition="None") -> None:
        self.field_condition = condition

    def effect_on(self, targets: tuple[Monster, Monster]):
        for monster in targets:
            match self.field_condition:
                case "sandstorm":
                    if monster.type not in ["sand", "ground"]:
                        monster.c_hp -= monster.max_hp * 0.05
                case "hail":
                    if monster.type != "ice":
                        monster.c_hp -= monster.max_hp * 0.05


class Moves:
    def __init__(self, name, data) -> None:
        self.name = name
        self.dmg = data["dmg"]
        self.spd = data["spd"]
        self.type = data["type"]
        self.status_effect = data["status_effect"]
        self.battle_effect = data["battle_effect"]
        self.min_lvl = data["learn_level"]

    def status_change(self, target: Monster):
        match self.status_effect:
            case "burn":
                target.status = "burned"
            case "poison":
                target.status = "poisoned"
            case "hard poison":
                target.status = "badly poisoned"
            case "paralysis":
                target.status = "paralyzed"
            case "sleep":
                target.status = "asleep"
            case None:
                pass

    def field_change(self, battle: Battle):
        match self.battle_effect:
            case "sunny":
                battle.field_condition = "sunny"
            case "rainy":
                battle.field_condition = "rainy"
            case "dark":
                battle.field_condition = "dark"
            case "hail":
                battle.field_condition = "hail"
            case "sandstorm":
                battle.field_condition = "sandstorm"
            case "foggy":
                battle.field_condition = "foggy"
