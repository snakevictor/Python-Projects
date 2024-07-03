from items import Item
from team import Team


class Ai_Player:
    def __init__(self, team: Team, inventory: list[Item]) -> None:
        self.team = team
        self.inventory = inventory

    def ai_action(self):
        pass
