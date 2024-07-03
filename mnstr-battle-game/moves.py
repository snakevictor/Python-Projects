from battle import Battle
from monsters import Monster


class Move:
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
