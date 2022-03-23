import util

class PokemonType:
    def __init__(self,
            name,
            effective_against=None,
            ineffective_against=None,
            immune_against=None,
            no_effect_against=None):
        self.name = util.validate_str(name)
        self.effective_against = util.validate_or_default_list(effective_against)
        self.ineffective_against = util.validate_or_default_list(ineffective_against)
        self.immune_against = util.validate_or_default_list(immune_against)
        self.no_effect_against = util.validate_or_default_list(no_effect_against)
    
    def __repr__(self):
        return self.name

ELECTRIC_TYPE = PokemonType("electric")
WATER_TYPE = PokemonType("water")
GRASS_TYPE = PokemonType("grass")
FIRE_TYPE = PokemonType("fire")
ROCK_TYPE = PokemonType("rock")
