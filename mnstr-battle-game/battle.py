from ai import Ai_Player
from monsters import Monster
from player import Player


class Battle:
    def __init__(self, player: Player, ai_player: Ai_Player, condition="None") -> None:
        self.field_condition = condition
        self.player = player
        self.ai_player = ai_player

    def round(self):
        player_action = self.player.choose_action()
        ai_action = self.ai_player.ai_action()

        match player_action, ai_action:
            case "":
                pass

    def effect_on(self, targets: tuple[Monster, Monster]):
        for monster in targets:
            match self.field_condition:
                case "sandstorm":
                    if monster.type not in ["sand", "ground"]:
                        monster.c_hp -= monster.max_hp * 0.05
                case "hail":
                    if monster.type != "ice":
                        monster.c_hp -= monster.max_hp * 0.05
