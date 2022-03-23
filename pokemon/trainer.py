
import util

class PokemonTrainer:
    def __init__(self, name, pokemon, backpack):
        self.name = util.validate_str(name)
        self.pokemon = pokemon
        self.backpack = backpack
    
    def has_remaining_pokemon(self):
        for poke in self.pokemon:
            if not poke.fainted:
                return True
        return False
