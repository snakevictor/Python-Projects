from items import Item
from monsters import Monster
from moves import Move
from team import Team


class Player:
    def __init__(self, team: Team, inventory: list[Item]) -> None:
        self.team = team
        self.inventory = inventory

    def choose_action(self):
        player_input = input()
        return self.return_action(player_input)

    def choose_attack(self) -> Move | None:
        attacks = [move for move in self.team.active_monster.moves]
        player_input = int(input())
        choice = attacks[player_input]
        return choice

    def choose_item(self) -> Item | None:
        items = [item for item in self.inventory]
        player_input = int(input())
        choice = items[player_input]
        return choice

    def choose_monster(self) -> Monster | None:
        monsters = [monster for monster in self.team.team_list]
        player_input = int(input())
        choice = monsters[player_input]
        return choice

    def return_action(self, choice) -> Move | Monster | Item:
        _return: Move | Monster | Item | None
        if choice == "attack":
            _return = self.choose_attack()
        elif choice == "item":
            _return = self.choose_item()
        elif choice == "monster":
            _return == self.choose_monster()
        if _return is None:
            return self.choose_action()
        return _return
