import util
from enum import Enum

class PokemonTypeName(Enum):
    electric = 1
    water = 2
    grass = 3
    fire = 4
    rock = 5

class PokemonType:
    def __init__(self,
            name: PokemonTypeName,
            effective_against: list[PokemonTypeName] = None,
            ineffective_against: list[PokemonTypeName] = None,
            immune_against: list[PokemonTypeName] = None,
            no_effect_against: list[PokemonTypeName] = None):
        self.name = name
        self.effective_against = util.validate_or_default_list(effective_against)
        self.ineffective_against = util.validate_or_default_list(ineffective_against)
        self.immune_against = util.validate_or_default_list(immune_against)
        self.no_effect_against = util.validate_or_default_list(no_effect_against)
    
    def __repr__(self):
        return self.name


ELECTRIC_TYPE = PokemonType(
    name=PokemonTypeName.electric,
    effective_against=[PokemonTypeName.water],
    ineffective_against=[PokemonTypeName.grass]
)

WATER_TYPE = PokemonType(PokemonTypeName.water)
GRASS_TYPE = PokemonType(PokemonTypeName.grass)
FIRE_TYPE = PokemonType(PokemonTypeName.fire)
ROCK_TYPE = PokemonType(PokemonTypeName.rock)
