from trainer import PokemonTrainer


class BattleEngineInfo:
    STATUS_GOOD = "good"
    STATUS_LOST = "lost"

    def __init__(self, battler: PokemonTrainer, status=STATUS_GOOD):
        self.battler = battler
        self.status = status


class BattleEngine:
    STATUS_GOOD = "good"
    STATUS_LOST = "lost"

    def __init__(self, battler1: PokemonTrainer, battler2: PokemonTrainer):
        self.turn_order = [
            BattleEngineInfo(battler1),
            BattleEngineInfo(battler2),
        ]
        self.turn_index = 0

    def increment_turn_order(self):
        self.turn_index = (self.turn_index + 1) % len(self.turn_order)

    def get_current_battler(self):
        return self.turn_order[self.turn_index]
    
    def get_current_opponent(self):
        opponent_index = (self.turn_index + 1) % len(self.turn_order)
        return self.turn_order[opponent_index]
    
    def change_current_battler_status(self, status):
        self.turn_order[self.turn_index].status = status
    
    def prompt_current_battler(self):
        battler_info = self.get_current_battler()
        battler = battler_info.battler

        print(f"It is {battler.name}'s turn!")
        print(f"What would you like to do?")

        print(f"1. Attack")
        print(f"2. Forfeit")

        response = input()
        return response

    def resolve_action(self, response):
        battler_info = self.get_current_battler()
        battler = battler_info.battler

        if response == "attack":
            print("attack!!!")
        else:
            print(f"Trainer {battler.name} has forfeited the match!")
            self.change_current_battler_status(BattleEngine.STATUS_LOST)
    
    def attack_pokemon(self, attacker, move, defender):
        return
    
    def determine_winner(self):
        if self.get_current_battler().status == BattleEngine.STATUS_LOST:
            return self.get_current_opponent().battler
        elif self.get_current_opponent().status == BattleEngine.STATUS_LOST:
            return self.get_current_battler().battler
        else:
            return None
