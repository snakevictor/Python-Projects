from dataclasses import dataclass

from monsters import Monster


@dataclass
class Team:
    team_list: list[Monster]
    active_monster: Monster

    def can_battle(self):
        if any(monster.can_battle() for monster in self.team):
            return True
        return False
